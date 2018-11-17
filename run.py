from os import environ

from race_time_predictor import app

if __name__ == "__main__":
    if "FLASK_ENV" in environ and environ["FLASK_ENV"] == "development":
        app.run(debug=True, host="0.0.0.0")
    else:
        app.run()
