from app import app
from flask import render_template, url_for, request, jsonify, redirect
from joblib import load

import forms

atk_model = load("fifa_atk_regressor.joblib")

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

        # General Attributes
        pace = request.form.get('pace', type=int)
        shoot = request.form.get('shoot', type=int)
        passing = request.form.get('passing', type=int)
        dribble = request.form.get('dribble', type=int)
        defend = request.form.get('defend', type=int)
        physic = request.form.get('physic', type=int)

        # Attacking Attributes
        crossing = request.form.get('crossing', type=int)
        finishing = request.form.get('finishing', type=int)
        heading = request.form.get('heading', type=int)
        short_pass = request.form.get('short_pass', type=int)
        volleys = request.form.get('volleys', type=int)

        # Skills Attributes
        skill_dribbling = request.form.get('skill_dribbling', type=int)
        fk_accuracy = request.form.get('fk_accuracy', type=int)
        long_pass = request.form.get('long_pass', type=int)
        ball_control = request.form.get('ball_control', type=int)

        # Movement Attributes
        aggression = request.form.get('aggression', type=int)
        interceptions = request.form.get('interceptions', type=int)
        positioning = request.form.get('positioning', type=int)
        vision = request.form.get('vision', type=int)
        penalties = request.form.get('penalties', type=int)
        composure = request.form.get('composure', type=int)

        # Defending Attributes
        marking = request.form.get('marking', type=int)
        stand_tackle = request.form.get('stand_tackle', type=int)
        slide_tackle = request.form.get('slide_tackle', type=int)

        return jsonify(pace=pace, 
                       shoot=shoot, 
                       passing=passing, 
                       dribble=dribble, 
                       defend=defend,
                       physic=physic,
                       crossing=crossing,
                       finishing=finishing,
                       heading=heading,
                       short_pass=short_pass,
                       volleys=volleys,
                       skill_dribbling=skill_dribbling,
                       fk_accuracy=fk_accuracy,
                       long_pass=long_pass,
                       ball_control=ball_control,
                       aggression=aggression,
                       interceptions=interceptions,
                       positioning=positioning,
                       vision=vision,
                       penalties=penalties,
                       composure=composure,
                       marking=marking,
                       stand_tackle=stand_tackle,
                       slide_tackle=slide_tackle
                       )
    return render_template('attackers.html',
                            form=form)
    #return redirect('success',
     #                       form=form)

#@app.route('/success/<name>')
#def success(overall):
@app.route('/success')
def success():
    return 'Ok!'
    #return "<xmp>" + str(requestResults(overall)) + " </xmp> "