from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from app.schemas.partida_pedido import PartidaPedidoCreate, PartidaPedidoOut
from app.schemas.pago import PagoCreate, PagoOut


class PedidoBase(BaseModel):
    cliente_id: int
    fecha_entrega: datetime
    subtotal: float
    descuento: float = 0
    envio: float = 0
    iva: float
    total: float
    forma_pago: str
    estatus: Optional[str] = "Pendiente"
    estatus_pago: str = "Pendiente"
    es_express: Optional[bool] = False
    notas: Optional[str] = None


class PedidoCreate(PedidoBase):
    partidas: List[PartidaPedidoCreate]
    pagos: List[PagoCreate]


class PedidoOut(PedidoBase):
    id: int
    folio: str
    fecha_creacion: datetime
    fua: datetime
    saldo: float
    partidas: List[PartidaPedidoOut]
    pagos: List[PagoOut]

    class Config:
        orm_mode = True
