from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

from api import *

from formats import (
    get_formatted_summary,
    get_formatted_daily_stats,
    get_formatted_monthly_stats,
    get_formatted_weekly_stats,
    get_formatted_stats
)
