from app import app
from flask import render_template, url_for, request, jsonify, redirect, session, flash
from joblib import load
import pandas as pd
import traceback
import numpy as np

import forms

model_columns = load("model_columns.pkl")
atk_model = load("fifa_atk_regressor.pkl")

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

    form = forms.OvrPredictForm()
    if form.validate_on_submit() and request.method == 'POST':
        try:
            session['output'] = outfield_predict(atk_model)
            #flash('Prediction Updated')
        except:
            print('Prediction Unsuccessful')



    output = session['output']
    return render_template('attackers.html',
                            output=output,
                            form=form)