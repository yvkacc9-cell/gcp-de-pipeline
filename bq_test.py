from google.cloud import bigquery

client = bigquery.Client(project="yvk987")

query = """
SELECT name, SUM(number) AS total
FROM `bigquery-public-data.usa_names.usa_1910_2013`
GROUP BY name
ORDER BY total DESC
LIMIT 5
"""

df = client.query(query).to_dataframe()
print(df)