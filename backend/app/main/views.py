import os
import re
import json
import datetime
from flask import render_template, jsonify, request, redirect, url_for, abort
from flask_login import login_required, current_user
from app import db
from app.models import Session, User
from app.main import main


@main.before_app_request
def before_request():
  if current_user.is_authenticated:
    current_user.last_seen = datetime.datetime.utcnow()
    db.session.commit()


@main.route('/')
@main.route('/index')
@main.route('/practice')
def practice():
  users = []
  for user in User.query.all():
    if user.is_online:
      users.append(user)
  return render_template('main/practice.html', users=users)


@main.route('/profile/<path:username>')
def profile(username):
  user = User.query.filter_by(username=username).first_or_404()
  return render_template('main/profile.html',
    user = user,
    statistics = {
      'daily': user.daily_stats.to_json(),
      'weekly': user.weekly_stats.to_json(),
      'monthly': user.monthly_stats.to_json()
    }
  )


@main.route('/scores')
def scores():
  users = User.query.all()
  return render_template('main/scores.html', users=users)


WORD_RE = re.compile('\w+')
# TODO: secure this
@main.route('/_words')
def words():
  # TODO: replace this
  with open(os.path.join(os.path.dirname(__file__), 'words.txt')) as f:
    words = f.read()
  words = WORD_RE.findall(words)
  return jsonify(result=words)
