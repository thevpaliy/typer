from flask import jsonify
from app.api import api
from app.models import User
from app.api.formats import (
    get_formatted_summary,
    get_formatted_scores,
    get_formatted_daily_stats,
    get_formatted_monthly_stats,
    get_formatted_weekly_stats
)

@api.route('/summary/<int:id>', methods=['GET'])
def get_summary(id):
  user = User.query.get_or_404(id)
  return jsonify(get_formatted_summary(user))


@api.route('/statistics/<int:id>', methods=['GET'])
def get_statistics(id):
  return jsonify({
    'id': id,
    'statistics': get_formatted_stats(id)
  })


@api.route('/statistics/monthly/<int:id>', methods=['GET'])
def get_monthly_statistics(id):
  return jsonify({
    'id': id,
    'statistics': get_formatted_monthly_stats(id)
  })


@api.route('/statistics/weekly/<int:id>', methods=['GET'])
def get_weekly_statistics(id):
  return jsonify({
    'id': id,
    'statistics': get_formatted_weekly_stats(id)
  })


@api.route('/statistics/daily/<int:id>', methods=['GET'])
def get_daily_statistics(id):
  return jsonify({
    'id': id,
    'statistics': get_formatted_daily_stats(id)
  })
