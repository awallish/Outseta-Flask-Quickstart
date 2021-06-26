from jose import jwt

from flask import Flask, request, render_template, redirect
from flask_login import login_required, login_user, current_user, logout_user

import constants
from authentication import login_manager, FlaskLoginUser


app = Flask(__name__)

app.secret_key = constants.FLASK_LOGIN_SECRET

login_manager.init_app(app)


@app.route('/', methods=["GET"])
def index():
    print(request.cookies)
    if current_user.is_authenticated:
        return redirect("/hidden")
    return render_template("index.html")


@app.route('/auth', methods=["GET"])
def auth():
    print(request.cookies)
    if current_user.is_authenticated:
        return redirect("/hidden")

    access_token = request.args.get("access_token")
    if not access_token:
        return redirect("/")

    try:
        jwt.decode(access_token, constants.OUTSETA_JWT_TOKEN, algorithms=[
            'RS256'], audience=constants.OUTSETA_URL)
        login_user(FlaskLoginUser(access_token))
        return redirect("/hidden")
    except:
        # jwt.decode throws an attribute error if the access token is invalid
        return redirect("/")


@app.route('/hidden', methods=["GET"])
@login_required
def project():
    return render_template("hidden.html", access_token=current_user.access_token)


@app.route('/logout', methods=["GET"])
def logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
