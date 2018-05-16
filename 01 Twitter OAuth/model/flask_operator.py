from flask import Flask, render_template, session, redirect
# session dictionary will be persistent between requests
import sys
sys.path.append("..")
from controller.login import Login

login = Login()
app = Flask(__name__)
app.secret_key = "1234"

@app.route("/")
def homage():
    return render_template("home.html")

@app.route("/login/twitter")
def twitter_login():

    request_token = login.get_request_token()
    session['request_token'] = request_token

    return redirect(login.get_auth_verifier_url(request_token))


app.run(port=4995)