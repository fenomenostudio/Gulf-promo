# Especificación del formulario — "Gana con Gulf"

> ⚠️ **PROPUESTA a confirmar con Gulf.** Estos campos son un punto de partida típico
> para una promo/rifa con captura de datos en Guatemala. Ajustar según la mecánica
> real del premio y lo que legal/marketing de Gulf requiera.

## Objetivo
Capturar participantes de la promo de forma rápida (se llena desde el celular tras
escanear el QR) y guardar todo en Google Sheets.

## Campos propuestos

| # | Campo | Tipo Tally | Requerido | Notas |
|---|---|---|---|---|
| 1 | Nombre completo | Short text | Sí | — |
| 2 | Teléfono (WhatsApp) | Phone number | Sí | Validación de formato; principal canal de contacto |
| 3 | Correo electrónico | Email | Sí | Validación de email |
| 4 | DPI / No. de identificación | Short text | Opcional* | *Requerido si el premio exige verificación de identidad |
| 5 | Departamento | Dropdown | Sí | Lista de los 22 departamentos de Guatemala |
| 6 | Estación Gulf / punto de compra | Short text o Dropdown | Opcional | Si la promo es por compra en estación |
| 7 | No. de factura / ticket | Short text | Opcional | Si la mecánica valida compra |
| 8 | Producto Gulf comprado | Dropdown | Opcional | Si aplica a productos específicos |
| 9 | Acepto términos y condiciones | Checkbox | Sí | Enlazar a T&C de la promo (bloquea envío si no marca) |
| 10 | Autorizo recibir comunicaciones de Gulf | Checkbox | Opcional | Opt-in de marketing (recomendado separarlo del #9) |

\* Ajustar obligatoriedad según la mecánica final.

## Lógica / comportamiento
- **Una sola página** (form corto = más conversión desde el QR).
- Validaciones nativas de Tally en teléfono y correo.
- Botón de envío con texto de marca: ej. **"¡Participar!"**.
- **Página de gracias:** "🎉 ¡Gracias por participar en *Gana con Gulf*! Pronto te
  contactaremos si resultas ganador." + recordatorio de T&C.
- (Opcional) **Hidden fields** para trackear origen si se usan varios QR (ej. `utm`
  o `estacion` por código) — útil si quieren saber de qué punto vino cada registro.

## Integraciones
- **Google Sheets** (nativa) — cada campo = una columna. Ver Fase 5 del RUNBOOK.
- Tally agrega automáticamente **timestamp** de envío.

## Privacidad / legal (recordatorio)
- Incluir enlace visible a **Términos y Condiciones** y **Aviso de privacidad**.
- El opt-in de marketing (#10) debe ser **separado y opcional** del consentimiento
  de participación (#9) — buena práctica de datos.
