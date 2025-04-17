from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

# Crear un producto


def create_producto(db: Session, producto: schemas.ProductoCreate):

    db_producto = models.Producto(
        nombre=producto.nombre,
        precio=producto.precio,
        precioExpress=producto.precioExpress,
        tipo=producto.tipo,
        esActivo=producto.esActivo,
        fua=datetime.utcnow(),  # Fecha de creación del producto
        seccion_id=producto.seccion_id,  # Suponiendo que el producto recibe la sección
    )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

# Obtener todos los productos


def get_productos(db: Session, skip: int = 0, limit: int = 100, seccion_id: int = None, activo: bool = None):
    query = db.query(models.Producto)

    if seccion_id:
        query = query.filter(models.Producto.seccion_id ==
                             seccion_id)  # Filtrar por seccion_id

    if activo is not None:
        query = query.filter(models.Producto.esActivo ==
                             activo)  # Filtrar por activo

    return query.offset(skip).limit(limit).all()

# Obtener un producto por ID


def get_producto(db: Session, producto_id: int):
    return db.query(models.Producto).filter(models.Producto.id == producto_id).first()

# Actualizar un producto


def update_producto(db: Session, producto_id: int, producto: schemas.ProductoUpdate):
    db_producto = db.query(models.Producto).filter(
        models.Producto.id == producto_id).first()
    if db_producto:
        for key, value in producto.dict(exclude_unset=True).items():
            setattr(db_producto, key, value)
        db.commit()
        db.refresh(db_producto)
        return db_producto
    return None

# Eliminar un producto


def delete_producto(db: Session, producto_id: int):
    db_producto = db.query(models.Producto).filter(
        models.Producto.id == producto_id).first()
    if db_producto:
        db.delete(db_producto)
        db.commit()
        return db_producto
    return None
