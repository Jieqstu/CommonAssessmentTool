from fastapi import APIRouter
from app.modelmgmt.model_list import get_available_models

router = APIRouter(prefix="/models", tags=["models"])

@router.get("/", summary="List available ML models")
def list_models_route():
    return {"available_models": get_available_models()}

