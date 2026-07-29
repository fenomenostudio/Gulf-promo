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

Por eso en escritorio se usa `aspect-ratio: 1920/350` con `object-fit: cover`:
recorta el vacío transparente, no los logos (quedan 32px de margen arriba y 16px
abajo). En móvil se mantiene la proporción completa 1920/647.

## Regla importante del validador de Tally

Tally revisa el contenido del campo y **rechaza el bloque completo** si detecta
algo sospechoso, mostrando *"The custom CSS won't be applied because it suggests
malicious intent"* debajo del campo. Pasó con una versión que llevaba comentarios
mencionando JavaScript e inyección de código.

→ Pegar el CSS **sin comentarios**, y confirmar que no aparezca el mensaje rojo
antes de dar por hecho que se aplicó.
