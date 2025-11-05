import os
import yaml

def load_config(config_file):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

def get_simulation_config():
    config_path = os.path.join(os.path.dirname(__file__), '../../config/simulation_config.yaml')
    return load_config(config_path)

def get_azure_config():
    config_path = os.path.join(os.path.dirname(__file__), '../../config/azure_config.yaml')
    return load_config(config_path)