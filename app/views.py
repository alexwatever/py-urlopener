import os
from flask import render_template
from flask import request
from flask import send_from_directory
from flask_sitemap import Sitemap
from jinja2 import Environment, FileSystemLoader
from app import app


# sitemap
ext = Sitemap(app=app)
# sitemap config
app.config['SITEMAP_GZIP'] = True


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

@app.route('/contact')
def contact():
  return render_template('contact.html',
    title='Contact')

@app.route('/feedback')
def feedback():
  return render_template('feedback.html',
    title='Feedback')

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
