from pydantic import BaseModel
from typing import Optional


class ProductoBase(BaseModel):
    nombre: str
    precio: float

    class Config:
        orm_mode = True


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(ProductoBase):
    pass


class Producto(ProductoBase):
    id: int

    class Config:
        orm_mode = True
