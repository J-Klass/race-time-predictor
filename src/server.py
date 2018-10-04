import json
import os

from flask import Flask, request, send_from_directory

from server.config import load_config
from server.queries import fetch_activities, fetch_profile
from server.auth import get_access_credentials

app = Flask(__name__)
is_dev = "FLASK_ENV" in os.environ and os.environ["FLASK_ENV"] == "development"

# Directories
src_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(src_dir)
static_dir = os.path.join(project_dir, "dist")

# Configuration
client_id, client_secret = load_config(os.path.join(project_dir, "config.json"))


@app.route("/profile", methods=["GET"])
def get_profile():
    # Fetch access token using code
    code = request.args.get("code")
    access_token, athlete_id = get_access_credentials(client_id, client_secret, code)
    if access_token is None:
        return json.dumps({"success": False}), 400, {"ContentType": "application/json"}

    # Fetch athlete profile and stats
    profile = fetch_profile(access_token, athlete_id)

    return (
        json.dumps({"success": True, "profile": profile}),
        200,
        {"ContentType": "application/json"},
    )


@app.route("/predictions", methods=["GET"])
def get_predictions():
    # Fetch access token using code
    code = request.args.get("code")
    access_token, athlete_id = get_access_credentials(client_id, client_secret, code)
    if access_token is None:
        return json.dumps({"success": False}), 400, {"ContentType": "application/json"}

    # Fetch athlete's activities
    activities = fetch_activities(access_token)
    print(activities)

    # TODO calculate and return predictions
    predictions = {}

    return (
        json.dumps({"success": True, "predictions": predictions}),
        200,
        {"ContentType": "application/json"},
    )


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
