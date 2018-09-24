import os
import re

from flask import render_template, jsonify, request, redirect, url_for
from flask_login import login_required

from app.main import main

WORD_RE = re.compile('\w+')

@main.route('/practice')
def practice():
  return render_template('main/practice.html')


@main.route('/_words')
@login_required
def words():
  with open(os.path.join(os.path.dirname(__file__), 'words.txt')) as f:
    words = f.read()
  words = WORD_RE.findall(words)
  return jsonify(result=words)


@main.route('/save', methods=('POST',))
@login_required
def save():
  # TODO: save session
  return redirect(url_for('main.practice'))


@main.route('/scores')
@login_required
def scores():
  return render_template('main/scores.html')
