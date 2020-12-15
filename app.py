from flask import Flask
from config import DevConfig
from joblib import load

model_columns = load("model_columns.pkl")
atk_model = load("fifa_atk_regressor.pkl")
mid_model = load("fifa_mid_regressor.pkl")
def_model = load("fifa_def_regressor.pkl")

app = Flask(__name__)
app.config.from_object(DevConfig)

from routes import *

if __name__ == '__main__':
    app.run()