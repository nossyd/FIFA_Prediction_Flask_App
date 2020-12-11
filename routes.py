from app import app
from flask import render_template, url_for

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/attackers', methods=['GET','POST'])
def attackers():
    return render_template('attackers.html')