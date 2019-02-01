# -*- coding: future_fstrings -*-
import threading
from flask_mail import Message
from flask import render_template, current_app
from app.extensions import mail


def send_reset_password(user, pin, callback_url):
  send(f'{pin} is your Typer account recovery code',
        sender = current_app.config['MAIL_USERNAME'],
        recipients = [user.email],
        html = render_template(
          'email.html',
           user=user, pin=pin, callback_url=callback_url)
        )


def send_email(app, msg):
  with app.app_context():
    mail.send(msg)


def send(subject, sender, recipients, html):
  message = Message(subject, sender=sender, recipients=recipients)
  message.html = html
  threading.Thread(
    target=send_email,
    args=(current_app._get_current_object(), message,)
  ).start()
