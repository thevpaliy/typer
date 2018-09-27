from flask_mail import Message
from flask import render_template
from app import mail

def send_reset_password(user, token):
  send('Typer Reset Your Password',
        sender = "vpaliy97@gmail.com",
        recipients = [user.email],
        html = render_template(
          'email/reset_password.html',
           user=user, token=token)
        )


def send(subject, sender, recipients, html):
  message = Message(subject, sender=sender, recipients=recipients)
  message.html = html
  mail.send(message)
