import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import sys

np.random.seed(5)

recipes_df = pd.read_csv("recipes_data.csv", nrows=1000)

# Preprocess the data
recipes_df['ingredients'] = recipes_df['ingredients'].apply(eval)

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the ingredients column
ingredients_str = [' '.join(ing) for ing in recipes_df['ingredients']]
tfidf_matrix = tfidf_vectorizer.fit_transform(ingredients_str)

# nltk.download('punkt')

from sklearn.cluster import KMeans

km = KMeans(n_clusters=5)

km.fit(tfidf_matrix)

clusters = km.labels_.tolist()

recipes_df["cluster"] = clusters

recipes_df['cluster'].value_counts()


def predict_similar_recipe(previous_recipe, n_recommendations=4):
    # Find the cluster of the previous recipe
    previous_recipe_cluster = recipes_df.loc[recipes_df['title'] == previous_recipe, 'cluster'].values[0]

    # Filter recipe in the same cluster as the previous recipe
    similar_recipe = recipes_df[recipes_df['cluster'] == previous_recipe_cluster]

    # Exclude the previous movie itself
    similar_recipe = similar_recipe[similar_recipe['title'] != previous_recipe]

    # Sort similar recipe based on some criteria and select top recommendations
    similar_recipe = similar_recipe.head(n_recommendations)

    # Convert output to JSON format
    output_json = similar_recipe[['title', 'link']].to_json(orient='records')

    return output_json

# Example: Predict similar recipe after making "No-Bake Nut Cookies"
previous_recipe = str(sys.argv[1])
similar_recipe = predict_similar_recipe(previous_recipe)
# print("Similar recipe to", previous_recipe, ":", similar_recipe)
print(similar_recipe)