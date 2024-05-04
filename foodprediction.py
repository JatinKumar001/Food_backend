import sys
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

# Load the dataset
recipes_df = pd.read_csv("recipes_data.csv", nrows=1000)

# Preprocess the data
recipes_df['ingredients'] = recipes_df['ingredients'].apply(eval)

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the ingredients column
ingredients_str = [' '.join(ing) for ing in recipes_df['ingredients']]
tfidf_matrix = tfidf_vectorizer.fit_transform(ingredients_str)

# Function to predict food based on ingredients
def predict_food(ingredient_list, num_recommendations=5):
  # Transform input ingredients
  input_tfidf = tfidf_vectorizer.transform([' '.join(ingredient_list)])

  # Compute cosine similarity
  cosine_sim = cosine_similarity(input_tfidf, tfidf_matrix)

  # Get indices of most similar recipes
  sim_indices = cosine_sim.argsort()[0][-num_recommendations-1:-1][::-1]

  # Create a list to store recommended recipes data
  recommendations = []
  for idx, sim_idx in enumerate(sim_indices, start=1):
        recipe_data = {}
        recipe_data["id"] = idx  # Assign ID
        recipe_data["title"] = recipes_df['title'].iloc[sim_idx]
        recipe_data["link"] = recipes_df['link'].iloc[sim_idx]
        recipe_data["ingredients"] = recipes_df['ingredients'].iloc[sim_idx]
        # Check if directions column exists before adding
        if 'directions' in recipes_df.columns:
            recipe_data["directions"] = recipes_df['directions'].iloc[sim_idx]
        else:
            recipe_data["directions"] = "Not Available"
        recommendations.append(recipe_data)

  # Return the recommendations as JSON
  return json.dumps(recommendations)

# Example usage
ingredient_list = [str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]), str(sys.argv[5]), str(sys.argv[6])]
recommendations_json = predict_food(ingredient_list)
print(recommendations_json)