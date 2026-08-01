# Medición y campaña de Meta — "Gana con Gulf"

Estado de la instrumentación para medir registros del formulario desde anuncios
de Meta. Todo verificado contra el HTML publicado y contra la API de Meta.

## Dónde vive cada cosa

| Recurso | Dónde | ID |
|---|---|---|
| Pixel / conjunto de datos | Portafolio **Fenómeno Studio** | `2162722331255733` ("Gana con Gulf") |
| Portafolio propietario | Fenómeno Studio | `3801886976793479` |
| Cuenta publicitaria | Gulf Lubricantes | `107258260078806` |
| Conversión personalizada | Cuenta Gulf Lubricantes | `27393149657048443` |
| Dominio verificado | Fenómeno Studio | `ganacongulf.com` |

**Decisión: el pixel es de Fenómeno, no de Lubriimport.** Existe un "Píxel de
Lubriimport, S.A." que pertenece a la comercializadora, no a la marca. Se creó uno
propio para no depender de accesos de terceros. El dominio se verificó en el mismo
portafolio que el pixel — Meta solo permite verificarlo en **uno**.

El pixel se comparte con la cuenta publicitaria vía **Activos conectados**, no como
socio. Es lo que corresponde: la cuenta necesita usar el pixel, no administrarlo.

## Verificación del dominio

Método TXT en Cloudflare (no la meta-etiqueta HTML). Valor:

```
facebook-domain-verification=v64arwjrkfpxtu1utciuz0ep5ksvea
```

⚠️ El error que se cometió la primera vez fue pegar el HTML de la meta-etiqueta
dentro del registro TXT. Cloudflare rechaza eso por comillas. Va solo el string.

## Código del pixel

Va en el **code injection a nivel de dominio** (Domains → General Settings), debajo
del script del header con scroll. No en el campo Custom CSS.

```html
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '2162722331255733');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=2162722331255733&ev=PageView&noscript=1" /></noscript>
```

Tally dispara por su cuenta dos eventos personalizados cuando detecta `fbq`:
`Tally.FormPageView` y `Tally.FormSubmitted`. No hay que escribirlos.

## Conversión personalizada

```json
{
  "name": "Registro — Gana con Gulf",
  "custom_event_type": "LEAD",
  "pixel_rule": {"and":[
    {"event":{"eq":"Tally.FormSubmitted"}},
    {"or":[{"URL":{"i_not_contains":"terminos"}}]}
  ]}
}
```

**Por qué la regla de URL es obligatoria:** la página `/terminos` carga el mismo
pixel y conserva su botón de envío (el que sirve de regreso al formulario). Sin esa
regla, cada persona que vuelve del documento legal contaría como un registro.

**Por qué el evento no es "Todo el tráfico de la URL":** eso contaría cada visita a
la página como conversión. El formulario vive en una sola URL que no cambia al
enviarse, así que no hay ninguna URL de "gracias" que sirva como señal — la única
señal real de registro es el evento `Tally.FormSubmitted`.

**Categoría `Cliente potencial` puesta a mano.** Por defecto Meta dice "Categoría
seleccionada por Meta" y la adivina. La categoría es lo que mapea la conversión al
modelo de optimización, así que se define explícitamente.

Sin valor de conversión: no hay venta, un monto inventado ensuciaría el ROAS.

## Medición de eventos agregados: no aplica

Este portafolio ya está migrado al **ranking automático**. La pantalla manual de
prioridades no existe en Configuración del conjunto de datos ni en la URL directa.
La categoría `Cliente potencial` es la señal que consume ese ranking, así que el
paso queda cubierto.

Si algún día reaparece la pantalla manual: cambiar prioridades **pausa 72 horas**
los conjuntos de anuncios que optimicen por un evento degradado. Hacerlo antes de
lanzar, nunca en campaña.

## Ajustes del conjunto de datos

| Ajuste | Estado | Razón |
|---|---|---|
| Cookies de origen | Activadas | Mejora atribución |
| Detalles de páginas por IA | Activado | Sin efecto negativo |
| Eventos sin código | **Desactivado** | Ya hay eventos explícitos; duplicaría |
| API de conversiones | Sin usar ("Connection pending") | Solo pixel de navegador |
| Coincidencias del sitio web automáticas | **Pendiente de decisión** | Ver abajo |

