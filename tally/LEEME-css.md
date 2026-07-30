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

## Experimento: header que se encoge al hacer scroll

Archivos: `custom-css-con-scroll.css` (CSS) + `scroll-header.html` (script).

Cómo funciona: el script agrega el atributo `data-gulf-scroll="on"` al `<html>`
cuando el scroll pasa los 120px, y el CSS reacciona a ese atributo. Es **un solo
cambio discreto** al cruzar un umbral, no una animación por píxel — mucho más barato
y estable que `animation-timeline: scroll()`, que fue lo que se eliminó por inestable.

| Estado | Escritorio | Móvil |
|---|---|---|
| Reposo | `aspect-ratio 1920/270`, scale 1.111 | `aspect-ratio 1920/971`, scale 1.549 |
| Compacto | `aspect-ratio 1920/150`, scale 1.285 | `aspect-ratio 1920/591`, scale 1.25 |

Dos detalles que se corrigieron tras probarlo en vivo:

1. **El cambio salta en seco si el estado compacto usa `height` fijo**, porque en reposo
   el alto viene de `aspect-ratio` (= `height: auto`) y no se puede animar desde `auto`.
   Ambos estados usan `aspect-ratio`, que sí es interpolable.
2. **Cambiar el alto del header mueve el layout, eso mueve el scroll, y ese movimiento
   vuelve a disparar el umbral** → el header oscilaba al abrir un dropdown (el navegador
   acomoda el campo a la vista y mueve el scroll). Se resuelve con histéresis
   (enciende a 200px, apaga a 60px) más un bloqueo de 500ms después de cada cambio.

El `<script>` va en el code injection **a nivel de dominio** (Domains → General
Settings), que es donde Tally documenta los códigos de analítica. NO va en el campo
Custom CSS del formulario.

**El CSS es inofensivo por sí solo:** si el script nunca corre o Tally lo rechaza, el
atributo no aparece nunca y el header se queda en estado de reposo. O sea que se puede
pegar el CSS sin riesgo aunque el script falle.

Si el script no se puede aplicar, el estado final del proyecto es
`custom-css-final.css` sin efecto de scroll.

### Corrección del reset al abrir un dropdown (solo escritorio)

Síntoma: al abrir un dropdown en escritorio el header volvía a tamaño grande, y al
cerrarlo se compactaba otra vez. En móvil no pasaba.

Causa: en escritorio Tally dibuja su propia lista y aplica un **scroll lock** (fija el
`body`). Con el `body` en `position: fixed`, `window.pageYOffset` devuelve **0**, así que
el script creía que el usuario estaba en el tope de la página. En móvil se usa el
selector nativo del sistema, sin lock — por eso ahí no ocurría.

Dos guardas en el script, aplicadas solo al momento de **apagar** el estado compacto:

1. `scrollBloqueado()` — no apaga si el `body` está `position: fixed` o con
   `overflow: hidden` (o sea, si hay un scroll lock activo).
2. Salto sospechoso — no apaga si la posición cayó más de 250px de golpe respecto a la
   lectura anterior. Un scroll real es gradual; un lock salta a 0 de una.

El efecto compacto quedó **solo en escritorio**; en móvil se eliminó por decisión de
diseño (no aportaba).

### Tamaño del bloque "Período de participación"

Va deliberadamente más pequeño que cualquier otro texto del formulario: **14px en
escritorio y 13px en móvil**, cuando el texto legible más chico del resto es 16px y 15px
respectivamente. (Los 11px y 13px que aparecen en otras reglas son los íconos ✓
decorativos, no texto de lectura.)

Razón de diseño: la promo dura hasta el 19 de octubre, y un período largo mostrado con
demasiado peso visual invita a postergar el registro. La información tiene que estar,
pero sin competir con el llamado a participar.

El color es **Gulf Dark Grey `#6C6F70`** de la paleta de apoyo. Se eligió ese y no los
grises más claros por contraste: sobre blanco da 5.07:1, que cumple el mínimo de 4.5:1
para texto pequeño. Gulf Metallic Grey (`#7E848B`) da 3.78:1 y Medium Grey (`#A5ACAF`)
2.30:1 — ninguno cumple, y en un texto de 13-14px eso ya es ilegible para bastante gente.

Las reglas van **al final del archivo** a propósito: comparten especificidad con
`.tally-page-1 .tally-block-text` y con la media query de móvil, así que ganan por
orden de cascada. Si se agregan reglas nuevas después, hay que dejarlas antes de este
bloque o subirle la especificidad.

### Flecha del botón de Instagram

Va con el glifo **`\279A`** (HEAVY NORTH EAST ARROW) en lugar de `\2197` (↗), que se
veía demasiado delgada. Se escribe con el escape CSS y no con el carácter literal, para
que no dependa de la codificación al pegarlo en Tally.

Se descartó dibujarla con bordes (`border-top` + `border-right` rotados): sin rotación
queda como una esquina `¬` y con `rotate(45deg)` apunta a la derecha en vez de
arriba-derecha, perdiendo el sentido de "abre enlace externo".

## Validación de los consentimientos (T&C y mayoría de edad)

Un bloque de checkboxes marcado como **Required** en Tally solo exige **al menos una**
opción. Con dos casillas ("Acepto Términos y Condiciones" y "Soy mayor de 18 años") eso
dejaba pasar a quien marcara solo una — justo lo que el checkbox de edad busca respaldar.

**Solución aplicada:** `Min choices = 2` en el bloque (verificado en el formulario
publicado: `hasMinChoices: true, minChoices: 2` en ambas casillas). Es nativo y no
requiere mantener lógica. Al título se le agregó "(marca ambas para continuar)" porque el
mensaje de error de Tally es genérico ("se requiere un mínimo de 2").

**Descartado:** resolverlo con lógica condicional. La regla que se había construido usaba
*"When **all** match: does not contain A **y** does not contain B → ocultar botón"*, que
solo oculta el botón cuando **ninguna** casilla está marcada; los dos casos parciales se
escapaban. Con "any" en lugar de "all" habría funcionado, pero `Min choices` ya lo cubre.

### El bloque "Recuerda qué" es intencionalmente condicional — NO es un bug

Está marcado `isHidden: true` y se muestra mediante una **lógica condicional activa**
atada a la casilla "Soy mayor de 18 años". **Esto es deliberado. No lo desactives.**

El razonamiento: ese bloque contiene la condición que puede definir si alguien llega a
cobrar el premio (el ganador debe asistir presencialmente a la entrega el 25 de octubre,
y si no puede, se elige otro). Es parte de los T&C, pero la mayoría de la gente acepta
los términos sin leerlos. Sacándola del documento y mostrándola en el formulario, aparece
donde la atención es más alta.

Por qué funciona sin dejar a nadie afuera: `Min choices = 2` obliga a marcar ambas
casillas, así que el bloque se muestra al **100% de quienes envían**, y siempre **antes**
de pulsar "Participar" — el envío, no la casilla, es el compromiso real. Y al estar
oculto por defecto, no alarga el formulario para quien apenas está empezando a llenarlo.

⚠️ Consecuencia operativa: si algún día se borra esa lógica condicional, **hay que
desocultar el bloque primero** (menú del bloque → Hide / ⌘⇧H). Si se borra la lógica con
el bloque aún oculto, la información desaparece del formulario sin que nadie lo note.
