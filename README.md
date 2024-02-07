# End To End Customer Satisfaction MLOps Project Using Zenml And MLFlow 
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![ZenML](https://img.shields.io/badge/ZenML-1.8-green)](https://docs.zenml.io/)
[![MLflow](https://img.shields.io/badge/MLflow-3.0-red)](https://mlflow.org)



## 1. Introduction

This function focuses on predicting customer satisfaction scores (survey scores) for future orders/purchases based on historical order data. We use the Brazilian e-commerce public dataset from Olist which contains 100,000 orders placed on Brazilian markets between 2016-2018. The dataset provides rich information about order details such as status, price, payment method, shipment, customer location etc. with customer written reviews. We use factors such as order status, price bracket, payment method to train a machine learning model that can predict the evaluation score of a new order/purchase. The program uses ZenML to create a complex pipeline of MLOps to simulate these models in practice.

## 🚀 MLflow Pipeline Architecture
![ZenML Pipeline Architecture](https://assets-global.website-files.com/65264f6bf54e751c3a776db1/652fbc286e750e159bf251b5_trainingandif.png)

This diagram visualizes the high-level components and workflow of the MLflow pipeline:
1. **Ingest Data**: Raw data is collected from the source databases/systems and ingested into the MLflow tracking server.
2. **Clean Data**: Pre-processing tasks like data cleaning, feature engineering etc. are applied to transform the raw data into model-ready training data.
3. **Train Model**: The ML model is developed, trained and evaluated using the processed data based on an appropriate machine learning algorithm. Model artifacts like models files, images are registered with MLflow tracking.
4. **Evaluate Model**: The trained model is evaluated on test data using appropriate metrics. The model evaluation results are logged as model runs.
This modular pipeline enables reusable steps for developing, experimenting and deploying machine learning models using MLflow.

## 🛠️ Technology Stack

The key technologies used in the stages of the MLOps pipeline are:

**Orchestration & Pipeline Management**:
- [ZenML](https://github.com/zenml-io/zenml) - Used for building, testing and managing the end-to-end ML pipeline

**Experiment Tracking & Model Management**:  
- [MLflow](https://mlflow.org/) - For logging model experiments, packaging and deployment

**Model Serving**:
- [Streamlit](https://streamlit.io/) - Python framework used to build and serve the interactive web app for model predictions  

## 🔧 Setup & Installation

To set up and install the project:

1. Clone the repository
    ```bash
    git clone <repo_url>
    ```

2. Create and activate a virtual environment 
   ```bash
   virtualenv venv
   source venv/bin/activate
   ```

3. Install Python dependencies
   ```bash
   pip install -r requirements.txt
   ```  

4. Install ZenML integrations
   ```bash
   zenml integration install mlflow -y 
   ```

5. Register MLflow as experiment tracker and model deployer
   ```bash
   zenml experiment-tracker register mlflow_tracker --flavor=mlflow  
   zenml model-deployer register mlflow --flavor=mlflow
   ```

6. Create an MLflow ZenML stack
   ```bash
   zenml stack register mlflow_stack -a default -o default -d mlflow -e 
   mlflow_tracker --set
   ```

7. Run pipeline and deploy model
   ```bash
   python run_pipeline.py
   python run_deployment.py
   ```
## 🚀 Model Deployment 

The `deployment_pipeline.py` handles continuous training and deployment. The key stages are:

- Data ingestion, processing, model training and evaluation (same as training pipeline)
- `deployment_trigger`: Checks if model accuracy meets predefined threshold
- `model_deployer`: Uses MLflow to deploy model to local server if accuracy criteria is met

ZenML logs all MLflow experiments, model artifacts, evaluations metrics to local MLflow tracking server.

If model accuracy meets threshold, pipeline launches MLflow local deployment server to serve latest model. This runs continuously in background to serve new models when better ones are available.

## 💡 Making Predictions

We deploy a Streamlit app to interact with deployed models:

```python
service = prediction_service_loader(
   pipeline_name="continuous_deployment_pipeline",
   running=False,
)

service.predict(data) # Get predictions
```

This asynchronously gets predictions from the latest model deployed via the pipeline, without needing to restart app.

While the example uses local MLflow deployment, ZenML supports integration with Seldon etc for scalable deployments on Kubernetes.

## 🤝 Contributions

Contributions to this project are welcome!

**Reporting issues/bugs**

File a GitHub issue for any bugs or enhancements needed:

- Provide detailed description of the problem
- Include steps to reproduce
- Mention software versions used 
- Attach log files, screenshots if applicable

**Contributing code**

- Fork the repository and create a new branch
- Make code changes and thoroughly test locally
- Ensure CI/CD pipelines pass all checks  
- Update docs if needed
- Open a PR against `main` branch describing work done
- Tag project admins to review for feedback 

**Dev environment**

First complete [setup and installation](setup-install) steps.

Key tools used:

- Python 3.9
- ZenML
- MLflow  

Code formatting:

- Use flake8 linter
- Stick to PEP8 styles
- Add adequate comments  

Testing:

- Write pytest unit tests
- Validate end-to-end pipeline runs


## License 📄

This project is licensed under the MIT license - see [LICENSE](LICENSE) file for details.

**Limitations:**

- Needs at least 5GB RAM for training pipelines 💻
**Support 🆘** 

For help, questions or feedback reach out to:

- Name: Dhrubaraj Roy 
- Email: dhrubarajroy123@gmail.com
- GitHub: [@dhrubarajroy](https://github.com/Dhrubaraj-Roy)

Additionally, you can file a GitHub issue 🐛 or pull request  in this repo for bugs/ enhancements.

