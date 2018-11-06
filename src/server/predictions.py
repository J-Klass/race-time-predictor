import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from server.queries import fetch_activities


def get_predictions(access_token):
    """Fetch athlete's activities and calculate predictions

    :param access_token: User's OAuth 2 access token for the Strava API
    :type access_token: str
    :return: Predictions
    :rtype: dict

    """

    activities = fetch_activities(access_token)
    return calculate_predictions(activities)


def calculate_predictions(activities):
    """
    Calculate predictions
    :param activities: list of user activities from strava
    :type: JSON object
    :return: predictions
    """

    # Convert activities to pandas dataframe
    dataframe = pd.DataFrame(activities)

    # Get predictions
    predictions = {}

    predictions_5_10_half = calculate_prediction_5_10_half(dataframe)
    predictions.update(predictions_5_10_half)

    prediction_marathon = calculate_prediction_marathon(dataframe)
    predictions["Marathon"] = prediction_marathon

    return predictions


def clean_dataframe(dataframe, type):
    """
    Filter for only running data
    :param dataframe: A dataframe with all strava data
    :param type: string with eiter 'Ride' or 'Run'
    :return: dataframe with only data of type 'Run'
    """

    # TODO: Delete extreme outliers to avoid data with measuring error

    # Select only running entries
    dataframe = dataframe.loc[dataframe["type"] == type]

    # Select relevant columns
    dataframe = dataframe[["moving_time", "distance", "total_elevation_gain"]]

    return dataframe


def calculate_prediction_marathon(dataframe):
    """
    Calculate marathon prediction using a ridge regression
    :param dataframe: dataframe of running data
    :return: prediction for marathon time
    :rtype: int
    """

    dataframe = clean_dataframe(dataframe, "Run")

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
    """
    Calculate prediction for 5k, 10k and half-marathon
    :param dataframe: dataframe of running data
    :return: prediction for 5K, 10k, half-marathon
    :rtype: int[]
    """

    dataframe = clean_dataframe(dataframe, "Run")

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

    # Model validation
    print("score: ", linear_regression_model.score(X_test, y_test))
    y_predict = linear_regression_model.predict(X_test)
    linear_regression_model_mse = mean_squared_error(y_predict, y_test)
    print("MSE: ", linear_regression_model_mse)

    predictions = {
        "5K": int(linear_regression_model.predict([[5000, 0]])[0][0]),
        "10K": int(linear_regression_model.predict([[10000, 0]])[0][0]),
        "Half marathon": int(linear_regression_model.predict([[21097, 0]])[0][0]),
    }

    return predictions
