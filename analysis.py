import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score
from constants import *
import warnings

warnings.filterwarnings(action='ignore', category=FutureWarning)


def clean_nan(df):
    data = df.fillna('MISSING')
    for col in data.columns:
        if data[col].dtype == 'object':
            data[col] = data[col].replace('MISSING', df[col].mode()[
                                          0])
        else:
            data[col] = data[col].replace(
                'MISSING', df[col].mean())
    return data


def pca_selection(df):
    data = clean_nan(df)
    X_standardized = StandardScaler().fit_transform(data)

    # Applying PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_standardized)

    # Print the feature importance
    feature_importance = np.abs(pca.components_).sum(axis=0)
    for i, column in enumerate(data.columns):
        print(f"Feature importance of {column}: {feature_importance[i]}")
    # Checking the variance explained by the 2 principal components
    print("Explained variance ratio:", pca.explained_variance_ratio_)
    return X_pca


def linear_regression(X, y):
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Create a LinearRegression object
    lr = LinearRegression()

    # Fit the model to the training data
    lr.fit(X_train, y_train)

    # Predict the target variable for the test data
    y_pred = lr.predict(X_test)

    # Calculate the mean squared error of the predictions
    mse = mean_squared_error(y_test, y_pred)
    r2 = lr.score(X_test, y_test)

    print("Mean Squared Error:", mse)
    print("R-squared score:", r2)

    return lr


def random_forest(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Training a classifier, for example, a random forest classifier
    classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    classifier.fit(X_train, y_train)

    # Predicting the class for the test set
    y_pred = classifier.predict(X_test)

    # Evaluating the classifier
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')


# run
df = pd.read_csv('fulldata.csv')
X = df.drop(PRICE_COLUMNS+DATE_COLUMNS, axis=1)
y = df['avg_price']
X_pca = pca_selection(X)
# std_X = StandardScaler().fit_transform(clean_nan(X))
# linear_regression(std_X, y)
random_forest(X_pca, y)
