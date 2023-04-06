import psycopg2


conn_string = f'postgresql://karenalo13:91CMVrdLIPka@ep-autumn-dream-433615.eu-central-1.aws.neon.tech/neondb'
# establish a connection to the database
conn = psycopg2.connect(conn_string)

# create a cursor object to execute SQL queries
cur = conn.cursor()

# specify the table you want to select from
table_name = "Item"

# construct the SQL query
query = f"SELECT * FROM {table_name};"

# execute the query and fetch all results
cur.execute(query)
results = cur.fetchall()
print(results)
# print out the results
for row in results:
    print(row)
    print('\n')

# close the cursor and connection
cur.close()
conn.close()
