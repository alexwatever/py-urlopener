import os
from flask import render_template, request, send_from_directory, flash
from forms import ContactForm, FeedbackForm
from flask_mail import Mail, Message
from flask_sitemap import Sitemap
from jinja2 import Environment, FileSystemLoader
from app import app


# setup mailer
mail = Mail()
mail.init_app(app)

# setup sitemap
ext = Sitemap(app=app)


# routes
@app.route('/')
def index():
  return render_template('index.html',
    title='Home')

@app.route('/about')
def about():
  lastmod = '11/10/85'
  return render_template('about.html',
    title='About',
    priority='1')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  # set form
  form = ContactForm()
  # check request type
  if request.method == 'POST':
    # if post then validate submission
    if form.validate() == False:
      # if form doesn't validate and flash error
      for message in form.name.errors:
        flash(message)
      for message in form.email.errors:
        flash(message)
      for message in form.subject.errors:
        flash(message)
      for message in form.message.errors:
        flash(message)
      return render_template('contact.html',
        title='Contact',
        form=form)
    else:
      # if form does validate submit form and send email
      msg = Message(form.subject.data, sender=form.email.data, recipients=[app.config["MAIL_USERNAME"]])
      msg.body = """
      From: %s <%s>
      Subject: %s
      Message: %s
      """ % (form.name.data, form.email.data, form.subject.data, form.message.data)
      mail.send(msg)
      # return page and flash success
      flash('Thank you for the message. I\'ll get back to you shortly.')
      return render_template('contact.html',
        title='Contact',
        form=form)
  elif request.method == 'GET':
    # if get then return page
    return render_template('contact.html',
      title='Contact',
      form=form)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
  # set form
  form = FeedbackForm()
  # check request type
  if request.method == 'POST':
    # if post then validate submission
    if form.validate() == False:
      # if form doesn't validate and flash error
      for message in form.name.errors:
        flash(message)
      for message in form.email.errors:
        flash(message)
      for message in form.topic.errors:
        flash(message)
      for message in form.message.errors:
        flash(message)
      return render_template('feedback.html',
        title='Feedback',
        form=form)
    else:
      # if form does validate submit form and send email
      msg = Message(form.topic.data, sender=form.email.data, recipients=[app.config["MAIL_USERNAME"]])
      msg.body = """
      From: %s <%s>
      Subject: %s
      Message: %s
      """ % (form.name.data, form.email.data, form.topic.data, form.message.data)
      mail.send(msg)
      # return page and flash success
      flash('Thank you for the message. I\'ll get back to you shortly.')
      return render_template('feedback.html',
        title='Feedback',
        form=form)
  elif request.method == 'GET':
    # if get then return page
    return render_template('feedback.html',
      title='Feedback',
      form=form)

@app.route('/privacy')
def privacy():
  return render_template('privacy',
    title='Privacy')

@app.route('/robots.txt')
def static_from_root():
  return send_from_directory(app.static_folder, request.path[1:])


# sitemap pages
@ext.register_generator
def index():
  lastmod = '2016-06-09'
  changefreq = 'daily'
  priority = '1.0'
  yield 'index', {}, lastmod, changefreq, priority

@ext.register_generator
def about():
  lastmod = '2016-06-09'
  changefreq = 'weekly'
  priority = '0.8'
  yield 'about', {}, lastmod, changefreq, priority

@ext.register_generator
def contact():
  lastmod = '2016-06-09'
  changefreq = 'weekly'
  priority = '0.5'
  yield 'contact', {}, lastmod, changefreq, priority

@ext.register_generator
def feedback():
  lastmod = '2016-06-09'
  changefreq = 'weekly'
  priority = '0.5'
  yield 'feedback', {}, lastmod, changefreq, priority

@ext.register_generator
def privacy():
  lastmod = '2016-06-09'
  changefreq = 'weekly'
  priority = '0.7'
  yield 'privacy', {}, lastmod, changefreq, priority

@ext.register_generator
def static_from_root():
  lastmod = '2016-06-09'
  changefreq = 'yearly'
  priority = '0.1'
  yield 'static_from_root', {}, lastmod, changefreq, priority
