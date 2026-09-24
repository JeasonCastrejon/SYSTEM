from datetime import datetime
from pydantic import BaseModel
class RecognitionResponse(BaseModel):
    success:bool=True
    persona_id:int|None
    nombre:str|None
    similitud:float
    distancia:float
    umbral:float
    coincide:bool
    probabilidad_calibrada:float|None
class ProbabilityInput(BaseModel):
    similitud:float
    distancia:float
    calidad_imagen:float
    iluminacion:float
class HistoryResponse(BaseModel):
    id:int; persona_id:int|None; nombre:str|None; similitud:float; distancia:float; umbral:float; coincide:bool; probabilidad_calibrada:float|None; created_at:datetime
