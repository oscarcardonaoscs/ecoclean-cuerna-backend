from typing import Optional
from pydantic import BaseModel
from .producto import Producto


class PartidaPedidoBase(BaseModel):
    producto_id: int
    cantidad: int
    precio_unitario: float
    importe: float
    notas: Optional[str] = None


class PartidaPedidoCreate(PartidaPedidoBase):
    pass


class PartidaPedidoOut(PartidaPedidoBase):

    id: int
    pedido_id: int
    producto: Producto

    class Config:
        orm_mode = True
