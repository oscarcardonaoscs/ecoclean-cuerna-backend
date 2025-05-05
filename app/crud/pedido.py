from sqlalchemy.orm import Session
from datetime import datetime
from app.models.pedido import Pedido
from app.models.partida_pedido import PartidaPedido
from app.models.pago import Pago
from app import schemas


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
