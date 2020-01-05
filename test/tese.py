import os

from app.models import User


def get_user():
    user = User.query.filter_by(email='ingrun@163.com').first()
    print(user)


if __name__ == '__main__':
    get_user()
