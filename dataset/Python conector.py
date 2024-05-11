# Import necessary libraries
import pandas as pd
import duckdb

# Set .db file path
db_path = r"C:\Users\Veronica\M2\ih_datamadpt0124_project_m2\dataset\dataset.db"

# Establish a connection to the .db file
con = duckdb.connect(db_path)

# Query a table with all tables in the database
db_tables = '''SELECT table_name FROM information_schema.tables WHERE table_schema = 'main';'''
db_tables_df = con.sql(db_tables).df()
db_tables_df
print(db_tables_df)

# Create a dataframe for every table and load them in a list
dataframes = []
for table in db_tables_df['table_name']:
    query_table = f'''SELECT * FROM {table};'''
    df_10 = con.sql(query_table).df()
    dataframes.append(df_10)
print(len(dataframes))

# Load every dataframe in a pytho object in order to be loaded into Power BI
agents = dataframes[0]
bookings = dataframes[1]
customers = dataframes[2]
destinations = dataframes[3]
flights = dataframes[4]
hotels = dataframes[5]
Locations = dataframes[6]
payments = dataframes[7]
promotions = dataframes[8]
reviews = dataframes[9]
tickets = dataframes[10]


# Close the connection to database explicitly
con.close()

