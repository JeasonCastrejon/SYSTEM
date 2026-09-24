from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import Base,engine
from app.models import Persona,FaceEmbedding,RecognitionLog,MLTrainingRecord
from app.core.config import CORS_ORIGINS
from app.api.routes import health,personas,recognition,probabilities,models,dashboard
Base.metadata.create_all(bind=engine)
app=FastAPI(title="FaceAI Intelligence API",version="1.0.0",description="API para reconocimiento facial, probabilidades calibradas y ML.")
app.add_middleware(CORSMiddleware,allow_origins=CORS_ORIGINS,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
app.include_router(health.router,prefix="/api")
app.include_router(dashboard.router,prefix="/api")
app.include_router(personas.router,prefix="/api")
app.include_router(recognition.router,prefix="/api")
app.include_router(probabilities.router,prefix="/api")
app.include_router(models.router,prefix="/api")
@app.get("/")
def root(): return {"message":"FaceAI Intelligence API","docs":"/docs"}
