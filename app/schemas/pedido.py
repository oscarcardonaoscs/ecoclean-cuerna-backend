from typing import List, Optional, Literal
from datetime import datetime
from pydantic import BaseModel
from app.schemas.partida_pedido import PartidaPedidoCreate, PartidaPedidoOut
from app.schemas.pago import PagoCreate, PagoOut
from .cliente import ClienteSimple


class PedidoStatusUpdate(BaseModel):
    estatus: Literal[
        "Pendiente",
        "En Proceso",
        "Por Entregar",
        "Por Recoger",
        "Entregado",
        "Enviado",
        "Cancelado"
    ]


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
    cliente: ClienteSimple

    class Config:
        orm_mode = True


class PedidoStatusHistoryOut(BaseModel):
    id: int
    pedido_id: int
    estatus_anterior: str
    estatus_nuevo: str
    creado_en: datetime

    # Pydantic v2: para permitir lectura desde atributos de SQLAlchemy
    model_config = {
        "from_attributes": True
    }
