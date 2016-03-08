#!/usr/bin/env python
# coding=utf8
# Import flask dependencies
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import request
from config import BACKEND_URI
from app import db

admin_dashboard = Blueprint('dashboard', __name__, url_prefix=BACKEND_URI + '/dashboard')

@admin_dashboard.route('/')
def index():
    return render_template("admin/dashboard/index.html")




