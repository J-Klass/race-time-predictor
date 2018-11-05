import os
from concurrent.futures import ThreadPoolExecutor

from flask import Flask, request, send_from_directory

from server.auth import get_access_credentials
from server.config import load_config
from server.exceptions import AuthError
from server.predictions import get_predictions
from server.queries import fetch_profile, fetch_stats
from server.responses import success, auth_error, server_error

app = Flask(__name__)

# Detect development/production environment from env variable
is_dev = "FLASK_ENV" in os.environ and os.environ["FLASK_ENV"] == "development"

# Directories
src_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(src_dir)
static_dir = os.path.join(project_dir, "dist")

# Configuration
client_id, client_secret = load_config()


@app.route("/api/athlete", methods=["GET"])
def get_athlete():
    """Fetch athlete profile and activities from Strava, run machine-learning algorithm to obtain
    predictions, and return relevant results to the client. Request must contain OAuth 2 code as
    query param

    :return: Athlete information and race predictions
    :rtype: JSON object
    """

    # Fetch access token using code
    code = request.args.get("code")
    try:
        access_token, athlete_id = get_access_credentials(client_id, client_secret, code)
    except AuthError as e:
        return auth_error(e)
    except Exception as e:
        return server_error(e)

    # Get profile, stats, and predictions in parallel
    with ThreadPoolExecutor(3) as pool:
        future_profile = pool.submit(fetch_profile, access_token)
        future_stats = pool.submit(fetch_stats, access_token, athlete_id)
        future_predictions = pool.submit(get_predictions, access_token)
        futures = [future_profile, future_stats, future_predictions]

    # Handle exceptions
    for future in futures:
        e = future.exception()
        if e:
            if type(e) == AuthError:
                return auth_error(e)
            else:
                return server_error(e)

    # Send data to client
    data = {
        "profile": future_profile.result(),
        "stats": future_stats.result(),
        "predictions": future_predictions.result(),
    }
    return success(data)


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
