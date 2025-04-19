from pydantic import BaseModel
from typing import Optional


class DireccionCreate(BaseModel):
    calle: Optional[str] = None
    numero_exterior: Optional[str] = None
    numero_interior: Optional[str] = None
    colonia: Optional[str] = None
    municipio: Optional[str] = None
    estado: Optional[str] = None
    codigo_postal: Optional[str] = None
    pais: Optional[str] = None

    class Config:
        orm_mode = True


class DireccionResponse(DireccionCreate):
    id: int
    cliente_id: int  # ID del cliente al que pertenece la dirección
