import json
from abc import ABCMeta, abstractmethod
from six import add_metaclass

from rauth import OAuth1Service, OAuth2Service
from flask import current_app, url_for, request, redirect, session

@add_metaclass(ABCMeta)
class OAuthBase(object):
  def __init__(self, name, config):
    self.name = name
    self.client_id = config.client_id
    self.client_secret = config.secret_id

  @abstractmethod
  def authorize(self):
    """Start the authorization process."""

  @abstractmethod
  def callback(self):
    """Returns the data needed to authorize the user."""

  @property
  def redirect_uri(self):
    return url_for('auth.oauth_callback', provider=self.name,
        next = request.args.get('next') or request.referrer or None,
        _external=True
    )

class OAuthFactory(object):
  _providers = None

  @classmethod
  def get_provider(cls, provider, config=None):
    if cls._providers is None:
      cls._providers = {}
    if provider not in cls._providers:
      if provider == 'facebook':
        cls._providers[provider] = OAuthFacebook(config)
      else:
        cls._providers[provider] = OAuthTwitter(config)
    return cls._providers[provider]

  @classmethod
  def dispose(cls):
    providers = cls._providers
    for provider in providers:
      del provider
    del cls._providers
    cls._providers = None

class OAuthFacebook(OAuthBase):
  def __init__(self, credentials):
    super(OAuthFacebook, self).__init__('facebook', credentials)
    self.service = OAuth2Service(
        name='facebook',
        client_id=self.client_id,
        client_secret=self.client_secret,
        authorize_url='https://graph.facebook.com/oauth/authorize',
        access_token_url='https://graph.facebook.com/oauth/access_token',
        base_url='https://graph.facebook.com/'
    )

  def authorize(self):
    return redirect(self.service.get_authorize_url(
        scope='email',
        response_type='code',
        redirect_uri=self.redirect_uri)
    )

  def callback(self):
    def decode_json(payload):
      return json.loads(payload.decode('utf-8'))

    if 'code' not in request.args:
      return None, None, None

    oauth_session = self.service.get_auth_session(
        data = {'code': request.args['code'],
                'grant_type': 'authorization_code',
                'redirect_uri': self.redirect_uri
        },
        decoder = decode_json
    )
    me = oauth_session.get('me?fields=id,email').json()
    return ('facebook$' + me['id'],
            me.get('email').split('@')[0],
            me.get('email')
    )


class OAuthTwitter(OAuthBase):
  def __init__(self, credentials):
    super(OAuthTwitter, self).__init__('twitter', credentials)
    self.service = OAuth1Service(
        name='twitter',
        consumer_key=self.client_id,
        consumer_secret=self.client_secret,
        request_token_url='https://api.twitter.com/oauth/request_token',
        authorize_url='https://api.twitter.com/oauth/authorize',
        access_token_url='https://api.twitter.com/oauth/access_token',
        base_url='https://api.twitter.com/1.1/'
    )

  def authorize(self):
    raise NotImplementedError

  def callback(self):
    raise NotImplementedError
