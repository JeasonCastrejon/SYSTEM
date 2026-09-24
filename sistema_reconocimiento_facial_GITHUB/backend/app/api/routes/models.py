from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models import MLTrainingRecord
from app.services.probability_service import train,load_model
router=APIRouter()
@router.post("/modelos/entrenar")
def entrenar(db:Session=Depends(get_db)):
    rows=db.query(MLTrainingRecord).all()
    try: metrics=train(rows)
    except ValueError as e: raise HTTPException(400,str(e))
    return {"success":True,"message":"Modelo entrenado y calibrado correctamente.","metrics":metrics}
@router.get("/modelos/metricas")
def metricas(db:Session=Depends(get_db)):
    model=load_model()
    if model is None: return {"precision":None,"recall":None,"f1":None,"false_positive_rate":None,"false_negative_rate":None,"confusion_matrix":None,"modelo":None,"muestras":0}
    rows=db.query(MLTrainingRecord).all()
    try: return train(rows)
    except ValueError as e: raise HTTPException(400,str(e))
