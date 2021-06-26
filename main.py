from jose import jwt

from flask import Flask, request, render_template, session, url_for, redirect, flash
from flask_login import LoginManager, login_required, login_user, current_user, logout_user, UserMixin

import constants


app = Flask(__name__)

app.secret_key = constants.FLASK_LOGIN_SECRET

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/?login=true'


class FlaskLoginUser(UserMixin):

    def __init__(self, uid):
        self.uid = uid

    def get_id(self):
        return self.uid


@login_manager.user_loader
def user_loader(uid):
    try:
        return FlaskLoginUser(uid)
    except LookupError:
        return
    return


@app.route('/', methods=["GET"])
def index():
    if current_user.is_authenticated:
        return redirect("/hidden")
    return render_template("index.html")


@app.route('/auth', methods=["GET"])
def auth():
    if current_user.is_authenticated:
        return redirect("/hidden")

    access_token = request.args.get("access_token")
    decoded = jwt.decode(access_token, constants.OUTSETA_JWT_TOKEN, algorithms=[
                         'RS256'], audience=constants.OUTSETA_URL)
    login_user(FlaskLoginUser(decoded["sub"]))
    return redirect("/hidden")


@app.route('/hidden', methods=["GET"])
@login_required
def project():
    print(current_user.uid)
    return render_template("hidden.html", access_token=current_user.uid)


@app.route('/logout', methods=["GET"])
def logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
