from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Asegúrate de importar DireccionCreate desde el archivo de esquemas donde lo tengas definido
# Importando DireccionCreate desde su archivo correspondiente
from .direccion import DireccionCreate


class ClienteCreate(BaseModel):
    nombre: str
    razon_social: Optional[str] = None
    rfc: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    notas: Optional[str] = None
    tipo_pago: Optional[str] = None
    es_habilitado: bool = True
    fua: Optional[datetime] = None

    class Config:
        orm_mode = True


class ClienteResponse(ClienteCreate):
    id: int
    direcciones: List[DireccionCreate] = []  # List of DireccionCreate models
