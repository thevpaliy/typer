from abc import ABCMeta, abstractmethod
from six import add_metaclass
from flask import url_for

@add_metaclass(abc.ABCMeta)
class OAuthBase(object):
  _providers = None

  def __init__(self, **config):
    self.config = config


  @abstractmethod
  def authorize(self):
    """Begin the authorization process"""

  @abstractmethod
  def callback(self):
    """"""

  @property
  @classmethod
  def redirect_uri(cls):
    return url_for('oauth_redirect', provider=cls.__name__,
          next=request.args.get('next') or request.referrer or None))
