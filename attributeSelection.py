import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from constants import *


def attribute_selection():
    df = pd.read_csv('fulldata.csv')

    df = df.drop(PRICE_COLUMNS, axis=1)
    df = df.drop(DATE_COLUMNS, axis=1)
    data = df.fillna('MISSING')
    for col in data.columns:
        if data[col].dtype == 'object':
            data[col] = data[col].replace('MISSING', df[col].mode()[
                                          0]).infer_objects(copy=False)
        else:
            data[col] = data[col].replace(
                'MISSING', df[col].mean()).infer_objects(copy=False)

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


attribute_selection()
