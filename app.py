""" 
    enzo.galletta.xyz - Personal Website
    Copyright (C) 2020  Enzo E. Galletta

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>. 
"""

from flask import Flask, render_template, request, flash, redirect, url_for
import json
import smtplib, ssl
import os

from searchneu.api import get_course

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
    with open("academic.json",'r') as file:
        academic_obj = json.load(file)
    classes = []
    for course in academic_obj:
        course_obj = get_course(course['subj'], course['courseId'])
        classes.append(
            {
                "name": course_obj['class']['latestOccurrence']['name'],
                "code": (course['subj'] + str(course['courseId'])),
                "description": course_obj['class']['latestOccurrence']['desc']
            }
        )
    return render_template('academic.html', classes=classes)

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