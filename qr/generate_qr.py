#!/usr/bin/env python3
"""
Generador del codigo QR de la promo "Gana con Gulf".

El QR apunta al dominio de la landing (Tally con dominio propio).
Se generan 3 variantes:
  1. ganacongulf-qr.svg      -> vector, ideal para imprenta (escala infinita)
  2. ganacongulf-qr.png      -> raster alta resolucion (para digital / preview)
  3. ganacongulf-qr-mini.png -> version pequena de control visual

Colores: navy Gulf sobre blanco = maximo contraste = maxima legibilidad al
escanear. NO se recomienda invertir (claro sobre oscuro) ni bajar contraste.

Nivel de correccion de error: H (30%). Aunque no lleve logo encima, deja margen
para desgaste de impresion / superficies curvas (ej. pega en surtidor).
"""
import segno

# --- Configuracion -----------------------------------------------------------
URL = "https://ganacongulf.com"      # destino final del QR (dominio propio Tally)
NAVY = "#002776"                      # Gulf Dark Blue oficial (Pantone 280 C, brand book)
LIGHT = "#FFFFFF"                     # fondo

# --- Generacion --------------------------------------------------------------
qr = segno.make(URL, error="h")

# SVG vectorial (el entregable bueno para imprenta)
qr.save(
    "ganacongulf-qr.svg",
    kind="svg",
    scale=10,
    border=4,          # quiet zone: 4 modulos (minimo recomendado por el estandar)
    dark=NAVY,
    light=LIGHT,
)

# PNG alta resolucion
qr.save(
    "ganacongulf-qr.png",
    kind="png",
    scale=24,          # ~ 1000+ px de lado
    border=4,
    dark=NAVY,
    light=LIGHT,
)

# PNG mini de control
qr.save(
    "ganacongulf-qr-mini.png",
    kind="png",
    scale=6,
    border=4,
    dark=NAVY,
    light=LIGHT,
)

print(f"QR generado -> {URL}")
print(f"Version/tamano de matriz: {qr.designator}")
