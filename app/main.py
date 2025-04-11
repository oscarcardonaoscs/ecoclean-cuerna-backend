from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD para productos


@app.post("/productos/", response_model=schemas.Producto)
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.create_producto(db=db, producto=producto)


@app.get("/productos/", response_model=list[schemas.Producto])
def get_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_productos(db=db, skip=skip, limit=limit)


@app.get("/productos/{producto_id}", response_model=schemas.Producto)
def get_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.get_producto(db=db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto


@app.put("/productos/{producto_id}", response_model=schemas.Producto)
def update_producto(producto_id: int, producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = crud.update_producto(
        db=db, producto_id=producto_id, producto=producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto


@app.delete("/productos/{producto_id}", response_model=schemas.Producto)
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.delete_producto(db=db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

# CRUD para secciones


@app.post("/secciones/", response_model=schemas.Seccion)
def create_seccion(seccion: schemas.SeccionCreate, db: Session = Depends(get_db)):
    return crud.create_seccion(db=db, seccion=seccion)


@app.get("/secciones/", response_model=list[schemas.Seccion])
def get_secciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_secciones(db=db, skip=skip, limit=limit)


@app.get("/secciones/{seccion_id}", response_model=schemas.Seccion)
def get_seccion(seccion_id: int, db: Session = Depends(get_db)):
    db_seccion = crud.get_seccion(db=db, seccion_id=seccion_id)
    if db_seccion is None:
        raise HTTPException(status_code=404, detail="Sección no encontrada")
    return db_seccion


@app.put("/secciones/{seccion_id}", response_model=schemas.Seccion)
def update_seccion(seccion_id: int, seccion: schemas.SeccionCreate, db: Session = Depends(get_db)):
    db_seccion = crud.update_seccion(
        db=db, seccion_id=seccion_id, seccion=seccion)
    if db_seccion is None:
        raise HTTPException(status_code=404, detail="Sección no encontrada")
    return db_seccion


@app.delete("/secciones/{seccion_id}", response_model=schemas.Seccion)
def delete_seccion(seccion_id: int, db: Session = Depends(get_db)):
    db_seccion = crud.delete_seccion(db=db, seccion_id=seccion_id)
    if db_seccion is None:
        raise HTTPException(status_code=404, detail="Sección no encontrada")
    return db_seccion
