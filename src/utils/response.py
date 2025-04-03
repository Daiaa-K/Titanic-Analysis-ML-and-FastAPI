from pydantic import BaseModel
from typing import List, Literal

class PassengerPrediction(BaseModel):
    passenger_id:int
    prediction:Literal["survived","not survived"]
    
class PredictionsResponse(BaseModel):
    predictions:List[PassengerPrediction]