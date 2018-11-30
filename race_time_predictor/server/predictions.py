import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import train_test_split

from .queries import fetch_activities


def get_predictions(access_token):
    """Fetch athlete's activities and calculate predictions

    :param access_token: User's OAuth 2 access token for the Strava API
    :type access_token: str
    :return: Predictions
    :rtype: JSON object
    """

    activities = fetch_activities(access_token)

    # Convert activities to pandas dataframe
    dataframe = pd.DataFrame(activities)

    # clean dataframe
    dataframe = clean_dataframe(dataframe, "Run")

    # Create response JSON

    # Check for error
    error = False
    if len(dataframe.index) < 3:
        error = True

    # Check for warning
    warning = False
    if len(dataframe.index) < 10:
        warning = True

    # Prediction times
    predictions = calculate_predictions(dataframe)

    response = {
        "chart": {
            "distances": dataframe["distance"].values.tolist(),
            "times": dataframe["moving_time"].values.tolist(),
        },
        "predictions": {
            "error": error,
            "warning": warning,
            "predictionData": [
                {"distance": "5K", "time": predictions[0]},
                {"distance": "10K", "time": predictions[1]},
                {"distance": "Half marathon", "time": predictions[2]},
                {"distance": "Marathon", "time": predictions[3]},
            ],
        },
    }

    return response


def clean_dataframe(dataframe, type):
    """Filter for only running data

    :param dataframe: A dataframe with all strava data
    :param type: string with either 'Ride' or 'Run'
    :return: dataframe with only data of type 'type'
    """

    # Select only running entries
    dataframe = dataframe.loc[dataframe["type"] == type]

    # Select relevant columns
    dataframe = dataframe[["moving_time", "distance", "total_elevation_gain"]]

    return dataframe


def calculate_predictions(dataframe):
    """Calculate predictions using a kernel ridge regression

    :param dataframe: dataframe of running data
    :return: prediction for running times
    :rtype: int[]
    """
    # Isolation Forest for outlier detection
    rng = pd.np.random.RandomState(42)
    clf = IsolationForest(max_samples=100, random_state=rng, contamination=0.01)
    clf.fit(dataframe)
    dataframe["outlier"] = clf.predict(dataframe)
    dataframe = dataframe.loc[dataframe["outlier"] == 1]
    dataframe = dataframe[["moving_time", "distance", "total_elevation_gain"]]

    # Define Target
    X = dataframe.drop("moving_time", axis=1)
    y = dataframe[["moving_time"]]

    # Split into training and testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=1)

    # Train ridge regression model
    kernel_ridge_model = KernelRidge(alpha=1.0)
    kernel_ridge_model.fit(X_train, y_train)

    # Prediction
    predictions = [
        int(kernel_ridge_model.predict([[5000, 0]])[0][0]),
        int(kernel_ridge_model.predict([[10000, 0]])[0][0]),
        int(kernel_ridge_model.predict([[21097, 0]])[0][0]),
        int(kernel_ridge_model.predict([[42195, 0]])[0][0]),
    ]

    return predictions
