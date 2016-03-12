#!/usr/bin/env python
# coding=utf8
# Import flask dependencies
from flask import Blueprint, render_template, flash, redirect, url_for
from flask import request
from config import BACKEND_URI
from app import db
from app.models import *
from app.forms.admin import *
import hashlib

admin_user = Blueprint('admin_user', __name__, url_prefix=BACKEND_URI + '/adminuser')

@admin_user.route('/')
@admin_user.route('/list')
def list():
    models = AdminUser.query.all()
    return render_template("admin/adminuser/list.html", models=models)

@admin_user.route('/create', methods=['GET', 'POST'])
def create():
    form = AdminUserForm(request.form)
    if request.method == "POST" and form.validate():
        user_pass = hashlib.md5(form.user_pass.data.encode('utf-8')).hexdigest()
        adminUser = AdminUser(form.user_name.data, user_pass)
        db.session.add(adminUser)
        db.session.commit()
        return redirect(url_for('admin_user.list'))
    return render_template("admin/adminuser/create.html", form=form)

@admin_user.route('/<id>/update', methods=['GET', 'POST'])
def update(id):
    adminUser = AdminUser.query.get(id)
    form = AdminUserForm(request.form, adminUser)
    if request.method == "POST" and form.validate():
        user_pass = hashlib.md5(form.user_pass.data.encode('utf-8')).hexdigest()
        adminUser.user_name = form.user_name.data
        adminUser.user_pass = user_pass
        db.session.commit()
        return redirect(url_for('admin_user.list'))
    return render_template("admin/adminuser/update.html", form=form, adminUser=adminUser)

@admin_user.route('/<id>/delete', methods=['GET'])
def delete(id):
    adminUser = AdminUser.query.get(id)
    if adminUser.id == 1:
        flash(u'无法删除系统用户.')
    else:
        db.session.delete(adminUser)
        db.session.commit()
    return redirect(url_for('admin_user.list'))

@admin_user.route('/view', methods='GET')
def view():
    return render_template("admin/adminuser/view.html")
