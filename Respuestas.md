## ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?
Dado lo que hemos visto en clase, entiendo que GraphQL permite hacer peticiones trayendo solo los datos que necesito en ese momento, lo cual lo hace más eficiente.
En este proyecto lo he comprobado: por ejemplo, cuando hago una mutación como modificarStock, solo recibo el id, stock y disponible del producto afectado. No necesito traer todo el objeto.
Además, como estoy usando tanto el backend como el frontend, he notado que tener ese control sobre la estructura de datos hace que el flujo entre ambos sea más claro y fácil de manejar, especialmente al trabajar con múltiples componentes.

## ¿Cómo se definen los tipos y resolvers en una API con GraphQL?
En mi caso, primero definí un tipo Producto en el esquema (schema.py) con sus campos: id, nombre, precio, stock, disponible, img, etc.
Luego creé resolvers dentro de las mutaciones (resolvers/mutations.py) y queries (resolvers/queries.py).
Por ejemplo, tengo un resolver llamado modificarStock, que recibe un id y una cantidad, y se encarga de actualizar el stock del producto en la base de datos simulada, y también calcula si disponible debe estar en true o false.
Eso me permite controlar toda la lógica desde el backend y evitar inconsistencias.

## ¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?
Porque si solo el frontend cambia el valor de disponible, entonces cualquier otro cliente que use esa API no va a saber si el producto está disponible o no.
Es más seguro que el backend sea quien lo controle, así la lógica queda centralizada y no depende del cliente. Además, si algún día cambiamos la lógica o usamos otra interfaz (como una app móvil), todo sigue funcionando igual.

## ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?
Ya lo implementé en el backend en el resolver modificarStock, cada vez que cambio el stock de un producto, también se evalúa si debe estar disponible o no.
En el frontend, después de hacer una compra o modificar el carrito, recibo del backend los valores actualizados de stock y disponible, y los reflejo directamente en la interfaz.
Eso evita que haya desincronización entre lo que ve el usuario y lo que realmente está ocurriendo en la lógica del sistema. Así los dos lados (backend y frontend) trabajan juntos de forma coherente.