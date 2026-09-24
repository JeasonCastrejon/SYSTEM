from datetime import datetime
from pydantic import BaseModel,EmailStr
class PersonaCreate(BaseModel):
    nombre:str
    email:EmailStr
class PersonaResponse(BaseModel):
    id:int; nombre:str; email:EmailStr; activo:bool; created_at:datetime
    class Config: from_attributes=True
