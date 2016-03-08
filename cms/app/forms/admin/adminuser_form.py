#!/usr/bin/env python
# coding=utf8
from wtforms import Form, StringField, PasswordField, validators

class AdminUserForm(Form):
    user_name = StringField(u'用户名', [ validators.required(message=u"用户名不能为空。") ])
    user_pass = PasswordField(u'密码', [ validators.required(message=u"密码不能为空。") ])
