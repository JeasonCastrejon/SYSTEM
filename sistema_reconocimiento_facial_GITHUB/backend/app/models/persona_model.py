from datetime import datetime
from sqlalchemy import Boolean,Column,DateTime,Integer,String,Text,ForeignKey,Float
from sqlalchemy.orm import relationship
from app.database.connection import Base
class Persona(Base):
    __tablename__="personas"
    id=Column(Integer,primary_key=True,index=True)
    nombre=Column(String(150),nullable=False,index=True)
    email=Column(String(200),nullable=False,index=True)
    activo=Column(Boolean,default=True,index=True)
    created_at=Column(DateTime,default=datetime.utcnow,nullable=False)
    embeddings=relationship("FaceEmbedding",back_populates="persona",cascade="all, delete-orphan")
class FaceEmbedding(Base):
    __tablename__="face_embeddings"
    id=Column(Integer,primary_key=True,index=True)
    persona_id=Column(Integer,ForeignKey("personas.id",ondelete="CASCADE"),nullable=False,index=True)
    embedding=Column(Text,nullable=False)
    modelo=Column(String(100),nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow,nullable=False)
    persona=relationship("Persona",back_populates="embeddings")
class RecognitionLog(Base):
    __tablename__="recognition_logs"
    id=Column(Integer,primary_key=True,index=True)
    persona_id=Column(Integer,ForeignKey("personas.id",ondelete="SET NULL"),nullable=True,index=True)
    similitud=Column(Float,nullable=False)
    distancia=Column(Float,nullable=False)
    umbral=Column(Float,nullable=False)
    coincide=Column(Boolean,nullable=False,index=True)
    probabilidad_calibrada=Column(Float,nullable=True)
    created_at=Column(DateTime,default=datetime.utcnow,nullable=False,index=True)
class MLTrainingRecord(Base):
    __tablename__="ml_training_records"
    id=Column(Integer,primary_key=True,index=True)
    similitud=Column(Float,nullable=False)
    calidad_imagen=Column(Float,nullable=False)
    iluminacion=Column(Float,nullable=False)
    resultado_real=Column(Boolean,nullable=False,index=True)
    distancia=Column(Float,nullable=True)
    created_at=Column(DateTime,default=datetime.utcnow,nullable=False)
