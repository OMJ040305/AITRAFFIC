# AITRAFFIC

AITRAFFIC es un proyecto de detección de vehículos en video utilizando el modelo preentrenado YOLOv5 y OpenCV. El objetivo es identificar vehículos dentro de dos zonas definidas (una principal y una para flechas), mostrando el conteo en tiempo real y destacando las detecciones en el video.

## Requisitos

- Python 3.7 o superior
- [PyTorch](https://pytorch.org/) (incluye el soporte para YOLOv5)
- OpenCV
- Numpy
- Matplotlib

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/OMJ040305/AITRAFFIC.git

    Instala las dependencias:

pip install -r requirements.txt

Si aún no tienes el archivo requirements.txt, puedes crear uno con las dependencias principales:

    opencv-python
    torch
    numpy
    matplotlib

Uso

    Coloca tu video en la carpeta data/ con el nombre video.mp4 o cambia el nombre en el código.

    Ejecuta el script:

    python main.py

    El programa iniciará el procesamiento del video, detectando vehículos en tiempo real.

    El conteo de vehículos dentro de las zonas de interés se mostrará en la pantalla mientras se visualiza el video.

Estructura del proyecto

AITRAFFIC/
├── data/
│   └── video.mp4       # Video para procesar (debe estar en esta carpeta)
├── main.py             # Código principal para la detección
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Este archivo

Cómo funciona

    El modelo YOLOv5 preentrenado se carga y se usa para realizar predicciones sobre cada frame del video.

    Los vehículos detectados se filtran con un umbral de confianza del 40% y se dibujan en el video.

    Se valida si las detecciones caen dentro de dos zonas definidas:

        ZONAPRINCIPAL: La zona principal donde se cuenta el número de vehículos.

        ZONAFLECHA: Otra zona que también se monitorea.

El número total de vehículos en cada zona se muestra en la pantalla del video.
Contribuciones

Si deseas contribuir a este proyecto, puedes hacer un fork y crear un pull request con tus mejoras.
