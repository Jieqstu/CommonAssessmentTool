"""
Model listing and selection module for the Common Assessment Tool.

Provides:
- A list of available machine learning models
- Logic to get the currently active model (mock)
- Support for switching models (Done)

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

def switch_model(model_name):
    """
    Switch the current model if the provided model_name is available.
    Returns True if successful, False otherwise.
    """
    global CURRENT_MODEL
    if model_name in AVAILABLE_MODELS:
        CURRENT_MODEL = model_name
        return True
    return False


