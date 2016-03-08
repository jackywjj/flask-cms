#!/usr/bin/env python
# coding=utf8
# Import flask dependencies
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import Markup
from flask import request
from config import BACKEND_URI
from flask.ext.paginate import Pagination

from app import db
from app.models import *
from app.forms.admin import *

admin_login = Blueprint('admin_login', __name__, url_prefix=BACKEND_URI)

@admin_login.route('/', methods=['GET', 'POST'])
@admin_login.route('/login', methods=['GET', 'POST'])
def index():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        return redirect(url_for('dashboard.index'))
    return render_template("admin/login.html", form=form)

@admin_login.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('admin_login.index'))



