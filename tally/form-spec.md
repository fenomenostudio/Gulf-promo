# Especificación del formulario — Gulf (promo "Motopóker")

> Basado en el formulario **original del cliente** ("GULF- Motopocker", Google Forms).
> Creamos uno **nuevo** en Tally (branded) replicando estos campos — no se toca el del cliente.
> Fuente: https://forms.gle/GBq7F7KorrqSEjZF6

## Campos (los 6 del cliente)

| # | Campo (label exacto) | Tipo en Tally | Requerido | Notas |
|---|---|---|---|---|
| 1 | Nombre y Apellido | Short text | Sí | — |
| 2 | Número de celular | **Phone number** | Sí | En Tally usar tipo teléfono (valida formato). El cliente lo tenía como texto simple. |
| 3 | Correo | **Email** | Sí | En Tally usar tipo email (valida formato). El cliente lo tenía como texto simple. |
| 4 | Maneja vehículo pesado o liviano? | Multiple choice | Sí | Opciones: **Liviano**, **Pesado** |
| 5 | Que viscosidad utilizas? | Short text | Sí | Se puede mejorar a **Dropdown** con viscosidades comunes (20W-50, 15W-40, 10W-30, 5W-30, "No sé / otra"). Confirmar con Gulf. |
| 6 | Cual es el nombre de tu empresa o lugar de trabajo? | Short text | Sí | — |

> **Nota sobre "Requerido":** el Google Form del cliente no marcaba obligatoriedad.
> Para una promo conviene que 1–4 y 6 sean requeridos (datos de contacto y
> segmentación). Confirmar cuáles quiere Gulf obligatorios.

## Mejoras respecto al form original (opcionales, a confirmar con Gulf)
- **Teléfono y correo con validación** nativa de Tally (menos datos basura).
- **Viscosidad como dropdown** en vez de texto libre (respuestas consistentes → mejor data).
- **Términos y condiciones + aviso de privacidad**: el form original no los tenía. Si
  la promo entrega premio, es recomendable agregar un checkbox de aceptación de T&C
  (requerido) y, aparte, un opt-in opcional de marketing. **Legal de Gulf decide.**

## Comportamiento
- **Una sola página** (form corto = más conversión desde el QR).
- Botón de envío branded (ej. **"¡Participar!"**).
- **Página de gracias** con marca Gulf: "🎉 ¡Gracias por participar!".
- Branding (logo, colores, CSS) → ver `../brand/brand.md` y `custom-css.css`.

## Integración
- **Google Sheets** (nativa): hoja **"Gulf Motopóker — Respuestas"** con columnas
  que calzan a estos campos. Ver Fase 5 del RUNBOOK.
- Tally agrega **timestamp** automático por envío.

## Columnas de la Google Sheet (orden)
`Marca temporal` · `Nombre y Apellido` · `Número de celular` · `Correo` ·
`Tipo de vehículo` · `Viscosidad` · `Empresa o lugar de trabajo`
