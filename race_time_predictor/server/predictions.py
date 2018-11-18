import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
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

    # check for error
    error = False
    if len(dataframe.index) < 3:
        error = True

    # check for warning
    warning = False
    if len(dataframe.index) < 10:
        warning = True

    # prediction times
    times = calculate_prediction_5_10_half(dataframe)
    prediction_marathon = calculate_prediction_marathon(dataframe)
    times.append(prediction_marathon)

    predictions = {
        "chart": {
            "distances": dataframe["distance"].values.tolist(),
            "times": dataframe["moving_time"].values.tolist(),
        },
        "predictions": {
            "error": error,
            "warning": warning,
            "predictionData": [
                {"distance": "5K", "time": times[0]},
                {"distance": "10K", "time": times[1]},
                {"distance": "Half marathon", "time": times[2]},
                {"distance": "Marathon", "time": times[3]},
            ],
        },
    }

    return predictions


def clean_dataframe(dataframe, type):
    """Filter for only running data

    :param dataframe: A dataframe with all strava data
    :param type: string with either 'Ride' or 'Run'
    :return: dataframe with only data of type 'Run'
    """

    # TODO: Delete extreme outliers to avoid data with measuring error

    # Select only running entries
    dataframe = dataframe.loc[dataframe["type"] == type]

    # Select relevant columns
    dataframe = dataframe[["moving_time", "distance", "total_elevation_gain"]]

    return dataframe


def calculate_prediction_marathon(dataframe):
    """Calculate marathon prediction using a ridge regression

    :param dataframe: dataframe of running data
    :return: prediction for marathon time
    :rtype: int
    """

    # Define Target
    X = dataframe.drop("moving_time", axis=1)
    y = dataframe[["moving_time"]]

    # Split into training and testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=1)

    # Train ridge regression model
    ridge_regression_model = Ridge(alpha=0.01)
    ridge_regression_model.fit(X_train, y_train)

    # Prediction
    prediction = int(ridge_regression_model.predict([[42195, 0]])[0][0])

    return prediction


def calculate_prediction_5_10_half(dataframe):
    """Calculate prediction for 5k, 10k and half-marathon

    :param dataframe: dataframe of running data
    :return: prediction for 5K, 10k, half-marathon
    :rtype: int[]
    """

    # Filter dataframe by 'Distance'
    dataframe = dataframe.loc[dataframe["distance"] < 40000]

    # Define Target
    X = dataframe.drop("moving_time", axis=1)
    y = dataframe[["moving_time"]]

    # Split into training and testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=1)

    # Train regression model
    linear_regression_model = LinearRegression()
    linear_regression_model.fit(X_train, y_train)

    predictions = [
        int(linear_regression_model.predict([[5000, 0]])[0][0]),
        int(linear_regression_model.predict([[10000, 0]])[0][0]),
        int(linear_regression_model.predict([[21097, 0]])[0][0]),
    ]

    return predictions