**Coincidencias avanzadas automáticas.** Recomendado activarlas: el formulario pide
correo y teléfono, que son las señales que mejor emparejan. Sin esto Meta solo tiene
la cookie, que se pierde en iOS y navegación privada.

⚠️ Envía correo y teléfono en hash a Meta. Los T&C de Gulf deberían mencionar que se
comparten datos con plataformas de publicidad para medición. **La decisión es del
cliente, no de la agencia.**

## Atribución por canal: campos ocultos

Tres bloques `HIDDEN_FIELDS` en el formulario: `utm_source`, `utm_campaign`,
`utm_content`. Tally los llena solo desde los parámetros de la URL.

```
https://ganacongulf.com/?utm_source=meta&utm_campaign=nacional
```

Primer parámetro con `?`, los siguientes con `&`. Quien entra por el **QR impreso**
llega al dominio pelado y esas columnas quedan vacías — eso identifica el tráfico
orgánico/impreso sin necesidad de un QR distinto por canal.

Solo dos parámetros, fijos por campaña (`nacional` o `proximidad`). **`utm_content`
queda vacío a propósito**: el desglose por anuncio, ubicación y plataforma ya lo da
Meta nativamente, y etiquetarlo a mano sería trabajo manual para duplicar un dato que
la cuenta publicitaria entrega sola.

Lo que Meta **no** da, y por eso `utm_source` sí vale: la hoja que recibe Gulf no sabe
nada de anuncios. Sin ese campo no hay forma de decir cuántas filas vinieron de pauta y
cuántas del QR impreso. Además Meta reporta con atribución de 7 días clic y la hoja
cuenta filas — los totales nunca coinciden, y el origen en la propia hoja es lo que
permite reconciliarlos.

⚠️ **Trampa de Tally, ya pisada una vez.** Un bloque de texto marcado `isHidden: true`
(⌘⇧H) **no** es un campo oculto: es un párrafo invisible que no captura nada y no
genera columna en Sheets. El campo oculto real es un tipo de bloque propio, se inserta
con **`/hidden`**, y en el HTML publicado aparece como:

```json
{"type":"HIDDEN_FIELDS","payload":{"hiddenFields":[{"name":"utm_source"}]}}
```

Cómo verificarlo sin abrir el editor:

```bash
curl -s -L https://ganacongulf.com | grep -c HIDDEN_FIELDS   # debe dar 3
```

Después de agregarlos hay que **actualizar la integración de Google Sheets** para que
aparezcan las tres columnas nuevas.

## Prueba de punta a punta — cerrada

30 de julio, 16:06. Registro real desde teléfono, navegación normal, sin código de test:

- Conversión `Registro — Gana con Gulf`: `last_fired_time` pasó de `null` a
  `2026-07-30T16:06:22`.
- Eventos recibidos: `Tally.FormPageView` 7 · `PageView` 6 · `Tally.FormSubmitted` 1.
- Los tres UTM llegaron a la hoja con los valores esperados.
- Envíos de prueba borrados de Tally y de Sheets.

⚠️ **Lo que esta prueba NO demuestra.** Durante el recorrido se visitó `/terminos`, y
aun así solo hay **un** `Tally.FormSubmitted` en todo el conjunto de datos. Es decir:
el botón de regreso de esa página no dispara el evento, así que la regla
`URL no contiene terminos` **nunca llegó a activarse**.

Está probado que no hay doble conteo. **No** está probado que la regla funcione. Se
conserva igual, como seguro por si esa página cambia de comportamiento.

## Campañas creadas (ambas en PAUSED)

Presupuesto real: **Q7,000 nacional + Q4,300 proximidad, mensuales** — agosto,
septiembre y octubre, más el presupuesto de julio sin ejecutar repartido entre esos
tres meses. Total: **Q28,000 nacional** y **Q17,200 proximidad**.

| Campaña | ID | Objetivo | Presupuesto |
|---|---|---|---|
| Gana con Gulf — Nacional \| Registros | `120245753960150088` | OUTCOME_LEADS | CBO **total Q28,000** |
| Gana con Gulf — Proximidad \| 5 distribuidores | `120245723978660088` | OUTCOME_AWARENESS | ABO, Q3,440 totales por conjunto |

