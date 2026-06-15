# Gestión de Datos de Países

Sistema en Python que permite gestionar una lista de países desde un archivo CSV. Ofrece operaciones de alta, actualización, búsqueda, filtrado, ordenamiento y estadísticas, todo desde un menú interactivo en consola.

## Integrantes

- Alexis Leonel Ortiz
- Lautaro Nicolas Palenzuela

## Requisitos

- Python 3.x
- No requiere bibliotecas externas (solo la biblioteca estándar).

## Instalación y ejecución

1. Clonar este repositorio o descargar los archivos en una misma carpeta.
2. Asegurarse de que el archivo `paises.csv` (con los datos iniciales) esté en la misma carpeta que `gestion_paises.py`.
3. Abrir una terminal en esa carpeta y ejecutar:


```bash
python gestion_paises.py

```

## Uso del programa
Al ejecutar, aparecerá un menú con las siguientes opciones:

    1. Agregar país – Ingresar nombre, población, superficie y continente.

    2. Actualizar país – Modificar población y/o superficie de un país existente.

    3. Buscar país – Coincidencia parcial del nombre (no distingue mayúsculas).

    4. Filtrar por continente – Mostrar países de un continente específico.

    5. Filtrar por rango de población – Especificar mínimo y máximo (opcionales).

    6. Filtrar por rango de superficie – Similar al anterior.

    7. Ordenar países – Por nombre, población o superficie, ascendente o descendente (ordenamiento manual tipo burbuja).

    8. Estadísticas – Muestra: país con mayor/menor población, promedios de población y superficie, y cantidad de países por continente.

    9. Guardar y salir – Persiste los cambios en paises.csv y termina el programa.


## Ejemplo de entrada/salida
Agregar un país:

    Nombre: Uruguay
    Población: 3500000
    Superficie: 176215
    Continente: América
    País agregado
   

Filtrar por continente (América):

    Continente: América
    - Argentina | Población: 45376763 | Superficie: 2780400 | Continente: América
    - Brasil | Población: 213993437 | Superficie: 8515767 | Continente: América
    - Uruguay | Población: 3500000 | Superficie: 176215 | Continente: América


## Documentación adicional
Informe técnico en PDF: [pendiente]

Video demostrativo: [pendiente]


## Notas importantes
- Los datos solo se guardan en el archivo CSV al elegir la opción 9. Si se cierra el programa de otra forma, los cambios se pierden.

- Si el archivo paises.csv no existe al inicio, el programa arranca con una lista vacía y lo creará automáticamente al guardar.

- Todas las entradas numéricas (población, superficie, rangos) están validadas para evitar errores de tipo.

- El ordenamiento se implementó manualmente (algoritmo de burbuja) para cumplir con el requisito académico.


## Licencia
Trabajo práctico con fines educativos – UTN.
