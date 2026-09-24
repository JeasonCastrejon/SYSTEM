from fastapi import APIRouter,Depends,File,UploadFile,HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models import Persona,FaceEmbedding,RecognitionLog,MLTrainingRecord
from app.schemas.recognition_schema import RecognitionResponse,HistoryResponse
from app.services.face_service import validate_image,image_quality,illumination
from app.services.embedding_service import extract_embedding,deserialize_embedding,cosine_similarity
from app.services.probability_service import predict
from app.core.config import FACE_THRESHOLD
router=APIRouter()
@router.post("/reconocimiento",response_model=RecognitionResponse)
async def reconocimiento(file:UploadFile=File(...),db:Session=Depends(get_db)):
    try:image=validate_image(await file.read());quality=image_quality(image);light=illumination(image);query=extract_embedding(image)
    except RuntimeError as e: raise HTTPException(503,str(e))
    except ValueError as e: raise HTTPException(400,str(e))
    best=None
    for row in db.query(FaceEmbedding).join(Persona).filter(Persona.activo==True).all():
        sim=cosine_similarity(query,deserialize_embedding(row.embedding))
        if best is None or sim>best[0]: best=(sim,row)
    if best is None:
        raise HTTPException(404,"No existen embeddings faciales registrados.")
    sim,row=best;distance=float(1-sim);coincide=sim>=FACE_THRESHOLD;persona=db.get(Persona,row.persona_id);prob=None
    try: prob=predict(type("V",(),{"similitud":sim,"distancia":distance,"calidad_imagen":quality,"iluminacion":light})())
    except Exception: pass
    log=RecognitionLog(persona_id=persona.id if coincide else None,similitud=sim,distancia=distance,umbral=FACE_THRESHOLD,coincide=coincide,probabilidad_calibrada=prob);db.add(log);db.commit()
    return {"success":True,"persona_id":persona.id if coincide else None,"nombre":persona.nombre if coincide else None,"similitud":sim,"distancia":distance,"umbral":FACE_THRESHOLD,"coincide":coincide,"probabilidad_calibrada":prob}
@router.get("/reconocimiento/historial",response_model=list[HistoryResponse])
def historial(db:Session=Depends(get_db)):
    rows=db.query(RecognitionLog,Persona.nombre).outerjoin(Persona,RecognitionLog.persona_id==Persona.id).order_by(RecognitionLog.created_at.desc()).all()
    return [{"id":r.id,"persona_id":r.persona_id,"nombre":name,"similitud":r.similitud,"distancia":r.distancia,"umbral":r.umbral,"coincide":r.coincide,"probabilidad_calibrada":r.probabilidad_calibrada,"created_at":r.created_at} for r,name in rows]
