from flask import Flask
from config import DevConfig
from joblib import load

model_columns = load("model_columns.pkl")
atk_model = load("fifa_atk_regressor.pkl")

#def requestResults(overall):
 #   tweets = get_related_tweets(name)
  #  tweets['prediction'] = pipeline.predict(tweets['tweet_text'])
   # data = str(tweets.prediction.value_counts()) + '\n\n'
    #return data

app = Flask(__name__)
app.config.from_object(DevConfig)

from routes import home, attackers

if __name__ == '__main__':
    app.run()