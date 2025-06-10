from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, SessionLocal
from app import models
from app.core.config import settings
from app.routers import productos, secciones, clientes, direcciones, pedidos, pagos


# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

# Crear instancia de FastAPI
app = FastAPI(title="EcoClean API")

# Configuración de CORS
origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Puedes usar ["*"] durante desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir los routers de los diferentes módulos
app.include_router(productos.router, prefix="/productos")
app.include_router(secciones.router, prefix="/secciones")
app.include_router(clientes.router, prefix="/clientes")
app.include_router(direcciones.router, prefix="/direcciones")
app.include_router(pedidos.router, prefix="/pedidos")
app.include_router(pagos.router, prefix="/pagos")
