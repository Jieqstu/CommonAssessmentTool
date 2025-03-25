from fastapi import APIRouter
from app.modelmgmt.model_list import get_available_models, get_current_model

router = APIRouter(prefix="/models", tags=["models"])

@router.get("/", summary="List available ML models")
def list_models_route():
    return {"available_models": get_available_models()}

@router.get("/current", summary="Get current ML model")
def current_model():
    return {"current_model": get_current_model()}

