from flask import Blueprint

practice = Blueprint('practice', __name__)

from .views import *
