import os
import json
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from config.paths import TEMPLATE_DIRECTORY, STATIC_DIRECTORY
from Model.scripts.recommender import recommend, load_recommendation_models

app = Flask(
    __name__, 
    template_folder=TEMPLATE_DIRECTORY, 
    static_folder=STATIC_DIRECTORY
)

app.secret_key = os.urandom(24)


# ----------------- USER STORAGE -----------------

USER_DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "users.json")

def load_users():
    if not os.path.exists(USER_DATA_FILE):
        os.makedirs(os.path.dirname(USER_DATA_FILE), exist_ok=True)
        with open(USER_DATA_FILE, "w") as f:
            json.dump({}, f)
    with open(USER_DATA_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)


# ----------------- LOAD MODELS -----------------

loaded_models = load_recommendation_models()


# ----------------- ROUTES -----------------

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login.html')
def login():
    return render_template('login.html')


@app.route('/signup.html')
def signup():
    return render_template('signup.html')


# ----------------- SIGNUP LOGIC -----------------

@app.route('/signup', methods=['POST'])
def signup_user():
    first_name = request.form.get("first_name", "").strip()
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    # must be SJSU email
    if not username.endswith("@sjsu.edu"):
        flash("Please use your SJSU email (@sjsu.edu).")
        return redirect(url_for('signup'))

    if not first_name or not username or not password:
        flash("All fields are required.")
        return redirect(url_for('signup'))

    users = load_users()

    # prevent duplicate
    if username in users:
        flash("An account with this email already exists.")
        return redirect(url_for('signup'))

    # save user
    users[username] = {
        "first_name": first_name,
        "password_hash": generate_password_hash(password)
    }
    save_users(users)

    flash("Account created! Please log in.")
    return redirect(url_for('login'))


# ----------------- LOGIN LOGIC -----------------

@app.route('/login', methods=['POST'])
def login_user():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    users = load_users()
    user = users.get(username)

    if not user:
        flash("No account found with that email.")
        return redirect(url_for('login'))

    if not check_password_hash(user["password_hash"], password):
        flash("Incorrect password.")
        return redirect(url_for('login'))

    # start session
    session["username"] = username
    session["first_name"] = user["first_name"]

    return redirect(url_for('form'))  # take user to form after login


# ----------------- PROTECTED FORM -----------------

@app.route("/form")
def form():
    if "username" not in session:
        flash("Please sign in first.")
        return redirect(url_for('login'))
    return render_template("form.html")


# ----------------- RECOMMENDATIONS -----------------

@app.route('/recommendation', methods=['POST'])
def get_recommendations():
    if request.method == 'POST':
        user_input = request.form.get('user_input', '').strip()

        N_CLUBS = 15
        recommended_clubs = recommend(
            user_input=user_input,
            loaded_models=loaded_models,
            n=N_CLUBS
        )

        return render_template(
            'recommendation.html',
            recommended_clubs=recommended_clubs,
            user_query=user_input
        )
    
    return redirect(url_for('home'))


# ----------------- SAVE RSOs -----------------

@app.route("/save_rso", methods=["POST"])
def save_rso():
    starred = request.form.get("selected", "[]")
    selected = json.loads(starred)
    session["saved_rso"] = selected
    return redirect(url_for("profile"))


# ----------------- PROFILE -----------------

@app.route("/profile")
def profile():
    if "username" not in session:
        flash("Please sign in first.")
        return redirect(url_for("login"))

    saved = session.get("saved_rso", [])

    return render_template(
        "profile.html",
        saved_rso=saved,
        username=session["username"],
        first_name=session.get("first_name")
    )


# ----------------- LOGOUT -----------------

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("home"))


# ----------------- MAIN -----------------

if __name__ == '__main__':
    app.run(debug=True)
