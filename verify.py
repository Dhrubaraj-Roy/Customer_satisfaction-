import os

data_path = r"C:\Users\roydh\Desktop\ML2023\MLOps project\Project A\data\olist_customers_dataset.csv"

if os.path.exists(data_path):
    print("CSV file exists at the specified path.")
else:
    print("CSV file does not exist at the specified path.")
