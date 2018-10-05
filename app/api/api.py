import datetime
from app.api import api
from app.models import User, Session
from app import db
from flask import (
    jsonify,
    request,
    make_response,
    url_for
)
from app.api.formats import (
    get_formatted_summary,
    get_formatted_daily_stats,
    get_formatted_monthly_stats,
    get_formatted_weekly_stats
)

@api.route('/users/<int:id>')
def get_user(id):
  user = User.query.get_or_404(id)
  return jsonify(user.to_json())


@api.route('/users/<int:id>/sessions')
def get_user_sessions(id):
  user = User.query.get_or_404(id)
  page = request.args.get('page', 1, type=int)
  pagination = users.sessions.paginate(
    page, per_page=25, error_out=False
  )
  sessions = pagination.items
  next, prev = None, None
  if pagination.has_prev:
    prev = url_for('api.get_user_sessions', id=id, page=page-1)
  if pagination.has_next:
    next = url_for('api.get_user_sessions', id=id, page=page+1)
  return jsonify(
    'sessions': [session.to_json() for session in sessions],
    'prev': prev,
    'next': next,
    'count': pagination.total
  )


@api.route('/users/<int:id>/statistics')
def get_user_statistics(id):
  return jsonify({
    'id': id,
    'statistics': get_formatted_stats(id)
  })


@api.route('/users/<int:id>/summary')
def get_user_summary(id):
  user = User.query.get_or_404(id)
  return jsonify(get_formatted_summary(user))


@api.route('/users/<int:id>/statistics/monthly')
def get_monthly_statistics(id):
  return jsonify({
    'id': id,
    'statistics': get_formatted_monthly_stats(id)
  })


@api.route('/users/<int:id>/statistics/weekly')
def get_weekly_statistics(id):
  return jsonify({
    'id': id,
    'statistics': get_formatted_weekly_stats(id)
  })


@api.route('/users/<int:id>/statistics/daily')
def get_daily_statistics(id):
  return jsonify({
    'id': id,
    'statistics': get_formatted_daily_stats(id)
  })


@api.route('/users/<int:id>/session', methods=['POST'])
def save_user_session(id):
  user = User.query.get_or_404(id)
  data = request.get_json() or {}
  session = Session(user_id=id, created_date = datetime.datetime.now())
  session.accuracy = data['accuracy']
  session.words = data['correct']
  session.chars = data['chars']
  db.session.add(session)
  db.session.commit()
  return 'Success', 201
