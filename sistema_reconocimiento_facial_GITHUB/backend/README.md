# Backend — FaceAI Intelligence

## Tecnologías
Python, FastAPI, Uvicorn, SQLite, SQLAlchemy, OpenCV, NumPy, InsightFace/ArcFace, ONNX Runtime y scikit-learn.

## Instalación en Windows
```powershell
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

La API queda en `http://127.0.0.1:8000` y la documentación en `/docs`.

## Base de datos
SQLite se crea automáticamente en:
`backend/data/reconocimiento_facial.db`

Tablas:
- personas
- face_embeddings
- recognition_logs
- ml_training_records

## Endpoints
- POST `/api/personas`
- GET `/api/personas`
- POST `/api/personas/{id}/rostro`
- POST `/api/reconocimiento`
- GET `/api/reconocimiento/historial`
- POST `/api/probabilidades/prediccion`
- POST `/api/modelos/entrenar`
- GET `/api/modelos/metricas`
- GET `/api/dashboard`
- GET `/api/health`

## Machine Learning
El entrenamiento usa los registros reales de `ml_training_records`. No se insertan datos de ejemplo automáticamente.

Para alimentar el dataset se deben registrar comparaciones reales/validadas con:
- similitud
- distancia
- calidad de imagen
- iluminación
- resultado real

El modelo implementado es Regresión Logística con calibración sigmoid. La arquitectura permite cambiarlo por Random Forest o Gradient Boosting.

## Deep Learning
La extracción facial usa InsightFace/ArcFace. En el primer uso, el paquete puede necesitar descargar sus modelos preentrenados. El proceso depende del hardware y de la instalación de ONNX Runtime.

## Seguridad
Los embeddings se almacenan en la base de datos como información interna y no se devuelven al frontend. Para producción se debe añadir autenticación, autorización por roles, HTTPS, auditoría completa, políticas de retención y controles de privacidad/consentimiento.

## Nota
El sistema está preparado para desarrollo académico/local. Antes de producción deben completarse autenticación, gestión de usuarios, despliegue seguro y revisión legal aplicable.
