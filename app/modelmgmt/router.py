from fastapi import APIRouter
from fastapi import HTTPException, Query
from app.modelmgmt.model_list import get_available_models, get_current_model, switch_model

router = APIRouter(prefix="/models", tags=["models"])

@router.get("/", summary="List available ML models")
def list_models_route():
    return {"available_models": get_available_models()}

@router.get("/current", summary="Get current ML model")
def current_model():
    return {"current_model": get_current_model()}

@router.post("/switch", summary="Switch the active ML model")
def switch_model_endpoint(model: str = Query(..., description="Name of the model to switch to")):
    if switch_model(model):
        return {"message": f"Switched to {model}"}
    else:
        raise HTTPException(status_code=400, detail="Model not found. Available models: " + ", ".join(get_available_models()))
