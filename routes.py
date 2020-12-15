from app import app
from flask import render_template, url_for, request, jsonify, redirect, session, flash
from joblib import load
import pandas as pd
import numpy as np

import forms

model_columns = load("model_columns.pkl")
atk_model = load("fifa_atk_regressor.pkl")
mid_model = load("fifa_mid_regressor.pkl")
def_model = load("fifa_def_regressor.pkl")

def outfield_predict(model):

    cols = ['pace', 'shoot', 'passing', 'dribble', 'defend', 'physic', 
            'crossing', 'finishing', 'heading', 'short_pass', 'volleys', 
            'skill_dribbling', 'curve', 'fk_accuracy', 'long_pass', 'ball_control',
            'acceleration', 'sprint_speed', 'agility', 'reactions', 'balance', 
            'shot_power', 'jumping', 'stamina', 'strength', 'long_shots', 
            'aggression', 'interceptions', 'positioning', 'vision', 'penalties', 'composure', 
            'marking', 'stand_tackle', 'slide_tackle']

    data = [request.form.get('{}'.format(x) , type=int) for x in cols]

    prediction = model.predict([np.array(list(data))])

    output = prediction[0]

    return output


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/attackers', methods=['GET','POST'])

def attackers():
    try:
        form = forms.OvrPredictForm()
        if form.validate_on_submit() and request.method == 'POST':
            try:
                session['atk_output'] = outfield_predict(atk_model)
                #flash('Prediction Updated')
            except:
                print('Prediction Unsuccessful')
        atk_output = session['atk_output']
        return render_template('attackers.html',
                                atk_output=atk_output,
                                form=form)
    except:
        form = forms.OvrPredictForm()
        atk_output = 0
        return render_template('attackers.html',
                                atk_output=atk_output,
                                form=form)
            


@app.route('/midfielders', methods=['GET','POST'])
def midfielders():

    try:
        form = forms.OvrPredictForm()
        if form.validate_on_submit() and request.method == 'POST':
            try:
                session['mid_output'] = outfield_predict(mid_model)
                #flash('Prediction Updated')
            except:
                print('Prediction Unsuccessful')
        mid_output = session['mid_output']
        return render_template('midfielders.html',
                                mid_output=mid_output,
                                form=form)
    except:
        form = forms.OvrPredictForm()
        mid_output = 0
        return render_template('midfielders.html',
                                mid_output=mid_output,
                                form=form)


@app.route('/defenders', methods=['GET','POST'])
def defenders():

    try:
        form = forms.OvrPredictForm()
        if form.validate_on_submit() and request.method == 'POST':
            try:
                session['def_output'] = outfield_predict(def_model)
                #flash('Prediction Updated')
            except:
                print('Prediction Unsuccessful')
        def_output = session['def_output']
        return render_template('defenders.html',
                                def_output=def_output,
                                form=form)
    except:
        form = forms.OvrPredictForm()
        def_output = 0
        return render_template('defenders.html',
                                def_output=def_output,
                                form=form)