from flask import Flask, render_template, request, flash, redirect, url_for
import json
import smtplib, ssl
import os
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET')

# Constants
SERVER_EMAIL = os.environ.get('SERVER_EMAIL')
EMAIL_PW = os.environ.get('EMAIL_PW')
ENZO_EMAIL = os.environ.get('ENZO_EMAIL')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/experience')
def experience():
    with open("jobs.json",'r') as file:
        jobs_obj = json.load(file)
    return render_template('experience.html', jobs=jobs_obj)

@app.route('/projects')
def projects():
    with open("projects.json",'r') as file:
        projs_obj = json.load(file)
    return render_template('projects.html', projects=projs_obj)

@app.route('/academic')
def academic():
    return render_template('academic.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email_name = request.form['name']
        email_from = request.form['email']
        email_subj = request.form['subject']
        email_body = """\
        Subject: {}
        From: {}
        Author: {}

        {}""".format(email_subj, email_from, email_name, request.form['content'])
        send_email(email_from, email_subj, email_body)
        flash('Message Sent Sucessfully')
        return redirect(url_for('contact'))
    else:
        return render_template('contact.html')


def send_email(email_from: str, email_subject: str, email_body: str):
    port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(SERVER_EMAIL, EMAIL_PW)
        server.sendmail(email_from, ENZO_EMAIL, email_body)

@app.route('/3d')
def three_d():
    return render_template('3d.html')