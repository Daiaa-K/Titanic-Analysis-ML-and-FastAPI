from dotenv import load_dotenv
import os
import joblib
from tensorflow.keras.models import load_model

load_dotenv()

#Load env variables

APP_NAME = os.getenv("APP_NAME")
VERSION = os.getenv("VERSION")
API_SECRET_KEY = os.getenv("API_KEY")

# load models

SRC_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

preprocessor = joblib.load(os.path.join(SRC_PATH, "artifacts", "preprocessor.joblib"))
classifier = load_model(os.path.join(SRC_PATH, "artifacts", "best_titanic_model.keras"))