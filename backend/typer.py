import os
import click

from app import create_app, db
from app.users.models import User, Statistics
from app.practice.models import Session
from app.users.serializers import (UserSchema,
    ScoresSchema, StatisticSchema)
from app.practice.serializers import SessionSchema
from config import config


configuration = config[os.getenv('flavor') or 'development']
app = create_app(configuration)


@app.shell_context_processor
def context():
  return {
    'db': db,
    'User': User,
    'Session': Session,
    'Statistics': Statistics,
    'UserSchema': UserSchema,
    'ScoreSchema': ScoresSchema,
    'StatisticSchema': StatisticSchema,
    'SessionSchema': SessionSchema
  }


@app.cli.command()
def test():
  click.echo('Running tests...')
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)
