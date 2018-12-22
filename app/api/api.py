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
from app.api.formats import get_formatted_summary


@api.route('/users/<int:id>')
def get_user(id):
  user = User.query.get_or_404(id)
  return jsonify(user.to_json())


@api.route('/users/<int:id>/sessions')
def get_user_sessions(id):
  user = User.query.get_or_404(id)
  page = request.args.get('page', 1, type=int)
  pagination = user.sessions.paginate(
    page, per_page=25, error_out=False
  )
  sessions = pagination.items
  next, prev = None, None
  if pagination.has_prev:
    prev = url_for('api.get_user_sessions', id=id, page=page-1)
  if pagination.has_next:
    next = url_for('api.get_user_sessions', id=id, page=page+1)
  return jsonify({
    'sessions': [session.to_json() for session in sessions],
    'prev': prev,
    'next': next,
    'count': pagination.total
  })


@api.route('/users/<int:id>/statistics')
def get_user_stats(id):
  user = User.query.get_or_404(id)
  return jsonify({
    'id': id,
    'statistics': {
      'daily': user.daily_stats.to_json(),
      'weekly': user.weekly_stats.to_json(),
      'monthly': user.monthly_stats.to_json()
    }
  })


@api.route('/users/<int:id>/statistics/daily')
def get_daily_user_stats(id):
  user = User.query.get_or_404(id)
  return jsonify({
    'id': id,
    'statistics': {
      'daily': user.daily_stats.to_json()
    }
  })


@api.route('/users/<int:id>/statistics/weekly')
def get_weekly_user_stats(id):
  user = User.query.get_or_404(id)
  return jsonify({
    'id': id,
    'statistics': {
      'weekly': user.weekly_stats.to_json()
    }
  })


@api.route('/users/<int:id>/statistics/monthly')
def get_monthly_user_stats(id):
  user = User.query.get_or_404(id)
  return jsonify({
    'id': id,
    'statistics': {
      'monthly': user.monthly_stats.to_json()
    }
  })


@api.route('/users/<int:id>/summary')
def get_user_summary(id):
  user = User.query.get_or_404(id)
  average = {
    'words': user.words_score,
    'chars': user.chars_score,
    'accuracy': user.accuracy_score,
  }
  return {
    'id': user.id,
    'username': user.username,
    'average': average,
    'statistics': {
      'daily': user.daily_stats.to_json(),
      'weekly': user.weekly_stats.to_json(),
      'monthly': user.monthly_stats.to_json()
    }
  }
