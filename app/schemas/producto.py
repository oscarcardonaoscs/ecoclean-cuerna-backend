from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductoBase(BaseModel):
    nombre: str
    precio: float
    precioExpress: float  # Agregado el campo precioExpress
    tipo: str
    esActivo: bool = True  # Se asume que por defecto el producto es activo
    # La fecha de actualización (será generada automáticamente por la base de datos)
    fua: Optional[datetime] = None

    class Config:
        orm_mode = True


class ProductoCreate(ProductoBase):
    seccion_id: int  # Asegúrate de que el campo 'seccion_id' esté aquí.


class ProductoUpdate(ProductoBase):
    pass


class Producto(ProductoBase):
    id: int

    class Config:
        orm_mode = True
