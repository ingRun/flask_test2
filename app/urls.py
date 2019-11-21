from flask import request
from flask_login import login_required, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from app.models import User
from app.tools.tools import is_register


@app.route('/')
@login_required
def hello_world():
    return 'Hello World!'


@app.route('/api/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return 'ERROR'
    if request.method == 'POST':
        username = request.values.get('username')
        email = request.values.get('email')
        password = request.values.get('password')
        repassword = request.values.get('repassword')
        phone = request.values.get('phone')
        if password == repassword:
            is_reg = is_register(username=username, password=password, email=email, phone=phone)
            if is_reg.get('is'):
                password = generate_password_hash(password=password)
                user = User(username=username, password=password, email=email, phone=phone)
                db.session.add(user)
                db.session.commit()
                return 'success'
            return is_reg.get('msg')
        return '两次输入的密码不一致'


@app.route('/api/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 'ERROR'
    if request.method == 'POST':
        email = request.values.get('email')
        password = request.values.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return '登录成功'
        return '用户名或密码错误'