# RUNBOOK — Montaje de ganacongulf.com (Opción B / Tally)

Guía operativa paso a paso. Cada fase dice **quién lo hace** y **cuánto cuesta**.
La idea es que cualquiera del equipo pueda ejecutarlo aunque no conozca la mecánica.

Leyenda:
- 🟢 **Ya hecho** (en este repo)
- 🟠 **Requiere cuenta/pago** → lo ejecuta la agencia (Fenómeno) con sus credenciales
- ⚪ **Configuración** (sin costo, solo pasos)

---

## Resumen de costos (recurrentes)

| Concepto | Costo real | Frecuencia | Notas |
|---|---|---|---|
| Dominio `.com` (Cloudflare, al costo) | ~US$10.44 (~Q80–90) | anual | 1er año incluido en la cotización; renovación ~Q120/año a Gulf |
| Tally Pro | US$29/mes o **US$290/año** (2 meses gratis anual) | mensual/anual | necesario para quitar sello + dominio propio |
| Google Sheets | Gratis | — | con cuenta Google existente |
| Hosting landing | Gratis | — | lo hostea Tally directamente |

> **Decisión de negocio:** Tally Pro es un costo recurrente que la cotización no
> desglosó como línea mensual. Confirmar con Gulf si el mantenimiento de Tally Pro
> va por cuenta de la agencia (y se refactura) o se traslada al cliente. Ver §7.

---

## FASE 0 — Prerrequisitos ⚪

Antes de empezar, tener a mano:
- [ ] Cuenta **Cloudflare** (gratis) — para registrar el dominio y manejar DNS.
- [ ] Cuenta **Tally** (con el correo del proyecto, ej. `hola@fenomenostudio.com`).
- [ ] Cuenta **Google** con acceso a Google Sheets (la que será dueña de la base).
- [ ] **Manual de marca Gulf** (colores exactos, tipografía, logo en SVG/PNG).
- [ ] Definir con Gulf: **campos del formulario** y **términos y condiciones** de la promo.

---

## FASE 1 — Registrar el dominio `ganacongulf.com` 🟠

**Recomendado: Cloudflare Registrar.** Razón: vende el `.com` al costo (registro =
renovación, sin sorpresas), incluye DNS gratis y — clave para esto — hace **CNAME
flattening en el apex**, que es lo que permite que `ganacongulf.com` (sin `www`)
apunte a Tally. Otros registradores baratos: Porkbun, Spaceship. Evitar GoDaddy
(1er año barato, renovación cara).

Pasos:
1. Entrar a Cloudflare → **Domain Registration → Register Domains**.
2. Buscar `ganacongulf.com` → si está libre, comprar (~US$10.44/año).
   - Si NO está libre, avisar a Gulf de inmediato (alternativas: `.gt`, `.com.gt`,
     u otro nombre — pero eso cambia el QR, ver Fase 6).
3. Al registrarlo en Cloudflare, el DNS ya queda gestionado por Cloudflare (ideal).

> **Passthrough:** la agencia registra y factura a Gulf (así se cotizó). Guardar la
> factura del registrador para el traslado de costo.

**Resultado:** dominio propiedad de la agencia, DNS en Cloudflare, listo para Fase 4.

---

## FASE 2 — Crear cuenta Tally + activar Pro 🟠

