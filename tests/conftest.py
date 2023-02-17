import pytest
import yaml
import os
import json

schema_path = os.path.join("prediction_service", "schema.json")

@pytest.fixture
def config(config_path="params.yaml"):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

@pytest.fixture
def schema_in(schema_path="schema.json"):
    with open(schema_path) as json_file:
        config = json.safe_load(json_file)
    return config