⚠️ `120245723919200088` — renombrada **"ZZ NO USAR — Nacional (presupuesto diario,
reemplazada)"**. Es la primera versión, con presupuesto diario. Borrar cuando el
anuncio esté duplicado en la nueva.

**Por qué hubo que recrearla.** Meta no permite convertir el tipo de presupuesto de una
campaña existente:

```
Budget type change not allowed: Changing from lifetime to daily budget
or vice versa is not allowed for a campaign.  (subcode 1885630)
```

El tipo se define al crear y no se puede cambiar. Decisión a tomar **antes** de armar
la campaña, no después.

### Error #1870194 al publicar

Síntoma: *"Tu audiencia contiene una opción de segmentación por lugar que se ha
suprimido"*. No aparece en `ads_get_errors` — es validación de publicación, no de
guardado, así que el conjunto se crea sin quejas y falla recién al publicar.

Causa: al crear los conjuntos no se especificó `location_types` dentro de
`geo_locations`, y el valor por defecto que aplicó Meta incluye una opción ya retirada.

Arreglo, aplicado a los 6 conjuntos:

```json
"geo_locations": {"countries": ["GT"], "location_types": ["home", "recent"]}
```

`home` + `recent` = "personas que viven en o estuvieron recientemente en" — la
combinación que Meta sigue soportando.

Conjunto nacional `120245753969530088` — "Nacional — Amplio GT 18+":

```json
{
  "optimization_goal": "OFFSITE_CONVERSIONS",
  "billing_event": "IMPRESSIONS",
  "destination_type": "WEBSITE",
  "promoted_object": {"custom_conversion_id": "27393149657048443"},
  "targeting": {
    "geo_locations": {"countries": ["GT"], "location_types": ["home", "recent"]},
    "age_min": 18,
    "targeting_automation": {"advantage_audience": 0}
  },
  "attribution_spec": [
    {"event_type": "CLICK_THROUGH", "window_days": 7},
    {"event_type": "VIEW_THROUGH", "window_days": 1}
  ]
}
```

**Por qué `advantage_audience: 0`.** Con Advantage+ Audience activo, Meta trata
`age_min` como sugerencia y puede servir a menores de 18. La promo exige mayoría de
edad en sus T&C, así que el piso tiene que ser duro. Cuesta algo de expansión
algorítmica; se paga con gusto frente a registrar menores que no pueden participar.

**Sin intereses.** Guatemala tiene ~7 millones de adultos en Meta. Filtrar por
"mecánica" o "aceite de motor" achica el público hasta donde el algoritmo no tiene
dónde buscar, y excluye a quien cambia su aceite sin haber tocado nunca ese tema en
Facebook. Con un evento de conversión alimentándolo, el sistema encuentra el patrón.

**Un solo conjunto de anuncios.** Meta necesita ~50 conversiones semanales **por
conjunto** para salir de la fase de aprendizaje. Partir el presupuesto en varios
públicos deja a todos por debajo del umbral y optimizando a ciegas.

### Presupuesto nacional: total, no diario

**Q28,000 de presupuesto total** con fecha de fin el 19 de octubre. Meta reparte el
monto entre los días que queden.

Se eligió total sobre diario por dos razones del cliente: garantiza que se gaste
exactamente lo presupuestado (un presupuesto diario fija ritmo, no monto), y absorbe
sola cualquier corrimiento de la fecha de arranque.

Efecto secundario bueno: **desaparece el cambio manual del 1 de octubre.** Con
presupuesto diario había que subir de Q306 a Q491 a mano —porque octubre vale lo mismo
pero dura 19 días— y esa edición reiniciaba la fase de aprendizaje. Con total, Meta
acelera sola al acercarse el cierre.

El promedio implícito es **Q350 diarios** sobre 80 días. Salir de la fase de
aprendizaje (7 registros al día) admite un CPL de hasta **Q50**.

⚠️ Contrapartida honesta: Meta recomienda presupuesto diario para campañas de
conversión, porque el gasto parejo ayuda a la fase de aprendizaje. Con presupuesto
total el ritmo diario varía más. Si el gasto se vuelve irregular, se puede suavizar con
`daily_spend_cap` en el conjunto sin cambiar el tipo de presupuesto.

