from flask import Flask, render_template, session, redirect, request, url_for,g
# session dictionary will be persistent between requests
import sys
sys.path.append("..")
from controller.login import Login
from model.user import User


def initiate_flask_operator():

    login = Login()
    app = Flask(__name__)
    app.secret_key = "1234"

    @app.before_request
    def load_user():
        # Check if there is key called 'screen_name'
        if 'screen_name' in session:
            g.user = User.load_from_db_by_screen_name(session['screen_name'])

    @app.route("/")
    def homage():
        return render_template("home.html")

    @app.route("/login/twitter")
    def twitter_login():

        request_token = login.get_request_token()
        session['request_token'] = request_token

        return redirect(login.get_auth_verifier_url(request_token))

    @app.route("/auth/twitter")
    def twitter_auth():
        authentication_verifier = request.args.get("oauth_verifier")

        # Retrieve the value of request token from the session.
        access_token = login.get_access_token(session["request_token"], authentication_verifier)

        user = User.load_from_db_by_screen_name(access_token['screen_name'])
        if not user:
            user = User(None, access_token['screen_name'], access_token['oauth_token'],
                        access_token['oauth_token_secret'])

        session['screen_name'] = user.get_screen_name()

        return redirect(url_for("profile"))

    @app.route("/profile")
    def profile():
        return render_template("profile.html", user=g.user)

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(url_for("homepage"))

    # Callback URL in application settings would then be: http://127.0.0.1:4995/auth/twitter
    app.run(port=4995)