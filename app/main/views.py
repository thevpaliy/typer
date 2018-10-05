import os
import re
import json
import datetime
from flask import render_template, jsonify, request, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Session, User
from app.main import main
from app.api import get_formatted_stats


@main.route('/')
@main.route('/index')
@main.route('/practice')
def practice():
  return render_template('main/practice.html',
    users = User.query.all()
  )


@main.route('/profile/<path:username>')
def profile(username):
  print(username)
  user = User.query.filter_by(username=username).first_or_404()
  print(get_formatted_stats(user.id))
  return render_template('main/profile.html',
    user = user,
    statistics=get_formatted_stats(user.id)
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
