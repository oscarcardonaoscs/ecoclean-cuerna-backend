from sqlalchemy.orm import Session
from app import models, schemas

# Crear dirección


def create_direccion(db: Session, direccion: schemas.DireccionCreate, cliente_id: int):
    db_direccion = models.Direccion(cliente_id=cliente_id, **direccion.dict())
    db.add(db_direccion)
    db.commit()
    db.refresh(db_direccion)
    return db_direccion

# Obtener direcciones de un cliente


def get_direcciones(db: Session, cliente_id: int):
    return db.query(models.Direccion).filter(models.Direccion.cliente_id == cliente_id).all()

# Obtener una dirección específica


def get_direccion(db: Session, direccion_id: int):
    return db.query(models.Direccion).filter(models.Direccion.id == direccion_id).first()

# Actualizar dirección


def update_direccion(db: Session, direccion_id: int, direccion: schemas.DireccionCreate):
    db_direccion = db.query(models.Direccion).filter(
        models.Direccion.id == direccion_id).first()
    if db_direccion:
        for key, value in direccion.dict().items():
            setattr(db_direccion, key, value)
        db.commit()
        db.refresh(db_direccion)
        return db_direccion
    return None

# Eliminar dirección


def delete_direccion(db: Session, direccion_id: int):
    db_direccion = db.query(models.Direccion).filter(
        models.Direccion.id == direccion_id).first()
    if db_direccion:
        db.delete(db_direccion)
        db.commit()
        return db_direccion
    return None
