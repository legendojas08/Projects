import joblib
import pandas as pd

# Load the model from the file
model = joblib.load('movie_success_predictor.pkl')

# Example new movie data
new_movies = pd.DataFrame({
    'budget': [100000000, 50000000],
    'runtime': [120, 90],
    'genre': ['Action', 'Comedy'],
    'director': ['Director A', 'Director B'],
    'release_month': [7, 12]
})

# Make predictions
predictions = model.predict(new_movies)

# Print predictions
for i, prediction in enumerate(predictions):
    print(f"Movie {i+1}: {'Hit' if prediction == 1 else 'Flop'}")
