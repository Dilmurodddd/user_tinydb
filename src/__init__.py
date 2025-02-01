from csv_to_db import read_csv, insert_into_db
from csv_to_db import query_db


# class STUDENT:
# 
    # def __init__(self, data_csv_copy_path, insert_json_path):
        # self.data_csv_copy_path = data_csv_copy_path
        # self.insert_json_path = insert_json_path
        # # Read CSV file
        # data = read_csv(data_csv_copy_path)
        # 
        # # Insert into database
        # insert_into_db(data, insert_json_path)
# 



# Read CSV file
data = read_csv('/home/dilmurod/terminal/user_tinydb/user_data.csv')

# Insert into database
insert_into_db(data, 'users.json')

# Get all records
all_users = query_db('users.json')

# Filter by specific field
male_users = query_db('users.json', 'gender', 'Male')