import threading
from flask_mail import Message
from flask import render_template, current_app
from app.extensions import mail


def send_reset_password(user, token):
  send('Typer Reset Your Password',
        sender = current_app.config['MAIL_USERNAME'],
        recipients = [user.email],
        html = render_template(
          'email/reset_password.html',
           user=user, token=token)
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
