import os

from flask import Flask, request, send_from_directory

from server.auth import get_access_credentials
from server.config import load_config
from server.queries import fetch_activities, fetch_profile
from server.responses import success, error

app = Flask(__name__)

# Detect development/production environment from env variable
is_dev = "FLASK_ENV" in os.environ and os.environ["FLASK_ENV"] == "development"

# Directories
src_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(src_dir)
static_dir = os.path.join(project_dir, "dist")

# Configuration
client_id, client_secret = load_config()


@app.route("/profile", methods=["GET"])
def get_profile():
    """
    Fetch athlete profile and total stats from Strava, extract relevant information, and send it
    back to the client
    Request must contain OAuth 2 code as query param
    :return: profile
    :rtype: JSON object
    """

    # Fetch access token using code
    code = request.args.get("code")
    try:
        access_token, athlete_id = get_access_credentials(client_id, client_secret, code)
    except ValueError as e:
        return error(e)

    # Fetch athlete profile and stats
    try:
        profile = fetch_profile(access_token, athlete_id)
    except ValueError as e:
        return error(e)

    return success(profile)


@app.route("/predictions", methods=["GET"])
def get_predictions():
    """
    Fetch athlete activities from Strava, run machine-learning algorithm to obtain predictions, and
    return relevant results to the client
    Request must contain OAuth 2 code as query param
    :return: predictions
    :rtype: JSON object
    """

    # Fetch access token using code
    code = request.args.get("code")
    try:
        access_token, athlete_id = get_access_credentials(client_id, client_secret, code)
    except ValueError as e:
        return error(e)

    # Fetch athlete's activities
    try:
        activities = fetch_activities(access_token)
    except ValueError as e:
        return error(e)

    print(activities)

    # TODO calculate and return predictions
    predictions = {}

    return success(predictions)


# Serve static files in development mode (handled by nginx in production)
if is_dev:

    @app.route("/css/<path:path>", methods=["GET"])
    def get_css(path):
        return send_from_directory(os.path.join(static_dir, "css"), path)

    @app.route("/img/<path:path>", methods=["GET"])
    def get_img(path):
        return send_from_directory(os.path.join(static_dir, "img"), path)

    @app.route("/js/<path:path>", methods=["GET"])
    def get_js(path):
        return send_from_directory(os.path.join(static_dir, "js"), path)

    @app.route("/", methods=["GET"], defaults={"path": ""})
    @app.route("/<path:path>", methods=["GET"])
    def catch_all(path):
        return send_from_directory(static_dir, "index.html")


if __name__ == "__main__":
    if is_dev:
        app.run(debug=True, host="0.0.0.0", port=3000)
    else:
        app.run()
