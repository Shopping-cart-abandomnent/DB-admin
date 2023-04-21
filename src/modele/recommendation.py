from random_transaction import *

# recommendation rules
reco_df = articles_df.copy()
reco_df["score"] = 0

# Same product type
for _, product in random_articles.iterrows():
    reco_df.loc[reco_df["product_type_name"] == product["product_type_name"], "score"] += 1

# Same color
for _, product in random_articles.iterrows():
    reco_df.loc[reco_df["colour_group_name"] == product["colour_group_name"], "score"] += 1

# Same product group
for _, product in random_articles.iterrows():
    reco_df.loc[reco_df["product_group_name"] == product["product_group_name"], "score"] += 1

# Same garment group
for _, product in random_articles.iterrows():
    reco_df.loc[reco_df["garment_group_name"] == product["garment_group_name"], "score"] += 1

# Sorting by score and print the 2 best recommendations
reco_df = reco_df[reco_df.index != random_articles.index[0]]
reco_df = reco_df[reco_df.index != random_articles.index[1]]
reco_df = reco_df[reco_df.index != random_articles.index[2]]
reco_df = reco_df.sort_values(by=["score"], ascending=False).head(2)

print("\nRecommended products :")
for _, product in reco_df.iterrows():
    print("- " + product["prod_name"])
