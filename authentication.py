import time

from jose import jwt

from flask_login import LoginManager, UserMixin

import constants


login_manager = LoginManager()
login_manager.login_view = '/?login=true'


class FlaskLoginUser(UserMixin):

    def __init__(self, access_token):
        self.access_token = access_token

        self.data = jwt.decode(access_token, constants.OUTSETA_JWT_TOKEN, algorithms=[
            'RS256'], audience=constants.OUTSETA_URL)

    def get_id(self):
        return self.access_token

    @property
    def is_authenticated(self):
        return time.time() < self.data["exp"]


@login_manager.user_loader
def user_loader(access_token):
    try:
        return FlaskLoginUser(access_token)
    except LookupError:
        return
