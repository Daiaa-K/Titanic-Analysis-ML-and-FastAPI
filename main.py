from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from src.utils.inference import predict_survival
from src.utils.request import PassengerData
from src.utils.response import PredictionsResponse
from src.utils.config import API_SECRET_KEY,APP_NAME,VERSION
from typing import List

# Initialize FastAPI app
app = FastAPI(title=APP_NAME,version=VERSION)

# MiddleWare for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=True)
async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key!=API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

# Define the check endpoint
@app.get("/",tags=["health"],description="Health check endpoint")
async def health_check(api_key:str= Depends(verify_api_key)):
    """Health check endpoint"""
    return {"status": "up & running"}

# Define the predict endpoint
@app.post("/predict", response_model= PredictionsResponse , tags= ["predict"],description="Predict survival for a list of passengers")    
async def predict_passengers(passengers: List[PassengerData], api_key:str = Depends(verify_api_key)):
    try:
        """Predict survival for a list of passengers"""
        response = predict_survival(passengers)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
