#!/usr/bin/env python
# coding=utf8
# Import flask dependencies
from flask import Blueprint, render_template, flash, redirect, url_for
from flask import request
from config import BACKEND_URI
from app import db
from app.models import *
from app.forms.admin import *

admin_user = Blueprint('admin_user', __name__, url_prefix=BACKEND_URI + '/adminuser')

@admin_user.route('/')
@admin_user.route('/list')
def list():
    models = AdminUser.query.all()
    return render_template("admin/adminuser/list.html", models=models)

@admin_user.route('/create', methods=['GET', 'POST'])
def create():
    form = AdminUserForm(request.form)
    return render_template("admin/adminuser/create.html", form=form)

@admin_user.route('/<id>/update', methods=['GET', 'POST'])
def update(id):
    adminUser = AdminUser.query.get(id)
    form = AdminUserForm(request.form, adminUser)
    return render_template("admin/adminuser/update.html", form=form, adminUser=adminUser)

@admin_user.route('/<id>/delete', methods=['GET'])
def delete(id):
    user = AdminUser.query.get(id)
    if user.id == 1:
        flash(u'无法删除系统用户.')
    else:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('admin_user.list'))

@admin_user.route('/view', methods='GET')
def view():
    return render_template("admin/adminuser/view.html")
