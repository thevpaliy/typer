from flask import render_template
from app.errors import errors

@errors.app_errorhandler(404)
def _404(error):
  return render_template('errors/404.html')


@errors.app_errorhandler(500)
def _500(error):
  return render_template('errors/500.html')
