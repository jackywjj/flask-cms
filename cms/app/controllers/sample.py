# coding=utf8
# Import flask dependencies
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import Markup
from flask import request
from config import POSTS_PER_PAGE
from flask.ext.paginate import Pagination
from app import db
from app.models import *

sample = Blueprint('sample', __name__, url_prefix='/sample')

@sample.route('')
def index():
	return "product index"





