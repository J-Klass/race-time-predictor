import os

from dotenv import load_dotenv


def load_config():
    """
    Load configuration parameters specified in .env file
    :return: client_id, client_secret
    :rtype: str, str
    """

    # Load variables from .env file as system env variables
    load_dotenv()

    client_id = os.getenv("VUE_APP_CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    return client_id, client_secret
