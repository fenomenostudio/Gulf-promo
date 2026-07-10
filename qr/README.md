# Código QR — "Gana con Gulf"

QR de la promo, apunta a **`https://ganacongulf.com`** (verificado por decodificación).

## Archivos

| Archivo | Uso |
|---|---|
| `ganacongulf-qr.svg` | **Imprenta / diseño.** Vector, escala infinita sin pixelarse. |
| `ganacongulf-qr.png` | Digital / preview alta resolución (~890 px). |
| `ganacongulf-qr-mini.png` | Control visual pequeño. |
| `generate_qr.py` | Script para regenerar (cambiar `URL` si cambia el destino). |

## Especificaciones técnicas

- **Corrección de error:** nivel H (30%) — resiste desgaste de impresión y superficies.
- **Zona de silencio:** 4 módulos (mínimo del estándar) — **no recortarla**.
- **Color:** navy Gulf `#002F6C` sobre blanco (máximo contraste). No invertir ni
  bajar el contraste; los lectores fallan con QR claro sobre oscuro.

## Reglas de impresión

- Tamaño mínimo recomendado: **2 x 2 cm** para material impreso cercano; más grande
  (≥ 5 cm) para afiches/vallas o lectura a distancia.
- Mantener margen blanco alrededor (la zona de silencio).
- Evitar poner el QR sobre fotos o texturas; usar fondo plano.
- Si se agrega el logo Gulf al centro, mantenerlo ≤ 25% del área (la corrección H
  lo tolera) y **volver a probar el escaneo** antes de imprimir en volumen.

## ⚠️ Antes de imprimir en volumen

1. La Fase 4 del RUNBOOK debe estar **verde** (`ganacongulf.com` resolviendo a Tally).
2. Escanear el QR con un teléfono real (iOS y Android) y confirmar que abre el
   formulario con SSL.

## Regenerar

```bash
cd qr
python3 generate_qr.py     # requiere: pip install segno
```
Si cambia la URL final (por ej. `www.ganacongulf.com`), editar la variable `URL`
en `generate_qr.py` y volver a correr.
