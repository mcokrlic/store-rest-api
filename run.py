# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:06:22 2019

@author: TU376VX
"""

from app import app
from db import db

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()