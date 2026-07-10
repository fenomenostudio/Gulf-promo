# Receta de branding del formulario en Tally (plan GRATIS)

Todo esto se hace en Tally → abrí tu formulario → menú **"..." (arriba a la derecha)
→ Design/Theme** (o el panel de diseño con el ícono de pincel). No requiere Pro.

> HEX **oficiales** del brand book de Gulf (ver `../brand/brand.md`).

## 1. Tema (Theme → Custom)
Elegí **Custom** para definir tus propios colores:

| Elemento | Valor | HEX |
|---|---|---|
| **Background** (fondo) | White | `#FFFFFF` |
| **Text** (preguntas/texto) | Gulf Dark Blue | `#002776` |
| **Button** (fondo del botón) | Gulf Orange | `#FF6319` |
| **Button text** | White | `#FFFFFF` |
| **Accent** (links, opción seleccionada, foco de inputs) | Gulf Orange | `#FF6319` |

## 2. Fuente (Font)
- La tipografía primaria de Gulf es **Helvetica Neue** (secundaria: Arial), que no
  está en Google Fonts. La opción más **fiel a marca** en Tally es **Arimo**
  (equivalente métrico de Arial). Alternativa moderna aceptable: **Inter**.

## 3. Botón (Button settings)
- Texto del botón: **¡Participar!**
- Corner radius: **8 px**
- Alineación: centro
- Ancho: full width (se ve mejor en móvil, que es donde escanean el QR)
- Font size: 16–18 px, peso bold

## 4. Inputs (campos)
- Border color: **Gulf Light Grey `#D1D4D3`**
- Border radius: **8 px**
- Foco: usa el color de acento (naranja) → ya queda por el Accent del tema

## 5. Logo y portada (Cover)
- **Logo:** subí el logo Gulf (bloque de imagen arriba del título, o el slot de logo).
  Tener versión PNG con fondo transparente o SVG.
- **Cover image (opcional):** un banner de marca arriba del form (naranja/navy con el
  claim de la promo). Da mucho caché. Se puede diseñar aparte y subir.

## 6. Página de gracias (Thank you)
- **Cómo agregarla:** en el editor del form, al final, escribí **`/thank`** y elegí
  el bloque **"Thank you page"** (o activá el toggle "Thank you page" a la derecha de
  la última página). Es gratis; solo quitar el sello Tally es de Pro.
- Editala con texto/imagen: **"🎉 ¡Gracias por participar en Gana con Gulf!"** + próximos pasos.
- Mantener los mismos colores del tema.

---

## Lo que queda para cuando se active Tally Pro (al salir en vivo)
- Quitar el sello **"Made with Tally"**.
- Conectar el **dominio propio** `ganacongulf.com`.
- **CSS avanzado** (`custom-css.css`) para afinar detalles que el panel no cubre.

> Regla de oro: primero dejá el form lindo con el panel gratis; el CSS es solo para
> los últimos toques finos una vez que Pro esté activo.
