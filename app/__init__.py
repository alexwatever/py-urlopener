from flask import Flask


app = Flask(__name__)

# set secret key to prevent CSRF in forms
with open('secret_key') as key:
    for line in key.readlines():
        app.secret_key = line


# application config

# sitemap
app.config['SITEMAP_GZIP'] = True

# mailer config
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
with open('mail_username') as key:
    for line in key.readlines():
        app.config["MAIL_USERNAME"] = line
with open('mail_password') as key:
    for line in key.readlines():
        app.config["MAIL_PASSWORD"] = line


from app import views
