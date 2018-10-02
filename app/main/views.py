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
@main.route('/practice')
def practice():
  return render_template('main/practice.html')


@main.route('/profile/<path:username>')
def profile(username):
  user = User.query.filter_by(username=username).first_or_404()
  return render_template('main/profile.html',
    words = user.words_score,
    chars = user.chars_score,
    accuracy = user.accuracy_score,
    count = user.sessions_taken,
    statistics=get_formatted_stats(user.id)
  )


WORD_RE = re.compile('\w+')
# TODO: secure this
@main.route('/_words')
def words():
  # TODO: replace this
  with open(os.path.join(os.path.dirname(__file__), 'words.txt')) as f:
    words = f.read()
  words = WORD_RE.findall(words)
  return jsonify(result=words)
