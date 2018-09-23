from flask import render_template
from app.main import main

@main.route('/pratice')
def pratice():
  return render_template('main/pratice.html')


@main.route('/scores')
def scores():
  return render_template('main/scores.html')
