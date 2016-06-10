from flask_wtf import Form
from wtforms import TextField, TextAreaField, SelectField, SubmitField, validators, ValidationError

class ContactForm(Form):
    name = TextField("Name", [validators.Required("Please enter your name.")])
    email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter a valid email address.")])
    subject = TextField("Subject", [validators.Required("Please enter a subject.")])
    message = TextAreaField("Message", [validators.Required("Please include a message with your email.")])
    submit = SubmitField("Send")

class FeedbackForm(Form):
    name = TextField("Name", [validators.Required("Please enter your name.")])
    email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter a valid email address.")])
    topic = SelectField("Topic", [validators.Required("Please select a topic.")], choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    message = TextAreaField("Message", [validators.Required("Please include a message with your email.")])
    submit = SubmitField("Send")
