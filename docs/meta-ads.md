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
https://ganacongulf.com/?utm_source=meta&utm_campaign=gana_con_gulf&utm_content=reel_premio
```

Primer parámetro con `?`, los siguientes con `&`. Quien entra por el **QR impreso**
llega al dominio pelado y esas columnas quedan vacías — eso identifica el tráfico
orgánico/impreso sin necesidad de un QR distinto por canal.

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

## Pendientes antes de poner dinero

1. **Prueba limpia.** Todos los eventos hasta ahora salieron con el código de test
   `TEST76491` y no cuentan como tráfico real: el conjunto de datos marca 0 eventos en
   28 días y la conversión tiene `last_fired_time: null`. Hay que entrar desde un
   teléfono en navegación normal, con los UTM en la URL, y enviar el formulario.
   Semáforo verde = el contador deja de ser 0 y la conversión registra su primer
   disparo.
2. **Borrar los envíos de prueba** en Tally → Submissions (no solo en Sheets).
   Ojo: el formulario bloquea teléfonos duplicados, así que hay que borrar el registro
   viejo antes de volver a probar.
3. **Decidir sobre coincidencias avanzadas** con el cliente.
4. **`og:description` sigue vacío** — la vista previa en WhatsApp no muestra
   descripción.
5. **No imprimir el QR en volumen** hasta cerrar la prueba de punta a punta.
