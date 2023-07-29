import logging
import pandas as pd
from zenml import step

class IngestData:
    """Ingests data from a csv file.   This class"""
    def __init__(self, data_path : str):
        self.data_path = data_path
    def get_data(self):
        logging.info(f"Ingest data from {self.data_path}")
        return pd.read_csv(self.data_path)
    
@step
def ingest_df(data_path : str):
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")
        raise e
    
        