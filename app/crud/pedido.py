from sqlalchemy.orm import Session
from datetime import datetime
from decimal import Decimal
from app.models.pedido import Pedido
from app.models.partida_pedido import PartidaPedido
from app.models.pedido_status_history import PedidoStatusHistory
from app.models.pago import Pago
from app import schemas
from sqlalchemy.orm import selectinload


def generar_folio(db: Session) -> str:
    """Genera un folio basado en el año y el ID del último pedido."""
    year = datetime.utcnow().year
    last_pedido = db.query(Pedido).order_by(Pedido.id.desc()).first()
    next_id = 1 if not last_pedido else last_pedido.id + 1
    return f"{year}{str(next_id).zfill(5)}"  # Ejemplo: 202500001


def crear_pedido(db: Session, pedido: schemas.PedidoCreate):
    """Crea un pedido junto con sus partidas y pagos."""

    # Generar el folio automático
    folio = generar_folio(db)

    # Calcular total pagado y saldo
    monto_total_pagado = sum(p.monto_pagado for p in pedido.pagos)
    saldo = pedido.total - monto_total_pagado

    # Determinar estatus de pago
    if monto_total_pagado >= pedido.total:
        estatus_pago = "Pagado"
    elif monto_total_pagado > 0:
        estatus_pago = "Parcial"
    else:
        estatus_pago = "Pendiente"

    # Crear el objeto Pedido
    db_pedido = Pedido(
        folio=folio,
        cliente_id=pedido.cliente_id,
        fecha_entrega=pedido.fecha_entrega,
        fecha_creacion=datetime.utcnow(),  # Fecha de creación del pedido
        subtotal=pedido.subtotal,
        descuento=pedido.descuento,
        envio=pedido.envio,
        iva=pedido.iva,
        total=pedido.total,
        forma_pago=pedido.forma_pago,
        estatus=pedido.estatus,
        estatus_pago=estatus_pago,
        es_express=pedido.es_express,
        notas=pedido.notas,
        saldo=saldo,
    )

    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)  # Para tener el ID generado

    # Crear partidas
    for partida in pedido.partidas:
        db_partida = PartidaPedido(
            pedido_id=db_pedido.id,
            producto_id=partida.producto_id,
            cantidad=partida.cantidad,
            precio_unitario=partida.precio_unitario,
            importe=partida.importe,
            notas=partida.notas,
        )
        db.add(db_partida)

    # Crear pagos
    for pago in pedido.pagos:
        db_pago = Pago(
            pedido_id=db_pedido.id,
            forma_pago=pago.forma_pago,
            monto_pagado=pago.monto_pagado,
            monto_recibido=pago.monto_recibido,
            monto_cambio=pago.monto_cambio,
            fecha_pago=pago.fecha_pago or datetime.utcnow(),
            referencia_pago=pago.referencia_pago,
        )
        db.add(db_pago)

    db.commit()
    return db_pedido


def obtener_todos_los_pedidos(db: Session):
    """Obtiene todos los pedidos."""
    return db.query(Pedido).all()


def obtener_pedidos_por_estatus(db: Session, estatus: str):
    """Obtiene los pedidos filtrados por estatus."""
    return (
        db.query(Pedido)
        .options(selectinload(Pedido.cliente))  # Carga el cliente
        .filter(Pedido.estatus == estatus)
        .all()
    )


def obtener_pedido_por_id(db: Session, pedido_id: int) -> Pedido:
    """Devuelve un pedido por su ID o None si no existe."""
    return db.query(Pedido).filter(Pedido.id == pedido_id).first()


def cancelar_pedido(db: Session, pedido: Pedido) -> Pedido:
    """
    Marca un pedido como cancelado y pone su total en 0.00.
    Luego hace commit y refresh para devolver la entidad actualizada.
    """
    pedido.estatus = "Cancelado"
    pedido.total = Decimal("0.00")
    db.commit()
    db.refresh(pedido)
    return pedido


def actualizar_estatus_pedido(
    db: Session, pedido_id: int, nuevo_estatus: str
) -> Pedido:
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        return None

    antiguo = pedido.estatus
    pedido.estatus = nuevo_estatus
    db.add(pedido)

    # Registrar historial
    hist = PedidoStatusHistory(
        pedido_id=pedido_id,
        estatus_anterior=antiguo,
        estatus_nuevo=nuevo_estatus
    )
    db.add(hist)

    db.commit()
    db.refresh(pedido)
    return pedido
