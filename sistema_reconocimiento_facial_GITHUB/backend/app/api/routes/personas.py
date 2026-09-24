from fastapi import APIRouter,Depends,File,UploadFile,HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models import Persona,FaceEmbedding
from app.schemas.persona_schema import PersonaCreate,PersonaResponse
from app.services.face_service import validate_image
from app.services.embedding_service import extract_embedding,serialize_embedding
from app.core.config import MODEL_NAME
router=APIRouter()
@router.post("/personas",response_model=PersonaResponse)
def crear_persona(payload:PersonaCreate,db:Session=Depends(get_db)):
    p=Persona(nombre=payload.nombre.strip(),email=str(payload.email).lower());db.add(p);db.commit();db.refresh(p);return p
@router.get("/personas",response_model=list[PersonaResponse])
def listar_personas(db:Session=Depends(get_db)): return db.query(Persona).filter(Persona.activo==True).order_by(Persona.id.desc()).all()
@router.post("/personas/{persona_id}/rostro")
async def guardar_rostro(persona_id:int,file:UploadFile=File(...),db:Session=Depends(get_db)):
    p=db.get(Persona,persona_id)
    if not p: raise HTTPException(404,"Persona no encontrada.")
    try:
        image=validate_image(await file.read());emb=extract_embedding(image)
    except RuntimeError as e: raise HTTPException(503,str(e))
    except ValueError as e: raise HTTPException(400,str(e))
    db.add(FaceEmbedding(persona_id=p.id,embedding=serialize_embedding(emb),modelo=MODEL_NAME));db.commit()
    return {"success":True,"persona_id":p.id,"modelo":MODEL_NAME}
