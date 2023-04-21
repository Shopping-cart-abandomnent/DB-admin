from google.cloud import bigquery

# Construct a BigQuery client object.
from src.articles.schema import schema

client = bigquery.Client()

table_id = "valued-decker-380221.donnees_hm.articles"

job_config = bigquery.LoadJobConfig(
    schema=schema,
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
uri = "gs://bucket_hm/articles.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))