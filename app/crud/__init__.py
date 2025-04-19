from .producto import (
    create_producto,
    get_productos,
    get_producto,
    update_producto,
    delete_producto
)

from .seccion import (
    create_seccion,
    get_secciones,
    get_seccion,
    update_seccion,
    delete_seccion
)

# Agregando las importaciones para cliente
from .cliente import (
    create_cliente,
    get_clientes,
    get_cliente,
    update_cliente,
    delete_cliente
)

# Agregando las importaciones para direccion
from .direccion import (
    create_direccion,
    get_direcciones,
    get_direccion,
    update_direccion,
    delete_direccion
)
