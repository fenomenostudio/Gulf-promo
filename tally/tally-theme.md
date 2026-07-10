# Receta de branding del formulario en Tally (plan GRATIS)

Todo esto se hace en Tally → abrí tu formulario → menú **"..." (arriba a la derecha)
→ Design/Theme** (o el panel de diseño con el ícono de pincel). No requiere Pro.

> ⚠️ Los HEX son **recomendados**. Fenómeno debe confirmarlos contra el **manual de
> marca oficial de Gulf** y ajustarlos si difieren.

## 1. Tema (Theme → Custom)
Elegí **Custom** para definir tus propios colores:

| Elemento | Valor recomendado | HEX |
|---|---|---|
| **Background** (fondo) | Blanco (máxima conversión y contraste) | `#FFFFFF` |
| **Text** (preguntas/texto) | Gulf Navy | `#002F6C` |
| **Button** (fondo del botón) | Gulf Orange | `#F58220` |
| **Button text** | Blanco | `#FFFFFF` |
| **Accent** (links, opción seleccionada, foco de inputs) | Gulf Orange | `#F58220` |

## 2. Fuente (Font)
- Elegí una **Google Font** limpia y legible. Recomendadas (de más a menos neutra):
  **Inter**, **Montserrat**, **Archivo**.
- Si el manual de Gulf define una tipografía, usar la más cercana disponible en Google Fonts.

## 3. Botón (Button settings)
- Texto del botón: **¡Participar!**
- Corner radius: **8 px**
- Alineación: centro
- Ancho: full width (se ve mejor en móvil, que es donde escanean el QR)
- Font size: 16–18 px, peso bold

## 4. Inputs (campos)
- Border color: gris claro `#D9DEE7` (o Gulf Navy sutil)
- Border radius: **8 px**
- Foco: usa el color de acento (naranja) → ya queda por el Accent del tema

## 5. Logo y portada (Cover)
- **Logo:** subí el logo Gulf (bloque de imagen arriba del título, o el slot de logo).
  Tener versión PNG con fondo transparente o SVG.
- **Cover image (opcional):** un banner de marca arriba del form (naranja/navy con el
  claim de la promo). Da mucho caché. Se puede diseñar aparte y subir.

## 6. Página de gracias (Thank you)
- Mensaje branded: **"🎉 ¡Gracias por participar en Gana con Gulf!"** + próximos pasos.
- Mantener los mismos colores del tema.

---

## Lo que queda para cuando se active Tally Pro (al salir en vivo)
- Quitar el sello **"Made with Tally"**.
- Conectar el **dominio propio** `ganacongulf.com`.
- **CSS avanzado** (`custom-css.css`) para afinar detalles que el panel no cubre.

> Regla de oro: primero dejá el form lindo con el panel gratis; el CSS es solo para
> los últimos toques finos una vez que Pro esté activo.
