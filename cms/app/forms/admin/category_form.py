#!/usr/bin/env python
# coding=utf8

from wtforms import Form, StringField, PasswordField, validators

class CategoryForm(Form):
    title = StringField(u'标题', [ validators.required(message=u"标题不能为空")])
