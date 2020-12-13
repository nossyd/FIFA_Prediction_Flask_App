from app import app
from flask import render_template, url_for, request, jsonify, redirect
from joblib import load
import pandas as pd
import traceback
import numpy as np

import forms

model_columns = load("model_columns.pkl")
atk_model = load("fifa_atk_regressor.pkl")

#def get_attributes():
#    attributes_list = []
#    try:
#        attributes_list.append({})


#def requestResults(overall):
#    predict['prediction'] = atk_model.predict(tweets['tweet_text'])
#    return data + str(overall)
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/attackers', methods=['GET','POST'])
def attackers():

    form = forms.OvrPredictForm()
    if form.validate_on_submit():

        
        #General Attributes
        pace = request.form.get('pace', type=int)
        shoot = request.form.get('shoot', type=int)
        passing = request.form.get('passing', type=int)
        dribble = request.form.get('dribble', type=int)
        defend = request.form.get('defend', type=int)
        physic = request.form.get('physic', type=int)

        #Attacking Attributes
        crossing = request.form.get('crossing', type=int)
        finishing = request.form.get('finishing', type=int)
        heading = request.form.get('heading', type=int)
        short_pass = request.form.get('short_pass', type=int)
        volleys = request.form.get('volleys', type=int)

        #Skills Attributes
        skill_dribbling = request.form.get('skill_dribbling', type=int)
        curve = request.form.get('curve', type=int)
        fk_accuracy = request.form.get('fk_accuracy', type=int)
        long_pass = request.form.get('long_pass', type=int)
        ball_control = request.form.get('ball_control', type=int)

        #Movement Attributes
        acceleration = request.form.get('acceleration', type=int)
        sprint_speed = request.form.get('sprint_speed', type=int)
        agility = request.form.get('agility', type=int)
        reactions = request.form.get('reactions', type=int)
        balance = request.form.get('balance', type=int)

        #Power Attributes
        shot_power = request.form.get('shot_power', type=int)
        jumping = request.form.get('jumping', type=int)
        stamina = request.form.get('stamina', type=int)
        strength = request.form.get('strength', type=int)
        long_shots = request.form.get('long_shots', type=int)

        #Mentality Attributes
        aggression = request.form.get('aggression', type=int)
        interceptions = request.form.get('interceptions', type=int)
        positioning = request.form.get('positioning', type=int)
        vision = request.form.get('vision', type=int)
        penalties = request.form.get('penalties', type=int)
        composure = request.form.get('composure', type=int)

        #Defending Attributes
        marking = request.form.get('marking', type=int)
        stand_tackle = request.form.get('stand_tackle', type=int)
        slide_tackle = request.form.get('slide_tackle', type=int)

        data = [pace, shoot, passing, dribble, defend, physic, 
                crossing, finishing, heading, short_pass, volleys, 
                skill_dribbling, curve, fk_accuracy, long_pass, ball_control,
                acceleration, sprint_speed, agility, reactions, balance, 
                shot_power, jumping, stamina, strength, long_shots, 
                aggression, interceptions, positioning, vision, penalties, composure, 
                marking, stand_tackle, slide_tackle]

        prediction = atk_model.predict([np.array(list(data))])

        output = prediction[0]
        return render_template('attackers.html', prediction_text='Overall rating should be {}'.format(output), form=form)

    #if request.method == 'POST':
        # try converting json dict to list
        # try inserting list to model
        # get prediction
        # return page with prediction

       



        # return jsonify(pace=pace, 
        #                shoot=shoot, 
        #                passing=passing, 
        #                dribble=dribble, 
        #                defend=defend,
        #                physic=physic,
        #                crossing=crossing,
        #                finishing=finishing,
        #                heading=heading,
        #                short_pass=short_pass,
        #                volleys=volleys,
        #                skill_dribbling=skill_dribbling,
        #                fk_accuracy=fk_accuracy,
        #                long_pass=long_pass,
        #                ball_control=ball_control,
        #                aggression=aggression,
        #                interceptions=interceptions,
        #                positioning=positioning,
        #                vision=vision,
        #                penalties=penalties,
        #                composure=composure,
        #                marking=marking,
        #                stand_tackle=stand_tackle,
        #                slide_tackle=slide_tackle
        #                )
    return render_template('attackers.html',
                            form=form)
    #return redirect(url_for('predict',
     #                       form=form))



# @app.route('/attackers_predict',methods=['GET','POST'])
# def attackers_predict():

#     int_features = [int(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = atk_model.predict(final_features)

#     output = round(prediction[0], 2)

#     return render_template('attackers.html', prediction_text='Attackers overall be {}'.format(output))


# @app.route('/attackers_results',methods=['POST'])
# def attackers_results():

#     data = request.get_json(force=True)
#     prediction = atk_model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)



