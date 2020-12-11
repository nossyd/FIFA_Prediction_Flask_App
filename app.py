from flask import Flask
from config import DevConfig
from joblib import load

atk_model = load("fifa_atk_regressor.joblib")

app = Flask(__name__)
app.config.from_object(DevConfig)

from routes import home, attackers

if __name__ == '__main__':
    app.run()