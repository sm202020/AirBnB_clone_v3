#!/usr/bin/python3
"""
Created Flask app blueprint
"""
from flask import Blueprint

app_views = Blueprint('app_views',__name__,url_prefix'/apl/v1')

from api.v1.views.index import*
