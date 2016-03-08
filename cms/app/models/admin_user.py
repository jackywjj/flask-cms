import time
import re

from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import event

from base_model import Base

class AdminUser(Base):
	__tablename__ = 'tbl_admin_users'
	user_name    = db.Column(db.String(255),  nullable=False)
	user_pass = db.Column(db.String(255),  nullable=False)
	def __init__(self, user_name, user_pass):
		self.user_name	= user_name
		self.user_pass	= user_pass
	def __repr__(self):
		return '<User %r>' % (self.name)
	def check_password(self, userPass):
		if self.user_pass == userPass:
			return True
		else:
			return False
