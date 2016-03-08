import time
import re

from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import event
from app.helpers.helpers import *

from .base_model import Base

class Category(Base):
	__tablename__ = 'tbl_categories'
	category_title = db.Column(db.String(255),  nullable=False)
	active = db.Column(db.Boolean(),  nullable=False)
	def __init__(self, title):
		self.title      = title
		self.status     = 0
	def renderCount(self):
		return Post.query.filter_by(category_id=self.id, active='1').count()
