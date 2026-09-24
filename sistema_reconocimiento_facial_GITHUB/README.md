# SISTEMA INTELIGENTE DE RECONOCIMIENTO FACIAL

Proyecto completo:
- frontend: React + Vite + TypeScript + Tailwind CSS + Axios + Recharts
- backend: Python + FastAPI + SQLAlchemy + SQLite
- visión artificial: OpenCV + NumPy
- Deep Learning: InsightFace/ArcFace + ONNX Runtime
- Machine Learning: scikit-learn
- sin PostgreSQL

## Módulos
1. Dashboard
2. Registro facial
3. Reconocimiento
4. Probabilidades
5. Historial
6. Entrenamiento ML
7. Usuarios y seguridad

## Ejecución

### Backend
```powershell
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
En otra terminal:
```powershell
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:5173
Backend: http://127.0.0.1:8000
Swagger: http://127.0.0.1:8000/docs

## Flujo
React → Axios/REST → FastAPI → OpenCV → InsightFace/ArcFace → embeddings → comparación → umbral → historial → ML calibrado.

## Importante
No contiene personas, reconocimientos, probabilidades ni métricas ficticias. Los resultados dependen de datos reales y del backend.

El reconocimiento facial utiliza datos biométricos. Para un uso real deben implementarse consentimiento, control de acceso, HTTPS, auditoría, políticas de retención y las obligaciones legales aplicables.
