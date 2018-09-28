import os

from app import create_app, db
from app.models import User, Session
from config import config

configuration = config[os.getenv('flavor') or 'development']
app = create_app(configuration)

@app.shell_context_processor
def context():
  return {'db': db, 'User': User, 'Session': Session}
