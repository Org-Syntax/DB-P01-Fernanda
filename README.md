# Proyecto de suma en Python

Ejemplo pequeño de una función para sumar dos números, con pruebas automatizadas usando la biblioteca estándar de Python.

## Requisitos

- Python 3.10 o posterior

No se necesitan paquetes externos.

## Ejecutar el programa

Desde la carpeta raíz del repositorio:

```powershell
python src/suma.py
```

## Abrir la página

Abre `web/index.html` en el navegador. Ingresa los dos números y selecciona **Sumar** para ver el resultado.

## Ejecutar las pruebas

```powershell
python -m unittest discover -s tests -v
```

GitHub Actions muestra el resultado del programa y ejecuta estas pruebas en cada `push` y `pull request`.