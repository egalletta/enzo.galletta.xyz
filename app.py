from flask import Flask, render_template
import json
app = Flask(__name__)

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

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/3d')
def contact():
    return render_template('3d.html')