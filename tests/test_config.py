import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service

input_data = {
    "incorrect_range":
    {"fixed acidity": 7897897,
    "volatile acidity": 555,
    "citric acid": 99,
    "residual sugar": 99,
    "chlorides": 12,
    "free sulfur dioxide": 789,
    "total sulfur dioxide": 75,
    "density": 2,
    "pH": 33,
    "sulphates": 9,
    "alcohol": 9
    },

    "correct_range":
    {"fixed acidity": 5,
    "volatile acidity": 1,
    "citric acid": 0.5,
    "residual sugar": 10,
    "chlorides": 0.5,
    "free sulfur dioxide": 3,
    "total sulfur dioxide": 75,
    "density": 1,
    "pH": 3,
    "sulphates": 1,
    "alcohol": 9
    },

    "incorrect_col":
    {"fixed acidity": 5,
    "volatile acidity": 1,
    "citric acid": 0.5,
    "residual sugar": 10,
    "chlorides": 0.5,
    "free sulfur dioxide": 3,
    "total_sulfur dioxide": 75,
    "density": 1,
    "pH": 3,
    "sulphates": 1,
    "alcohol": 9
    }
}

TARGET_range = {
    "min": 3.0,
    "max": 8.0
}

def test_form_response_correct_range(data=input_data["correct_range"]):
    res = form_response(data)
    assert TARGET_range["min"] <= res <= TARGET_range["max"]

def test_api_response_correct_range(data=input_data["correct_range"]):
    res = api_response(data)["response"]
    assert TARGET_range["min"] <= res <= TARGET_range["max"]

def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)

def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)


def test_form_response_incorrect_col(data=input_data["incorrect_col"]):
    with pytest.raises(prediction_service.prediction.NotInCols):
        res = form_response(data)

def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    with pytest.raises(prediction_service.prediction.NotInCols):
        res = form_response(data)



