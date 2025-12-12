import os
import json
from flask import Flask, render_template, request, redirect, url_for, session

from config.paths import TEMPLATE_DIRECTORY, STATIC_DIRECTORY
from Model.scripts.recommender import recommend, load_recommendation_models

app = Flask(__name__,
            template_folder=TEMPLATE_DIRECTORY, 
            static_folder=STATIC_DIRECTORY)

app.secret_key = os.urandom(24)

#load the data and models once
loaded_models = load_recommendation_models()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route("/form")
def form():
    return render_template("form.html")

#processes the form, generates recommendations, and displays the results
@app.route('/recommendation', methods=['POST'])
def get_recommendations():
    if request.method == 'POST':
        # get data
        input = request.form.get('user_input', '')
        query = input.strip()

        # call the recommend function
        N_CLUBS = 10 
        recommended_clubs = recommend(
            user_input=query, 
            loaded_models=loaded_models, 
            n=N_CLUBS
        )

        # render the results page ('recommendation.html')
        # We pass the list of clubs and the original query to the template
        return render_template(
            'recommendation.html', 
            recommended_clubs=recommended_clubs,
            user_query=query
        )
    
    # if user tried to go to /recommendations before answering form
    return redirect(url_for('home'))

# to save the starred rsos
@app.route("/save_rso", methods=["POST"])
def save_rso():
    # get the value of the form field named "selected"
    starred = request.form.get("selected", "[]")

    # parse the JSON string into a Python list of strings, holding the rso names
    selected = json.loads(starred)

    #stores the list of selected RSO names in the user's session.
    session["saved_rso"] = selected

    return redirect(url_for("profile"))

# to viewing the user's profile with saved rsos
@app.route("/profile")
def profile():
    # get the list of saved RSOs from the session.
    saved = session.get("saved_rso", [])
    
    return render_template("profile.html", saved_rso=saved)


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)