from zenml.client import Client
from pipelines.trianing_pipeline import train_pipeline




if __name__ == '__main__':
    # Initialize the ZenML Client

    # train_pipeline()
    train_pipeline(data_path=r"C:\Users\roydh\Desktop\ML2023\MLOps project\Project A\data\olist_customers_dataset (2).csv")

