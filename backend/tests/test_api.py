import unittest
import datetime
import utils
import random
from app.models import User, Session
from flask import jsonify, url_for
from _base import BaseTestCase


class TyperApiTestCase(BaseTestCase):
  def test_get_user(self):
    user = utils.generate_user()

    # get the user
    response = self.client.get(
      '/api/users/{id}'.format(id=user.id)
    )
    json = jsonify(user.to_json()).get_json()

    self.assertEqual(response.status_code, 200)
    self.assertEqual(json, response.json)

    # test the 404 case
    response = self.client.get('/api/users/id')
    self.assertEqual(response.status_code, 404)

  def test_get_user_sessions(self):
    user = utils.generate_user()

    # test a user with not sessions
    response = self.client.get(
      '/api/users/{id}/sessions'.format(id=user.id)
    )

    self.assertEqual(response.status_code, 200)
    self.assertTrue(len(response.json['sessions']) == 0)
    self.assertTrue(response.json['count'] == 0)
    self.assertIsNone(response.json['next'])
    self.assertIsNone(response.json['prev'])

    # test with more than 25 (default page limit)
    sessions = [utils.generate_session(user.id) for _ in range(30)]
    response = self.client.get(
      '/api/users/{id}/sessions'.format(id=user.id)
    )

    self.assertEqual(response.status_code, 200)
    self.assertEqual(25, len(response.json['sessions']))
    self.assertIsNone(response.json['prev'])
    self.assertIsNotNone(response.json['next'])
    self.assertEqual(30, response.json['count'])

    # test the next url
    response = self.client.get(response.json['next'])

    self.assertEqual(response.status_code, 200)
    self.assertEqual(5, len(response.json['sessions']))
    self.assertIsNotNone(response.json['prev'])
    self.assertIsNone(response.json['next'])
    self.assertEqual(30, response.json['count'])

    # test the 404 case
    response = self.client.get('/api/user/id/sessions')
    self.assertEqual(response.status_code, 404)

  def test_get_user_daily_sessions(self):
    user = utils.generate_user()
    sessions = utils.generate_sessions_within(user.id,
      lambda : datetime.timedelta(minutes=random.randint(0, 360)))

    response = self.client.get(
      '/api/users/{id}/statistics/daily'.format(id=user.id)
    )

    json = jsonify({
      'id': user.id,
      'statistics': {
        'daily': user.daily_stats.to_json()
      }
    }).get_json()

    self.assertEqual(response.status_code, 200)
    self.assertEqual(json, response.json)

  def test_get_user_weekly_sessions(self):
    user = utils.generate_user()
    sessions = utils.generate_sessions_within(user.id,
      lambda : datetime.timedelta(days=random.randint(0, 7)))

    response = self.client.get(
      '/api/users/{id}/statistics/weekly'.format(id=user.id)
    )

    json = jsonify({
      'id': user.id,
      'statistics': {
        'weekly': user.weekly_stats.to_json()
      }
    }).get_json()

    self.assertEqual(response.status_code, 200)
    self.assertEqual(json, response.json)

  def test_get_user_monthly_sessions(self):
    user = utils.generate_user()
    sessions = utils.generate_sessions_within(user.id,
      lambda : datetime.timedelta(days=random.randint(0, 30)))

    response = self.client.get(
      '/api/users/{id}/statistics/monthly'.format(id=user.id)
    )

    json = jsonify({
      'id': user.id,
      'statistics': {
        'monthly': user.monthly_stats.to_json()
      }
    }).get_json()

    self.assertEqual(response.status_code, 200)
    self.assertEqual(json, response.json)
