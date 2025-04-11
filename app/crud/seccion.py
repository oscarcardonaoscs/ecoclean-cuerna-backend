from sqlalchemy.orm import Session
from app import models, schemas

# Crear una sección


def create_seccion(db: Session, seccion: schemas.SeccionCreate):
    db_seccion = models.Seccion(**seccion.dict())
    db.add(db_seccion)
    db.commit()
    db.refresh(db_seccion)
    return db_seccion

# Obtener todas las secciones


def get_secciones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Seccion).offset(skip).limit(limit).all()

# Obtener una sección por ID


def get_seccion(db: Session, seccion_id: int):
    return db.query(models.Seccion).filter(models.Seccion.id == seccion_id).first()

# Actualizar una sección


def update_seccion(db: Session, seccion_id: int, seccion: schemas.SeccionUpdate):
    db_seccion = db.query(models.Seccion).filter(
        models.Seccion.id == seccion_id).first()
    if db_seccion:
        for key, value in seccion.dict(exclude_unset=True).items():
            setattr(db_seccion, key, value)
        db.commit()
        db.refresh(db_seccion)
        return db_seccion
    return None

# Eliminar una sección


def delete_seccion(db: Session, seccion_id: int):
    db_seccion = db.query(models.Seccion).filter(
        models.Seccion.id == seccion_id).first()
    if db_seccion:
        db.delete(db_seccion)
        db.commit()
        return db_seccion
    return None
