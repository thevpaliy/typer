from flask import Blueprint

practice = Blueprint('practice', __name__, url_prefix='/api')

from views import *
