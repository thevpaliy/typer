import os

from app import create_app
from config import config

configuration = config[os.getenv('flavor') or 'development']
app = create_app(configuration)
