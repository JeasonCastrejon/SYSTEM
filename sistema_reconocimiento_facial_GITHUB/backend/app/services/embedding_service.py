import json, numpy as np
try:
    from insightface.app import FaceAnalysis
except Exception:
    FaceAnalysis=None
_app=None
def get_app():
    global _app
    if FaceAnalysis is None:
        raise RuntimeError("InsightFace/ONNX Runtime no está instalado correctamente.")
    if _app is None:
        _app=FaceAnalysis(name="buffalo_l",providers=["CPUExecutionProvider"])
        _app.prepare(ctx_id=0,det_size=(640,640))
    return _app
def extract_embedding(image):
    app=get_app()
    faces=app.get(image)
    if not faces: raise ValueError("No se detectó ningún rostro.")
    if len(faces)>1: raise ValueError("La imagen debe contener un solo rostro.")
    face=faces[0]
    emb=np.asarray(face.embedding,dtype=np.float32)
    norm=np.linalg.norm(emb)
    if norm==0: raise ValueError("No se pudo generar un embedding válido.")
    return emb/norm
def serialize_embedding(emb): return json.dumps(np.asarray(emb,dtype=float).tolist())
def deserialize_embedding(value): return np.asarray(json.loads(value),dtype=np.float32)
def cosine_similarity(a,b):
    a=np.asarray(a);b=np.asarray(b)
    den=np.linalg.norm(a)*np.linalg.norm(b)
    return float(np.dot(a,b)/den) if den else 0.0
