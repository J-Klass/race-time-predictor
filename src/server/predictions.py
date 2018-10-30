import pandas as pd

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def calculate_predictions(activities):

    # Convert activities JSON to pandas dataframe
    dataframe = pd.DataFrame(activities)

    # Select only running entries
    dataframe = dataframe.loc[dataframe["type"] == "Run"]

    # Select relevant columns
    dataframe = dataframe[["moving_time", "distance", "total_elevation_gain"]]

    # Define Target
    X = dataframe.drop("moving_time", axis=1)
    y = dataframe[["moving_time"]]

    # Split into training and testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

    # Train regression model
    regression_model = LinearRegression()
    regression_model.fit(X_train, y_train)

    # Model validation
    print("score: ", regression_model.score(X_test, y_test))
    y_predict = regression_model.predict(X_test)
    regression_model_mse = mean_squared_error(y_predict, y_test)
    print("MSE: ", regression_model_mse)

    # Prediction
    predictions = []
    predictions.append(regression_model.predict([[5000, 0]]))
    predictions.append(regression_model.predict([[10000, 0]]))
    predictions.append(regression_model.predict([[21100, 0]]))
    predictions.append(regression_model.predict([[42195, 0]]))

    return predictions
