import json
import os

current_dir = os.path.dirname(os.path.realpath(__file__))


def load_config(config_path):
    """
    Load configuration parameters from config.json file at the specified location
    :param config_path: Path to config.json file
    :type config_path: str
    :return: client_id, client_secret
    :rtype: str, str
    """

    with open(config_path) as config_file:
        config = json.load(config_file)
        return config["clientId"], config["clientSecret"]
