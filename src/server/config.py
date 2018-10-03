import json
import os

current_dir = os.path.dirname(os.path.realpath(__file__))


def load_config(config_path):
    with open(config_path) as config_file:
        config = json.load(config_file)
        return config["clientId"], config["clientSecret"]
