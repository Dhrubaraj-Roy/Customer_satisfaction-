from zenml import pipeline
from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluation import evaluate_model


@pipeline(enable_ceche=True)
def train_pipeline(data_path: str):
    '''
    Data pipeline for training the model.

    Args:
        data_path: The path to the data to be ingested.
    '''


    # Ingest data using the ingest_df step
    df = ingest_df(data_path)

    # Perform data cleaning using the clean_df step
    X_train, X_test, y_train, y_test =clean_df(df)

    
    # Train the model using the train_model step
    model = train_model(X_train, X_test, y_train, y_test)   
    r2_score, rmse = evaluate_model(model, X_test, y_test)
