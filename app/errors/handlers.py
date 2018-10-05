from flask import render_template, request
from app.errors import errors

@errors.app_errorhandler(403)
def _403(error):
  if request.accept_mimetypes.accept_json and \
          not request.accept_mimetypes.accept_html:
    response = jsonify({'error': 'forbidden'})
    response.status_code = 403
    return response
  return render_template('errors/403.html'), 403


@errors.app_errorhandler(404)
def _404(error):
  if request.accept_mimetypes.accept_json and \
          not request.accept_mimetypes.accept_html:
    response = jsonify({'error': 'not found'})
    response.status_code = 404
    return response
  return render_template('errors/404.html'), 404


@errors.app_errorhandler(500)
def _500(error):
  if request.accept_mimetypes.accept_json and \
          not request.accept_mimetypes.accept_html:
    response = jsonify({'error': 'internal server error'})
    response.status_code = 500
    return response
  return render_template('errors/500.html'), 500
