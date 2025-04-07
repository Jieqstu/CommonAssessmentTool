"""
Model listing and selection module for the Common Assessment Tool.

Provides:
- A list of available machine learning models
- Logic to get the currently active model (mock)
- Support for switching models (to be implemented)

Currently uses a static list and a mock current model for demonstration purposes.
"""

AVAILABLE_MODELS = ["random_forest", "svm", "xgboost"]
CURRENT_MODEL = "random_forest"


def get_available_models():
    """
    Return a list of available mock models.
    """
    return AVAILABLE_MODELS


def get_current_model():
    """
    Return the currently active model (mock).
    """
    return CURRENT_MODEL


def switch_model(new_model: str):
    """
    Switch the current model to a new one if it's available.

    Args:
        new_model (str): The name of the model to switch to

    Raises:
        ValueError: If the model is not in the available list
    """
    global CURRENT_MODEL
    if new_model not in AVAILABLE_MODELS:
        raise ValueError(f"Model '{new_model}' is not in the available list.")
    CURRENT_MODEL = new_model
