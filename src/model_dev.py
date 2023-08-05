import logging
from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression

class Model(ABC):
    """
    Abstract base class for all models.
    """

    
    @abstractmethod
    def train(self, X_train, y_train):
        """
        Trains the model on the given data.

        Args:
            x_train: Training data
            y_train: Target data
        """
        pass 



class LinearRegressionModel(Model):
    def train(self, X_train, y_train, **kwargs):
        try:
            reg = LinearRegression(**kwargs)
            reg.fit(X_train, y_train)
            logging.info("Model traind completed")
            return reg


        except Exception as e:
            logging.error("error in training model: {}".format(e))
            raise e     
                