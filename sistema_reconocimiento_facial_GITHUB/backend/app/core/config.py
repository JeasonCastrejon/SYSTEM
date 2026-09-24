import os
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parents[2]
DATA_DIR=BASE_DIR/"data"; MODELS_DIR=BASE_DIR/"models"
DATA_DIR.mkdir(exist_ok=True); MODELS_DIR.mkdir(exist_ok=True)
DATABASE_URL=os.getenv("DATABASE_URL",f"sqlite:///{DATA_DIR/'reconocimiento_facial.db'}")
CORS_ORIGINS=os.getenv("CORS_ORIGINS","http://localhost:5173").split(",")
FACE_THRESHOLD=float(os.getenv("FACE_THRESHOLD","0.75"))
MODEL_NAME=os.getenv("MODEL_NAME","ArcFace")
ML_MODEL_PATH=MODELS_DIR/"probability_model.joblib"
