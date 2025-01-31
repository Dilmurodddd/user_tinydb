from csv_to_db import read_csv, insert_into_db

# Read CSV file
data = read_csv('/home/dilmurod/terminal/user_tinydb/user_data.csv')

# Insert into database
insert_into_db(data, '/home/dilmurod/terminal/user_tinydb/user_data.json')