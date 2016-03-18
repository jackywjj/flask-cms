import time
import re

from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import event
from app.helpers.helpers import *

from .base_model import Base

class Article(Base):
    __tablename__ = 'tbl_articles'
    article_title = db.Column(db.String(255),  nullable=False)
    article_content = db.Column(db.String(255),  nullable=False)
    active = db.Column(db.Boolean(),  nullable=False)

    def __init__(self, article_title, article_content):
        self.article_title      = article_title
        self.article_content    = article_content
        self.status     = 0
