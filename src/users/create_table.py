import random

from google.cloud import bigquery
from schema import schema
from faker import Faker
import uuid

fake = Faker()


def generate_users():
    users = []
    # generate and add users to the list
    for n in range(10000):
        gender = random.choice(["Male", "Female"])
        firstname = fake.first_name_male() if gender == "Male" else fake.first_name_female()
        lastname = fake.last_name()
        age = random.randrange(18, 80)
        id = str(uuid.uuid1())
        country = fake.country()
        email = firstname+"."+lastname+"@gmail.com"

        user = {"first_name": firstname, "last_name": lastname, "age": age, "id": id, "gender": gender,
            "country": country, "email": email}
        users.append(user)
    return users


# Construct a BigQuery client object.
client = bigquery.Client()

table_id = "valued-decker-380221.donnees_hm.clients"

table = bigquery.Table(table_id, schema=schema)

client.delete_table(table)
table = client.create_table(table)  # Make an API request.
print("Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))

rows_to_insert = generate_users()

errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
if not errors:
    print("New rows have been added.")
else:
    print("Encountered errors while inserting rows: {}".format(errors))
