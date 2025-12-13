import os
import json
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from config.paths import TEMPLATE_DIRECTORY, STATIC_DIRECTORY, USER_DATA_PATH
from Model.scripts.recommender import recommend, load_recommendation_models

# Create Flask app
app = Flask(
    __name__, 
    template_folder=TEMPLATE_DIRECTORY, 
    static_folder=STATIC_DIRECTORY
)

# Secret key for sessions
app.secret_key = os.urandom(24)


# ----------------- USER STORAGE -----------------

# Load user data from file
def load_users():
    if not os.path.exists(USER_DATA_PATH):
        os.makedirs(os.path.dirname(USER_DATA_PATH), exist_ok=True)
        with open(USER_DATA_PATH, "w") as f:
            json.dump({}, f)
    with open(USER_DATA_PATH, "r") as f:
        return json.load(f)

# Save users back to the JSON file
def save_users(users):
    with open(USER_DATA_PATH, "w") as f:
        json.dump(users, f, indent=4)


# ----------------- LOAD MODELS -----------------

# Load the recommendation models once
loaded_models = load_recommendation_models()


# ----------------- ROUTES -----------------

# Landing page
@app.route('/')
def home():
    return render_template('home.html')

# Login page
@app.route('/login.html')
def login():
    return render_template('login.html')

# Signup page
@app.route('/signup.html')
def signup():
    return render_template('signup.html')


# ----------------- SIGNUP LOGIC -----------------

@app.route('/signup', methods=['POST'])
def signup_user():
    # Get form inputs
    first_name = request.form.get("first_name", "").strip()
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    # Only allow SJSU email
    if not username.endswith("@sjsu.edu"):
        flash("Please use your SJSU email (@sjsu.edu).")
        return redirect(url_for('signup'))

    # Check if all fields are filled
    if not first_name or not username or not password:
        flash("All fields are required.")
        return redirect(url_for('signup'))

    users = load_users()

    # Prevent duplicate account
    if username in users:
        flash("An account with this email already exists.")
        return redirect(url_for('signup'))

    # Create new user
    users[username] = {
        "first_name": first_name,
        "password_hash": generate_password_hash(password),
        "saved_rso": []     # list of saved RSOs for this user
    }
    save_users(users)

    flash("Account created! Please log in.")
    return redirect(url_for('login'))


# ----------------- LOGIN LOGIC -----------------

@app.route('/login', methods=['POST'])
def login_user():
    # Get login form data
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    users = load_users()
    user = users.get(username)

    # If email doesn't exist
    if not user:
        flash("No account found with that email.")
        return redirect(url_for('login'))

    # Wrong password
    if not check_password_hash(user["password_hash"], password):
        flash("Incorrect password.")
        return redirect(url_for('login'))

    # Store login info in session
    session["username"] = username
    session["first_name"] = user["first_name"]

    return redirect(url_for('form'))


# ----------------- PROTECTED FORM PAGE -----------------

@app.route("/form")
def form():
    # Only logged-in users can access
    if "username" not in session:
        flash("Please sign in first.")
        return redirect(url_for('login'))
    return render_template("form.html")


# ----------------- RECOMMENDATION PAGE -----------------

@app.route('/recommendation', methods=['POST'])
def get_recommendations():
    user_input = request.form.get('user_input', '').strip()

    N_CLUBS = 15
    recommended_clubs = recommend(
        user_input=user_input,
        loaded_models=loaded_models,
        n=N_CLUBS
    )

    # Load saved RSOs for this user (for auto-starring)
    users = load_users()
    saved = []
    if session.get("username"):
        saved = users[session["username"]].get("saved_rso", [])

    # Pass saved RSOs into the page
    return render_template(
        'recommendation.html',
        recommended_clubs=recommended_clubs,
        saved_rso=saved,
        user_query=user_input
    )


# ----------------- SAVE RSOs (PERSISTENT) -----------------

@app.route("/save_rso", methods=["POST"])
def save_rso():
    # Get starred RSOs from form
    starred = request.form.get("selected", "[]")
    new_selected = json.loads(starred)

    users = load_users()
    username = session.get("username")

    if not username:
        return redirect(url_for("login"))

    # Existing saved RSOs
    saved = users[username].get("saved_rso", [])

    # Merge new RSOs without duplicates
    for rso in new_selected:
        if rso not in saved:
            saved.append(rso)

    users[username]["saved_rso"] = saved
    save_users(users)

    return redirect(url_for("profile"))


# ----------------- DELETE AN RSO -----------------

@app.route("/delete_rso", methods=["POST"])
def delete_rso():
    rso_name = request.form.get("rso_name", "")

    users = load_users()
    username = session.get("username")

    saved = users[username].get("saved_rso", [])

    # Remove from saved list
    if rso_name in saved:
        saved.remove(rso_name)

    users[username]["saved_rso"] = saved
    save_users(users)

    flash(f"{rso_name} removed from your saved list.")
    return redirect(url_for("profile"))


# ----------------- PROFILE PAGE -----------------

@app.route("/profile")
def profile():
    if "username" not in session:
        flash("Please sign in first.")
        return redirect(url_for('login'))

    users = load_users()
    saved = users[session["username"]].get("saved_rso", [])

    return render_template(
        "profile.html",
        saved_rso=saved,
        username=session["username"],
        first_name=session.get("first_name")
    )


# ----------------- LOGOUT -----------------

@app.route("/logout")
def logout():
    # Clear session data and redirect
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("home"))


# ----------------- MAIN -----------------

if __name__ == '__main__':
    app.run(debug=True)
