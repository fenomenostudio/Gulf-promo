# Gulf Promo — ganacongulf.com

Proyecto de la promoción **"Gana con Gulf"**: el usuario escanea un **código QR**,
llega a `ganacongulf.com` y llena un **formulario branded (Tally)** cuyas respuestas
caen en **Google Sheets**.

> Cotización aprobada: **COT-202607-006 — Opción B (Landing branded / Tally)**.
> Cliente: Lubriimport · Marca: Gulf.

## Qué incluye la Opción B (contratado)

| Componente | Detalle |
|---|---|
| **Dominio** | Registro y configuración de `ganacongulf.com` (1er año incluido; renovación ~Q120/año). |
| **QR** | Código QR con diseño de marca Gulf, apuntando al dominio. |
| **Formulario** | Formulario branded en **Tally** (se ve custom, no como Google Forms), alojado **directamente en `ganacongulf.com`** y conectado a **Google Sheets**. |
| **Tally Pro** | Incluido para quitar el sello "Made with Tally" y habilitar el dominio propio. |

## Arquitectura

```
[ Usuario escanea QR ]
          │
          ▼
  https://ganacongulf.com   ← dominio propio (Cloudflare DNS)
          │  (CNAME → Tally, SSL automático)
          ▼
   Formulario Tally branded  (Tally Pro)
          │  (integración nativa)
          ▼
      Google Sheets          ← base de respuestas
```

## Estructura del repo

```
├── README.md              ← este archivo
├── docs/
│   └── RUNBOOK.md         ← guía paso a paso de TODA la mecánica (empezar aquí)
├── qr/
│   ├── generate_qr.py     ← script que genera el QR
│   ├── ganacongulf-qr.svg ← QR vectorial (para imprenta)
│   ├── ganacongulf-qr.png ← QR alta resolución
│   └── README.md          ← specs de uso/impresión del QR
├── tally/
│   ├── form-spec.md       ← campos y lógica del formulario (a confirmar)
│   └── custom-css.css     ← CSS de marca Gulf (code injection en Tally Pro)
└── brand/
    └── brand.md           ← colores y tipografías de referencia
```

## Estado

- [x] QR generado y verificado (decodifica a `https://ganacongulf.com`); versión con logo Gulf
- [x] Runbook y specs documentados
- [x] Dominio `ganacongulf.com` registrado (Cloudflare, vence 10-jul-2027 — **auto-renew apagado**)
- [x] Cuenta Tally + **Pro activo** (mensual)
- [x] Formulario construido y branded en Tally (colores/logo/fuente oficiales de marca)
- [x] Google Sheet de respuestas creada ("Gana con Gulf — Respuestas")
- [x] Google Sheets conectado a Tally
- [x] Página de gracias configurada
- [x] Bloque de Instagram (link + checkbox requerido)
- [x] DNS de Tally en Cloudflare (A `@` → 35.205.106.218 y CNAME `www` → cname.tally.so, ambos **DNS only**) — verificado resolviendo
- [ ] **Mapear el formulario a la raíz del dominio** (Tally → Domains → Domain) — hoy devuelve 404
- [ ] Quitar el sello "Made with Tally"
- [ ] Términos y condiciones (contenido pendiente de Gulf)
- [ ] Prueba end-to-end (escaneo → form → fila en la Sheet)
- [ ] Imprimir QR en volumen (solo después de la prueba end-to-end)

👉 **Empezá por [`docs/RUNBOOK.md`](docs/RUNBOOK.md).**
