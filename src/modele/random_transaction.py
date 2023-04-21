# Choose a random user in big query database and assigning him 3 random articles from articles.csv

from google.cloud import bigquery
import pandas as pd
import random

# Initialize BigQuery client
client = bigquery.Client()

# Fetch a random user from BigQuery
query = """
    SELECT id
    FROM `valued-decker-380221.donnees_hm.clients`
    ORDER BY RAND()
    LIMIT 1
"""
query_job = client.query(query)
result = query_job.result()
user_id = list(result)[0][0]

# Load articles from CSV into a DataFrame
articles_df = pd.read_csv('articles.csv')

# Randomly assign 3 articles to the user
random_articles = articles_df.sample(n=3)

# Print the randomly assigned articles
print("User ID:", user_id)
print("Randomly assigned articles:")
print(random_articles['prod_name'])
