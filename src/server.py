import json
import os

from flask import Flask, redirect, request, send_from_directory
from stravalib import Client

app = Flask(__name__)
is_dev = "FLASK_ENV" in os.environ and os.environ["FLASK_ENV"] == "development"

# Strava API client
client = Client()

# Directories
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
static_dir = os.path.join(parent_dir, "dist")


if is_dev:
    BASE_URL = "http://localhost:3000"
else:
    BASE_URL = "http://localhost:3000"  # TODO


with open(os.path.join(os.path.dirname(current_dir), "config.json")) as config_file:
    config = json.load(config_file)
    CLIENT_ID = config["clientId"]
    CLIENT_SECRET = config["clientSecret"]


@app.route("/auth-new", methods=["GET"])
def get_auth_url():
    redirect_uri = BASE_URL + "/auth-redirect"
    url = client.authorization_url(client_id=CLIENT_ID, scope="write", redirect_uri=redirect_uri)
    return redirect(url, code=302)


@app.route("/auth-redirect", methods=["GET"])
def parse_tokens():
    code = request.args.get("code")
    access_token = client.exchange_code_for_token(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET, code=code
    )
    print(access_token)
    return redirect("/", code=302)


# Serve static files in development mode (handled by nginx in production)
if is_dev:

    @app.route("/", methods=["GET"])
    def get_html():
        return send_from_directory(static_dir, "index.html")

    @app.route("/<path:path>")
    def catch_all(path):
        return send_from_directory(static_dir, path)


if __name__ == "__main__":
    if is_dev:
        app.run(debug=True, host="0.0.0.0", port=3000)
    else:
        app.run()
