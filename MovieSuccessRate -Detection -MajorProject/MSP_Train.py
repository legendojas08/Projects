import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the dataset
data = pd.read_csv('movies_dataset.csv')

# Data Preprocessing
# Handling missing values
data = data.dropna()

# Feature engineering
data['release_month'] = pd.to_datetime(data['release_date']).dt.month

# Define features and target
categorical_features = ['genre', 'director']
numerical_features = ['budget', 'runtime']
X = data[['budget', 'runtime', 'genre', 'director', 'release_month']]
y = data['success']  # Assuming 'success' is a binary column

# Splitting data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)])

# Model pipeline
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('classifier', LogisticRegression())])

# Model training
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'movie_success_predictor.pkl')
