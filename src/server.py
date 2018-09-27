import json
import os

from flask import Flask, redirect, request
from stravalib import Client

app = Flask(__name__)
client = Client()
current_dir = os.path.dirname(os.path.realpath(__file__))


if "FLASK_ENV" in os.environ and os.environ["FLASK_ENV"] == "development":
    BASE_URL = "http://localhost:3000"
else:
    BASE_URL = "http://localhost:3000"  # TODO


with open(os.path.join(os.path.dirname(current_dir), "config.json")) as config_file:
    config = json.load(config_file)
    CLIENT_ID = config["clientId"]
    CLIENT_SECRET = config["clientSecret"]


@app.route("/")
def hello():
    return "Hello World!"


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


if __name__ == "__main__":
    if "FLASK_ENV" in os.environ and os.environ["FLASK_ENV"] == "development":
        app.run(host="0.0.0.0", port=3000)
    else:
        app.run()
