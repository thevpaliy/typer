from flask import jsonify
from app.api import api

def bad_request(message):
  response = jsonify({'error': 'bad request', 'message': message})
  response.status_code = 400
  return response


def unauthorized(message):
  response = jsonify({'error': 'unauthorized', 'message': message})
  response.status_code = 401
  return response


def fobidden(message):
  response = jsonify({'error': 'forbidden', 'message': message})
  response.status_code = 403
  return response
