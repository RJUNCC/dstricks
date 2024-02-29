# check model performance
from sklearn.metrics import make_scorer, mean_squared_error, r2_score, mean_absolute_error
import numpy as np
import pandas as pd

# Function to compute adjusted R-squared
def adj_r2_score(predictors, targets, predictions):
    r2 = r2_score(targets, predictions)
    n = predictors.shape[0]
    k = predictors.shape[1]
    return 1 - ((1 - r2) * (n - 1) / (n - k - 1))


# Function to compute MAPE
def mape_score(targets, predictions):
    return np.mean(np.abs(targets - predictions) / targets) * 100


# Function to compute different metrics to check performance of a regression model
def model_performance_regression(model, predictors, target):
    """
    Function to compute different metrics to check regression model performance

    model: regressor
    predictors: independent variables
    target: dependent variable
    """

    pred = model.predict(predictors)                  # Predict using the independent variables
    r2 = r2_score(target, pred)                       # To compute R-squared
    adjr2 = adj_r2_score(predictors, target, pred)    # To compute adjusted R-squared
    rmse = np.sqrt(mean_squared_error(target, pred))  # To compute RMSE
    mae = mean_absolute_error(target, pred)           # To compute MAE
    mape = mape_score(target, pred)                   # To compute MAPE

    # Creating a dataframe of metrics
    df_perf = pd.DataFrame(
        {
            "RMSE": rmse,
            "MAE": mae,
            "R-squared": r2,
            "Adj. R-squared": adjr2,
            "MAPE": mape,
        },
        index=[0],
    )

    return df_perf

def outlierChecker(data: pd.DataFrame, column: str):
    iqr = data[column].quantile(0.75) - data[column].quantile(0.25)
    upper_outliers = data[data[column] > data[column].quantile(0.75) + 1.5 * iqr]
    lower_outliers = data[data[column] < data[column].quantile(0.25) - 1.5 * iqr]
    return upper_outliers, lower_outliers

def outlierSummary(data: pd.DataFrame, column: str):
    upper, lower = outlierChecker(data, column)
    print(f"Column: {column}")
    print(f"Upper Outliers: {len(upper)}")
    print(f"Lower Outliers: {len(lower)}")
    print(f"Normalized Upper Outliers: {len(upper)/data.shape[0]}")
    print(f"Normalized Lower Outliers: {len(lower)/data.shape[0]}")
    print("-----------------------------------")

def outlierRemoval(data: pd.DataFrame, column: str):
    upper, lower = outlierChecker(data, column)
    data = data.drop(index=list(upper.index))
    data = data.drop(index=list(lower.index))
    return data