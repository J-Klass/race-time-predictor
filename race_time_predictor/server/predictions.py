import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split, GridSearchCV

from .queries import fetch_activities

MARATHON = 42195
HALF_MARATHON = 21097
TEN_K = 10000
FIVE_K = 5000


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

    # Get graph data
    chart = create_graph_data(dataframe)

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
    predictions = calculate_predictions(dataframe)["predictions"]

    # Prediction graph
    prediction_graph = calculate_predictions(dataframe)["prediction_graph"]

    response = {
        "chart": chart,
        "predictions": {
            "error": error,
            "warning": warning,
            "predictionData": [
                {"title": "5K", "time": predictions[0], "distance": FIVE_K},
                {"title": "10K", "time": predictions[1], "distance": TEN_K},
                {"title": "Half marathon", "time": predictions[2], "distance": HALF_MARATHON},
                {"title": "Marathon", "time": predictions[3], "distance": MARATHON},
            ],
        },
        "predictions_graph": prediction_graph,
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
    dataframe = dataframe[
        ["moving_time", "distance", "total_elevation_gain", "elev_high", "elev_low"]
    ]

    # Isolation Forest for outlier detection
    rng = pd.np.random.RandomState(42)
    clf = IsolationForest(max_samples=100, random_state=rng, contamination=0.01)
    clf.fit(dataframe)
    dataframe["outlier"] = clf.predict(dataframe)
    dataframe = dataframe.loc[dataframe["outlier"] == 1]
    dataframe = dataframe[["moving_time", "distance", "total_elevation_gain", "elev_high"]]

    return dataframe


def calculate_predictions(dataframe):
    """Calculate predictions using a kernel ridge regression

    :param dataframe: dataframe of running data
    :return: prediction for running times
    :rtype: int[]
    """

    # Define Target
    X = dataframe.drop("moving_time", axis=1)
    y = dataframe[["moving_time"]]

    # Split into training and testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=1)

    # Train ridge regression model
    params = {"alpha": [25, 10, 4, 2, 1.0, 0.8, 0.5, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01]}
    kernel_ridge_model = GridSearchCV(Ridge(), params, cv=5, verbose=1)
    kernel_ridge_model.fit(X_train, y_train)

    # Prediction
    predictions = [
        int(kernel_ridge_model.predict([[FIVE_K, 0, 0]])[0][0]),
        int(kernel_ridge_model.predict([[TEN_K, 0, 0]])[0][0]),
        int(kernel_ridge_model.predict([[HALF_MARATHON, 0, 0]])[0][0]),
        int(kernel_ridge_model.predict([[MARATHON, 0, 0]])[0][0]),
    ]

    # Prediction graph
    prediction_graph = []
    for i in range(5000, 51000, 1000):
        prediction_graph.append(
            {"distance": i, "time": int(kernel_ridge_model.predict([[i, 0, 0]])[0][0])}
        )

    return {"predictions": predictions, "prediction_graph": prediction_graph}


def create_graph_data(dataframe):
    """Create graph data

    :param dataframe:
    :return: JSON with graph data
    """

    dataframe = dataframe.loc[dataframe["type"] == "Run"]

    dataframe = dataframe[["moving_time", "distance", "total_elevation_gain", "start_date"]]
    chart = dataframe.to_dict("records")

    return chart
