from pathlib import Path
import joblib, numpy as np
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score,recall_score,f1_score,confusion_matrix
from app.core.config import ML_MODEL_PATH
def load_model():
    return joblib.load(ML_MODEL_PATH) if Path(ML_MODEL_PATH).exists() else None
def train(rows):
    if len(rows)<10: raise ValueError("Se necesitan al menos 10 registros validados para entrenar el modelo.")
    X=np.array([[r.similitud,r.distancia,r.calidad_imagen,r.iluminacion] for r in rows],dtype=float)
    y=np.array([int(r.resultado_real) for r in rows],dtype=int)
    if len(set(y.tolist()))<2: raise ValueError("El dataset debe contener resultados positivos y negativos.")
    base=LogisticRegression(max_iter=1000)
    model=Pipeline([("scaler",StandardScaler()),("calibrated",CalibratedClassifierCV(base,method="sigmoid",cv=3))])
    model.fit(X,y)
    joblib.dump(model,ML_MODEL_PATH)
    pred=model.predict(X)
    cm=confusion_matrix(y,pred,labels=[0,1])
    tn,fp,fn,tp=cm.ravel()
    metrics={"precision":float(precision_score(y,pred,zero_division=0)),"recall":float(recall_score(y,pred,zero_division=0)),"f1":float(f1_score(y,pred,zero_division=0)),"false_positive_rate":float(fp/(fp+tn)) if fp+tn else 0.0,"false_negative_rate":float(fn/(fn+tp)) if fn+tp else 0.0,"confusion_matrix":cm.tolist(),"modelo":"Regresión Logística calibrada","muestras":len(rows)}
    return metrics
def predict(values):
    model=load_model()
    if model is None: raise FileNotFoundError("Todavía no existe un modelo ML entrenado.")
    X=np.array([[values.similitud,values.distancia,values.calidad_imagen,values.iluminacion]],dtype=float)
    return float(model.predict_proba(X)[0,1])