1. Ir a [tally.so](https://tally.so) → crear cuenta con el correo del proyecto.
2. Crear un **Workspace** para Gulf (ej. "Gulf — Gana con Gulf").
3. Activar **Tally Pro** (Settings → Billing). Plan anual sale más barato (US$290/año).
   - Pro habilita: quitar sello "Made with Tally", dominio propio, remover branding,
     inyección de CSS, y más lógica.

**Resultado:** workspace Pro listo para construir el formulario y conectar dominio.

---

## FASE 3 — Construir el formulario branded ⚪

Seguir la especificación en [`../tally/form-spec.md`](../tally/form-spec.md).
Resumen del proceso en Tally:

1. **New form** → empezar en blanco (no plantilla).
2. Agregar los campos definidos en `form-spec.md` (nombre, teléfono, etc.).
3. **Branding** (Form settings → Design / Branding):
   - Subir logo Gulf.
   - Colores: fondo, botones y acentos según [`../brand/brand.md`](../brand/brand.md).
   - Tipografía de marca (o la más cercana disponible en Tally).
4. **CSS avanzado** (opcional, Pro): pegar [`../tally/custom-css.css`](../tally/custom-css.css)
   en *Form settings → Code injection* para afinar look que el panel no cubre.
5. **Página de gracias** (Thank you): mensaje con la marca ("¡Gracias por participar
   en Gana con Gulf!") + T&C / próximos pasos.
6. **Remover sello** "Made with Tally" (Pro → Form settings → Branding).
7. **Publicar** el formulario.

**Resultado:** formulario publicado con URL de Tally (temporal, ej. `tally.so/r/xxxx`).
En la Fase 4 se le pone el dominio propio.

---

## FASE 4 — Conectar el dominio propio a Tally ⚪

1. En Tally (sidebar) → **Domains → Add domain** → escribir `ganacongulf.com`.
2. Tally muestra la pestaña **Configuration** con los registros DNS a crear
   (varios **CNAME** + un **TXT**).
3. En **Cloudflare → DNS → Records**, crear exactamente esos registros:
   - Los CNAME de Tally (Cloudflare aplica *flattening* en el apex automáticamente).
   - El TXT de verificación.
   - ⚠️ Poner los registros de Tally en **"DNS only"** (nube gris, sin proxy naranja)
     para que Tally pueda emitir su SSL.
4. Esperar propagación (segundos a pocas horas). Tally emite SSL solo y el semáforo
   se pone **verde** = dominio activo.
5. En **Domains → Map form**, elegir el formulario publicado y darle un slug corto.
   Para que el destino sea el apex limpio, mapearlo a la raíz de `ganacongulf.com`.

**Verificar:** abrir `https://ganacongulf.com` en el navegador → debe cargar el
formulario con candado SSL y sin sello Tally.

> Si el registrador NO fuera Cloudflare y no soportara apex/flattening: usar
> `www.ganacongulf.com` (CNAME) y redirigir el apex → `www`. En ese caso el QR
> debe apuntar a `https://www.ganacongulf.com` (regenerar, ver Fase 6).

---

## FASE 5 — Conectar Google Sheets ⚪

1. En el formulario Tally → **Integrations → Google Sheets → Connect**.
2. Autorizar con la **cuenta Google dueña de la base** (la del proyecto).
3. Elegir crear una hoja nueva (ej. "Gana con Gulf — Respuestas").
4. Mapear cada campo del formulario a una columna.
5. Hacer un envío de prueba → confirmar que la fila aparece en la hoja.

**Resultado:** cada respuesta cae automáticamente en Google Sheets, en tiempo real.

> Alternativa/robustez: se puede duplicar el flujo con **Make** (webhook Tally → Sheets)
> si se quiere lógica extra (dedup, notificaciones, etc.). No es necesario para el MVP.

---

## FASE 6 — Código QR 🟢

**Ya generado y verificado** en [`../qr/`](../qr/) apuntando a `https://ganacongulf.com`.

- Para imprenta usar el **SVG** (`ganacongulf-qr.svg`) — escala sin perder nitidez.
- Specs de tamaño mínimo / zona de silencio: ver [`../qr/README.md`](../qr/README.md).
- ⚠️ **No mandar a imprimir en volumen hasta que la Fase 4 esté verde** y el QR
  resuelva correctamente en un teléfono real (ver Fase 7).
- Si cambia la URL final (ej. `www` o dominio distinto), regenerar con
  `python3 qr/generate_qr.py` cambiando la variable `URL`.

---

## FASE 7 — Prueba end-to-end ⚪

Con todo montado, probar el recorrido real:
1. Imprimir/mostrar el QR en pantalla y **escanearlo con un teléfono** (iOS y Android).
2. Debe abrir `https://ganacongulf.com` con el formulario branded y SSL.
3. Llenar y enviar → confirmar:
   - [ ] La respuesta llega a **Google Sheets**.
   - [ ] Se muestra la **página de gracias**.
   - [ ] No aparece el sello "Made with Tally".
   - [ ] Se ve bien en móvil (la mayoría escanea desde el celular).
4. Probar con datos inválidos (teléfono/correo) → validaciones funcionan.

---

## FASE 8 — Entrega y mantenimiento

- **Renovación dominio:** ~Q120/año (recordatorio anual; Cloudflare puede autorrenovar).
- **Tally Pro:** revisar cargo mensual/anual; si se cancela, el dominio propio y el
  "sin sello" dejan de funcionar (el form vuelve a URL de Tally con sello).
- **Base de datos:** la Google Sheet es la fuente de verdad de participantes.
- **Handoff a Gulf:** entregar accesos o dejar todo bajo la agencia según lo acordado
  (definir en §7 de abajo).

---

## §7 — Decisiones pendientes (confirmar con Gulf / interno)

1. **Campos del formulario y T&C** → ver `tally/form-spec.md` (propuesta a validar).
2. **Costo recurrente de Tally Pro** → ¿lo absorbe la agencia y refactura, o se
   traslada a Gulf? La cotización lo incluyó pero sin desglose mensual.
3. **Propiedad de cuentas** → ¿dominio y Tally quedan a nombre de la agencia
   (gestión mensual) o se transfieren a Gulf al cierre de la promo?
4. **Vigencia de la promo** → fecha de fin (para saber hasta cuándo mantener Pro).
