
from zenml.client import Client
from pipelines.trianing_pipeline import train_pipeline




if __name__ == '__main__':
    train_pipeline(data_path='/home/dhruba/MLOps_projects/customer-stisfaction/Customer_satisfaction-/data/olist_customers_dataset (2).csv')
# python3 -m venv MLOp
# source newmlops/bin/activate
#  python3 run_pipeline.py
#  python3 run_deployment.py --config deploy
# python3 run_deployment.py --config predict

# zenml integration install mlflow -y
#  zenml experiment-tracker register mlflow_tracker_dhruba  --flavor=mlflow
#  zenml model-deployer register mlflow_dhruba --flavor=mlflow
# zenml stack register mlflow_tracker_dhruba -a default -o default -d mlflow_dhruba -e mlflow_tracker --set



# zenml experiment-tracker register mlflow_the_newone --flavor=mlflow
#  zenml model-deployer register mlflow3 --flavor=mlflow

# zenml stack register mlflow_the_newone -a default -o default -d mlflow3 -e mlflow_tracker --set

# streamlit run streamlit_app.py