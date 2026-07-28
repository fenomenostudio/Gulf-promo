# Especificación del formulario — "Gana con Gulf"

> Basado en el formulario **original del cliente** (Google Forms). Creamos uno
> **nuevo** en Tally (branded) replicando estos campos — no se toca el del cliente.
> Nombre de la promo: **Gana con Gulf**. Fuente: https://forms.gle/GBq7F7KorrqSEjZF6

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

## Términos y condiciones — cómo implementarlos en Tally

Limitaciones verificadas de Tally:
- El **code injection es solo CSS** (no HTML ni JS) → **no se puede hacer un popup/modal propio**.
- **No existe bloque acordeón/desplegable** para el visitante (el "fold" del editor es
  solo para ordenar la vista mientras se construye).
- ⚠️ **No poner los T&C después del botón de envío**: eso es la página de gracias, o
  sea que la persona ya aceptó sin poder leerlos. El consentimiento debe ser informado
  **antes** de marcar "acepto".

Dos rutas válidas (se pueden combinar):

**A. Acordeón con lógica condicional** (lo más cercano a un popup, sin navegar)
1. Checkbox **no requerido**: "📄 Ver términos y condiciones".
2. Debajo, bloque de texto con los T&C completos.
3. La lógica **no es un ícono de la barra superior**: es un bloque. Con el cursor debajo
   del checkbox, escribir **`/logic`** (atajo **⌘/Ctrl + Shift + L**) y configurar:
   *When "Ver términos y condiciones" is checked → Show → [bloque de texto].*
   Si el texto aparece por defecto, ocultar ese bloque con **Hide (⌘⇧H)** desde su menú.
4. Después, el checkbox **requerido**: "Acepto los términos y condiciones".

**B. Página propia en el dominio** (requiere Pro, ya activo) — **ruta elegida**
- Crear un segundo form de solo texto con los T&C y mapearlo a
  `ganacongulf.com/terminos` (Domains → Map form → slug `terminos`).
- En el form principal, enlazarlo abriendo en **pestaña nueva**: la persona no pierde
  lo que llevaba lleno y sigue dentro del dominio de la promo.
- Tally siempre renderiza un botón de envío, incluso en una página de solo texto.
  Ocultarlo inyectando `terminos-ocultar-boton.css` **solo en ese formulario**
  (Settings → Code injection → CSS). No usar "Redirect on completion" con un botón
  visible: cada clic registraría una respuesta vacía y ensuciaría los datos.

**Separar siempre** el consentimiento de participación (requerido) del opt-in de
marketing (opcional). El **contenido legal lo define Gulf**, no la agencia.

## Comportamiento
- **Una sola página** (form corto = más conversión desde el QR).
- Botón de envío branded (ej. **"¡Participar!"**).
- **Página de gracias** con marca Gulf: "🎉 ¡Gracias por participar!".
- Branding (logo, colores, CSS) → ver `../brand/brand.md` y `custom-css.css`.

## Integración
- **Google Sheets** (nativa): hoja **"Gana con Gulf — Respuestas"** con columnas
  que calzan a estos campos. Ver Fase 5 del RUNBOOK.
- Tally agrega **timestamp** automático por envío.

## Columnas de la Google Sheet (orden)
`Marca temporal` · `Nombre y Apellido` · `Número de celular` · `Correo` ·
`Tipo de vehículo` · `Viscosidad` · `Empresa o lugar de trabajo`
