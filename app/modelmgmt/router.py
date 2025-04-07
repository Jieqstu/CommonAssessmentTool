from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.modelmgmt.model_list import (
    get_available_models,
    get_current_model,
    switch_model,
)

router = APIRouter(prefix="/models", tags=["models"])


class ModelSwitchRequest(BaseModel):
    model: str


@router.get("/", summary="List available ML models")
def list_models_route():
    return {"available_models": get_available_models()}


@router.get("/current", summary="Get current ML model")
def current_model():
    return {"current_model": get_current_model()}


@router.post("/switch", summary="Switch current ML model")
def switch_model_route(request: ModelSwitchRequest):
    try:
        switch_model(request.model)
        return {"message": f"Model switched to {request.model}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
