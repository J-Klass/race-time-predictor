import os

from dotenv import load_dotenv


def load_config(is_dev, project_dir):
    """
    Load configuration parameters specified in .env file
    :return: client_id, client_secret
    :rtype: str, str
    """

    config_name = ".env"
    if is_dev and os.path.isfile(project_dir + "/.env.development"):
        config_name = project_dir + "/.env.development"
    elif not is_dev and os.path.isfile(project_dir + "/.env.production"):
        config_name = project_dir + "/.env.production"

    # Load variables from .env file as system env variables
    load_dotenv(config_name)

    client_id = os.getenv("VUE_APP_CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    return client_id, client_secret
