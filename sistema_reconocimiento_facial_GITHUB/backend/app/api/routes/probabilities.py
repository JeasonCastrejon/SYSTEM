from fastapi import APIRouter,HTTPException
from app.schemas.recognition_schema import ProbabilityInput
from app.services.probability_service import predict
router=APIRouter()
@router.post("/probabilidades/prediccion")
def prediccion(payload:ProbabilityInput):
    for field in ["similitud","distancia","calidad_imagen","iluminacion"]:
        value=getattr(payload,field)
        if value<0: raise HTTPException(400,f"{field} no puede ser negativo.")
    if payload.similitud>1 or payload.calidad_imagen>1 or payload.iluminacion>1: raise HTTPException(400,"similitud, calidad_imagen e iluminacion deben estar entre 0 y 1.")
    try:return {"success":True,"probabilidad_calibrada":predict(payload)}
    except FileNotFoundError as e: raise HTTPException(400,str(e))
