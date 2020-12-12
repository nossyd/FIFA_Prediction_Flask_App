from app import app
from flask import render_template, url_for, request, jsonify

import forms

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/attackers', methods=['GET','POST'])
def attackers():
    form = forms.OvrPredictForm()
    if form.validate_on_submit():
        pace = request.form.get('pace', type=int)
        shoot = request.form.get('shoot', type=int)
        passing = request.form.get('passing', type=int)
        dribble = request.form.get('dribble', type=int)
        defend = request.form.get('defend', type=int)
        physic = request.form.get('physic', type=int)
        return jsonify(pace=pace, 
                       shoot=shoot, 
                       passing=passing, 
                       dribble=dribble, 
                       defend=defend,
                       physic=physic)
    return render_template('attackers.html',
                            form=form)