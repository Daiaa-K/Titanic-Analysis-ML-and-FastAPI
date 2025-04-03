from src.utils.request import PassengerData
from src.utils.response import PassengerPrediction,PredictionsResponse
from src.utils.config import preprocessor,classifier
from typing import List
import pandas as pd

def predict_survival(passengers:List[PassengerData])->PredictionsResponse:
    """ predict survival for a list of passengers"""
    # Convert PassengerData objects to DataFrame
    df = pd.DataFrame([p.model_dump() for p in passengers])
    df_processed = preprocessor.transform(df)
    predictions = (classifier.predict(df_processed) > 0.5).astype("int32")
    
    # create response
    pred_response = PredictionsResponse(predictions=[
        PassengerPrediction(
            passenger_id = passenger.passenger_id,
            prediction= "survived" if pred == 1 else "not survived"
        )
        for passenger,pred in zip(passengers,predictions.flatten())
        
    ])
    return pred_response