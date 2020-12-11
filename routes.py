from app import app
from flask import render_template, url_for, request

import forms

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/attackers', methods=['GET','POST'])
def attackers():
    form = forms.OvrPredictForm()
    if form.validate_on_submit():
        pace = request.form['pace']
        return pace
    return render_template('attackers.html',
                            form=form)