#!/usr/bin/env python
# coding=utf8
from wtforms import Form, StringField, PasswordField, validators
from app.helpers import Unique
from app.models import AdminUser

class AdminUserForm(Form):
    user_name = StringField(u'用户名', [ validators.required(message=u"用户名不能为空。"), \
        Unique(AdminUser, AdminUser.user_name, message=u"相同的用户名已经存在。") ])
    user_pass = PasswordField(u'密码', [ validators.required(message=u"密码不能为空。") ])
