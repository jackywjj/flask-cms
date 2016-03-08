#!/usr/bin/env python
# coding=utf8

class CategoryForm(Form):
    title = TextField(u'标题', [ validators.Required(message=u"标题不能为空")])
