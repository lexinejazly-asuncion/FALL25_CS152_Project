from flask import Flask, render_template

from config.paths import TEMPLATE_DIRECTORY, STATIC_DIRECTORY

app = Flask(__name__,
            template_folder=TEMPLATE_DIRECTORY, 
            static_folder=STATIC_DIRECTORY)

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
@app.route("/explore")
def explore():
    return render_template("explore.html")
@app.route("/recommendation/")
@app.route("/recommendation")
def recommendation():
    return render_template("recommendation.html")
@app.route("/profile")
def profile():
    return render_template("profile.html")


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)