### Proximidad — 5 conjuntos creados con ubicación provisional

| Conjunto | ID |
|---|---|
| Proximidad — Distribuidor 1 ⚠ REEMPLAZAR UBICACIÓN | `120245745859680088` |
| Proximidad — Distribuidor 2 ⚠ REEMPLAZAR UBICACIÓN | `120245745863700088` |
| Proximidad — Distribuidor 3 ⚠ REEMPLAZAR UBICACIÓN | `120245745865530088` |
| Proximidad — Distribuidor 4 ⚠ REEMPLAZAR UBICACIÓN | `120245745868630088` |
| Proximidad — Distribuidor 5 ⚠ REEMPLAZAR UBICACIÓN | `120245745880000088` |

```json
{
  "optimization_goal": "REACH",
  "billing_event": "IMPRESSIONS",
  "lifetime_budget": 344000,
  "start_time": "2026-08-01T00:00:00-0600",
  "end_time": "2026-10-19T23:59:00-0600",
  "targeting": {
    "geo_locations": {"custom_locations": [
      {"latitude": 14.6349, "longitude": -90.5069, "radius": 5, "distance_unit": "kilometer"}
    ]},
    "age_min": 18,
    "targeting_automation": {"advantage_audience": 0}
  }
}
```

Las coordenadas son el centro de Ciudad de Guatemala, **provisionales**. El ⚠ en el
nombre está para que un conjunto sin reemplazar no pase inadvertido al activar.

**Presupuesto total (`lifetime_budget`), no diario.** Gulf espera que cada
distribuidor reciba un monto fijo, y eso es exactamente lo que garantiza un
presupuesto total: Q3,440 por punto, pase lo que pase. Un presupuesto diario no
garantiza ningún total — solo un ritmo.

Además resuelve la fecha de inicio incierta: esta campaña arranca cuando el material
impreso ya esté físicamente en las tiendas, no antes. Con presupuesto total Meta
reparte el monto entre los días que queden, sin recalcular nada a mano.

⚠️ El límite de esa flexibilidad: si el arranque se corre hasta muy cerca del 19 de
octubre, Meta tiene que gastar Q3,440 en pocos días y probablemente no lo logre. Con
tres semanas o más de margen no hay problema.

Es ABO y no CBO a propósito: con presupuesto de campaña, Meta volcaría casi todo en la
zona más barata y dejaría distribuidores sin cobertura.

**Al reemplazar la ubicación, no tocar** el objetivo (REACH), el presupuesto total, ni
`advantage_audience: 0`. Solo la ubicación y, si hace falta, el radio.

Radio inicial 5 km. Si dos distribuidores quedan cerca, bajarlo a 3 km en ambos: con
radios traslapados se paga dos veces por alcanzar a la misma gente.

### Retargeting — más adelante

Alrededor del día 14, cuando haya público suficiente (~1,000 personas), vale la pena
un conjunto para quienes visitaron y no completaron: el pixel ya distingue
`Tally.FormPageView` de `Tally.FormSubmitted`. Suele ser el conjunto más barato.

## Pendientes

1. **Reemplazar la ubicación provisional** en los 5 conjuntos de proximidad.
2. **Cargar los anuncios** (lo hace el equipo). Formatos 1080×1920 para Reels/Stories
   y 1080×1350 para feed. **El QR no va en los anuncios digitales** — nadie escanea un
   código con el mismo teléfono en que lo está viendo. En digital va el enlace con UTM.
3. **Duplicar el anuncio borrador** a la campaña nueva y borrar la vieja (ZZ NO USAR).
4. **No tocar nada los primeros 7 días** de la campaña nacional: los primeros días el
   costo por resultado siempre miente.
5. **No imprimir el QR en volumen** hasta que el material esté aprobado por Gulf.

## Corregido sobre versiones anteriores de este documento

- `og:description` **no** estaba vacío: Tally lo derivaba del primer bloque de texto
  del formulario. El problema real era otro — arrancaba con 135 caracteres antes de
  llegar a los premios, y WhatsApp corta cerca de los 100, así que la tarjeta se
  partía a media enumeración. Ya se reemplazó por una descripción propia y corta.
- La pantalla manual de Medición de Eventos Agregados **no existe** en este
  portafolio; está migrado a ranking automático.
