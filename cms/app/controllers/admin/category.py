# coding=utf8
# Import flask dependencies
from flask import Blueprint, render_template, flash, redirect, url_for
from flask import request
from config import BACKEND_URI
from app import db
from app.models import *
from app.forms.admin import *

admin_category = Blueprint('admin_category', __name__, url_prefix=BACKEND_URI + '/category')

@admin_category.route('/')
@admin_category.route('/list')
def list():
	return render_template("admin/category/list.html")

@admin_category.route('/create', methods=['GET', 'POST'])
def create():
    form = CategoryForm(request.form)
    return render_template("admin/category/create.html", form=form)

@admin_category.route('/<id>/update', methods=['GET', 'POST'])
def update(id):
    category = Category.query.get(id)
    form = CategoryForm(request.form, category)
    return render_template("admin/category/update.html", form=form, category=category)

@admin_category.route('/<id>/delete', methods=['GET'])
def delete(id):
	category = Category.query.get(id)
	db.session.delete(category)
	db.session.commit()
	return redirect(url_for('admin_category.list'))

@admin_category.route('/view', methods='GET')
def view():
    return render_template("admin/category/view.html")
