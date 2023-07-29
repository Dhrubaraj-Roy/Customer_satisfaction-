import logging
import pandas as pd      
from src.data_cleaning import DataCleaning , DataDivideStrategy, DataPreProcessStrategy
from zenml  import step
from typing import Tuple
from typing_extensions import Annotated

@step
def clean_df(df: pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame, "X_train"],
    Annotated[pd.DataFrame, "X_test"],
    Annotated[pd.Series, "y_train"],
    Annotated[pd.Series, "y_test"],

] :
    try:   
        process_staregy = DataPreprocessStrategy()
        data_cleaning = DataCleaning(df, process_staregy)
        processed_data = DataCleaning.handle_data()

        divide_staregy = DataDivideStaregy()
        data_cleaning = DataCleaning(processed_data, divide_staregy)
        X_train, X_test, y_train, y_test = data_cleaning.handle_data()
        logging.info("Data cleaning completed")
        return X_train, X_test, y_train, y_test
    except Exception as e:
        logging.error("Error in cleaning {}".format(e))
        raise e
