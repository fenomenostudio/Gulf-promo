# Cuál CSS usar

**Archivo vigente: `custom-css-final.css`** — es el que va pegado en Tally
(Domains → ganacongulf.com → code injection, dentro del `<style>`).

Los demás archivos son los pasos del diagnóstico y se conservan solo como
historial. No pegarlos.

## Qué causaba la pantalla blanca (diagnóstico cerrado)

El síntoma era: al abrir un dropdown en escritorio la página se blanqueaba y el
layout se descomponía. En móvil no pasaba.

Se descartaron por prueba y error, en este orden:

1. **Animaciones `animation-timeline: scroll()`** que animaban `clip-path` y
   `transform` con custom properties no interpolables. Se eliminaron: el bug siguió.
   → No era la causa (pero eran código inestable; quedaron fuera).
2. **Gradientes radiales del cover.** Se probaron por separado: el bug NO aparece.
   → Inocentes. Se conservan.
3. **`overflow-x: clip` en `html, body, .tally-app`** → **ESTA ERA LA CAUSA.**
   Creaba un contexto de recorte que afectaba al listado de los dropdowns.
   Ya no se usa: era necesario solo para tapar el desborde del `100vw` de la
   imagen full-bleed, que también se eliminó.

## Hallazgos sobre el CSS propio de Tally

Verificados leyendo el HTML publicado:

- `.tally-app` (`.hnTHhC`) tiene `display:flex; overflow-x:hidden; position:relative;
  z-index:1`. El `overflow-x:hidden` **desactiva `position: sticky`** en todo lo que
  esté dentro, porque convierte al elemento en contenedor de scroll.
  Se resuelve con `.tally-app { overflow: visible !important; }`.
- El `z-index` **máximo que usa Tally en todo su CSS es 1**. Por eso el header
  sticky lleva `z-index: 2`: lo mínimo para quedar encima de los badges de asterisco
  (`.kdcgLz`, que son `position:absolute; z-index:1`) sin usar valores altos que
  puedan tapar los dropdowns.
- El cover es `div.tally-form-cover > img` (imagen como elemento, no como
  background). El PNG es transparente (verificado: alfa 0 en las esquinas), así que
  el gradiente del CSS se ve a través de él.

## Header a media altura en escritorio

El PNG del cover es 1920×647 pero el contenido visible ocupa solo de `y=181` a
`y=482` (302px). Arriba y abajo hay ~28% y ~25% de transparencia.

**Escritorio:** `aspect-ratio: 1920/270` + `object-fit: contain` + `transform:
scale(1.111)` → logos de 140px con 130px de margen total.

Importante: acá **no** se puede usar `object-fit: cover`. Con una caja de 270px, cover
recorta la imagen de `y=188` a `y=458`, y los logos van de `y=181` a `y=482`: se
cortarían arriba y abajo. `contain` escala la imagen completa y el `transform` la
lleva al tamaño pedido.

**Móvil:** `aspect-ratio: 1920/971` (a 390px de ancho, 197px de alto) +
`transform: scale(1.549)` → logos de 95px. El scale es necesario porque con
`contain` la imagen queda limitada por el ancho, así que subir el alto de la caja no
la hace crecer: sin el scale, el espacio extra queda vacío.

Los escalados están verificados contra recorte: el contenido del PNG ocupa de `x=626`
a `x=1294` (626px transparentes por lado), y el scale más agresivo (1.549) solo
recorta 340px por lado.

Todos los textos van en Gulf Dark Blue `#002776`, incluido el que la persona
escribe en los campos. El único texto blanco es el de las tarjetas azules.

## Regla importante del validador de Tally

Tally revisa el contenido del campo y **rechaza el bloque completo** si detecta
algo sospechoso, mostrando *"The custom CSS won't be applied because it suggests
malicious intent"* debajo del campo. Pasó con una versión que llevaba comentarios
mencionando JavaScript e inyección de código.

→ Pegar el CSS **sin comentarios**, y confirmar que no aparezca el mensaje rojo
antes de dar por hecho que se aplicó.

## Bloques sin estilo de tarjeta

Dos bloques de texto van planos (sin tarjeta, sin borde naranja, sin barra navy),
targeteados por su clase única de Tally:

| Bloque | Clase |
|---|---|
| "Ver términos y condiciones" | `tally-block-e503a3de-72b4-4eb8-9c95-a2f087e67296` |
| "Período de participación" | `tally-block-0f2906b0-1823-4fe4-b3ac-88d1c71be7f8` |

⚠️ Esas clases son el ID interno del bloque en Tally. **Si se borra y se vuelve a
crear el bloque, el ID cambia** y hay que actualizar el CSS. Si algún día uno de los
dos vuelve a aparecer con tarjeta, la causa es esa: buscar la clase nueva en el HTML
publicado y reemplazarla acá.
