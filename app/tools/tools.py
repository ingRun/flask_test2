from app import models


# 检查用户名是否已存在
def is_username(username):
    if not len(username) >= 3:
        return False
    return not models.User.query.filter_by(username=username).first()


# 检查email是否已存在
def is_email(email):
    if not len(email) >= 6:
        return False
    return not models.User.query.filter_by(email=email).first()


def is_phone(phone):
    if len(phone) == 11:  # 手机号码 长度11位
        if phone.isdigit():  # 手机号码必须全部是数字
            return True
    return False


def is_password(password):
    if len(password) >= 8:
        if password.isalnum():
            return True
    return False


# 验证注册的用户信息是否符合规范
def is_register(username, password, email, phone):
    if not is_username(username=username):
        return {'is': False, 'msg': '该用户名已存在或不符合规范'}
    if not is_password(password=password):
        return {'is': False, 'msg': '密码长度必须要大于8位，同时使用字母和数字'}
    if not is_email(email=email):
        return {'is': False, 'msg': '该email已被使用或不符合规范'}
    if not is_phone(phone=phone):
        return {'is': False, 'msg': '请输入正确的手机号'}
    return {'is': True, 'msg': '验证通过'}
