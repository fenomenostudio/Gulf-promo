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

- [x] QR generado y verificado (decodifica a `https://ganacongulf.com`)
- [x] Runbook y specs documentados
- [ ] Dominio registrado (requiere pago — agencia)
- [ ] Cuenta Tally + Pro (requiere cuenta/pago — agencia)
- [ ] Formulario construido en Tally
- [ ] Dominio conectado a Tally (DNS)
- [ ] Google Sheets conectado
- [ ] Prueba end-to-end

👉 **Empezá por [`docs/RUNBOOK.md`](docs/RUNBOOK.md).**
