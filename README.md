# Booze And Bites - Back en Flask

Este es un proyecto backend básico utilizando **Flask** y **GraphQL**, que simula una API para la gestión de productos. Puedes consultar y modificar productos con campos como nombre, precio, stock, y disponibilidad.

---
## Requisitos
- Python 3.10 o superior
- `virtualenv` o `venv` disponible
---
## Instalación y ejecución
1. **Clona el repositorio**
2. **Crea el entorno virtual**:

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
```

3. **Instala las dependencias**:

```bash
pip install -r requirements.txt
```

4. **Ejecuta el servidor Flask**:

```bash
python app.py
```

El servidor estará disponible en: [http://localhost:5000](http://localhost:5000)

---

## Pruebas

Este proyecto incluye pruebas unitarias para las consultas y mutaciones.

Para ejecutarlas:

```bash
pytest -v -s tests/
```

---
## Estructura del Proyecto

```
.
├── app.py                # Punto de entrada principal del servidor
├── schema.py             # Definición del esquema GraphQL
├── db/data.py            # Base de datos simulada de productos
├── resolvers/            # Mutaciones y queries GraphQL
├── models/product.py     # Modelo base del producto
├── tests/                # Pruebas unitarias con pytest
├── requirements.txt      # Dependencias
├── venv/                 # Entorno virtual local
└── README.md             # Este archivo
```
