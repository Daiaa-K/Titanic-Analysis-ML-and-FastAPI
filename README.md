# Titanic Survival Prediction API

A machine learning API that predicts the survival probability of Titanic passengers based on their demographic and trip information. This API utilizes a neural network model trained on the historical Titanic dataset.

## Project Structure

```
TITANIC-ANALYSIS-ML-AND-FASTAPI/
├── src/
│   ├── __pycache__/
│   ├── artifacts/
│   │   ├── best_titanic_model.keras
│   │   └── preprocessor.joblib
│   └── utils/
│       ├── __pycache__/
│       ├── __init__.py
│       ├── config.py
│       ├── inference.py
│       ├── request.py
│       └── response.py
├── __init__.py
├── .env
├── .env.example
├── .gitignore
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
└── Titanic_ML_and_Analysis.ipynb
```

## Features

- RESTful API built with FastAPI
- Neural network model for classification
- Standard data preprocessing pipeline
- API key authentication
- Dockerized deployment ready
- Comprehensive input validation

## Requirements

- Python 3.8+
- FastAPI
- TensorFlow
- scikit-learn
- Joblib
- Python-dotenv

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/titanic-analysis-ml-and-fastapi.git
cd titanic-analysis-ml-and-fastapi
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file based on the `.env.example`:

```bash
cp .env.example .env
```

5. Edit the `.env` file and add your API key:

```
APP_NAME = "Titanic-Classifier"
VERSION = "1.0.0"
API_KEY = "your-secret-api-key"
```

## Usage

### Starting the API Server

Run the following command to start the API server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### API Documentation

FastAPI automatically generates interactive API documentation:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### Making Predictions

To predict survival for passengers, send a POST request to the `/predict` endpoint with passenger data:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'X-API-Key: your-secret-api-key' \
  -H 'Content-Type: application/json' \
  -d '{
  "passengers": [
    {
      "passenger_id": 1,
      "age": 25.0,
      "fare": 50.0,
      "sex": "female",
      "embarked": "S",
      "parch": 0,
      "sibsp": 1,
      "pclass": 1
    }
  ]
}'
```

### Example Response

```json
{
  "predictions": [
    {
      "passenger_id": 1,
      "prediction": "survived"
    }
  ]
}
```

## Input Data Format

The API accepts the following passenger attributes:

- `passenger_id`: Unique identifier for the passenger (integer)
- `age`: Age in years (float between 0.3 and 80.0)
- `fare`: Ticket fare (float between 0.0 and 600.0)
- `sex`: Gender ("male" or "female")
- `embarked`: Port of embarkation ("C" for Cherbourg, "Q" for Queenstown, "S" for Southampton)
- `parch`: Number of parents/children aboard (integer between 0 and 10)
- `sibsp`: Number of siblings/spouses aboard (integer between 0 and 10)
- `pclass`: Passenger class (1, 2, or 3)

The family size is automatically calculated as `sibsp + parch + 1`.

## Development

### Model Training

The machine learning model was trained using the Jupyter notebook `Titanic_ML_and_Analysis.ipynb`. This notebook contains the data analysis, preprocessing steps, and model development process.

### Adding New Features

To add new features to the model:

1. Update the `PassengerData` class in `src/utils/request.py`
2. Retrain the model with the new features
3. Update the preprocessor and model files in the `src/artifacts/` directory

## License

MIT License