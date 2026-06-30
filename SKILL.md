---
name: marca-horizonte-sostenible
description: Aplica la identidad de marca de Horizonte Sostenible S.A.S. B.I.C. (manual v2026.06) a cualquier pieza visual — carruseles y posts de redes, UI de diagnóstico/producto, one-pagers, propuestas visuales y papelería. Úsala siempre que Juan Felipe pida diseñar, maquetar o producir una pieza, aunque no diga "marca" o "manual"; frases como "arma el carrusel de X", "necesito una portada para Y", "maqueta el one-pager de Z" o "diséñame la pantalla de resultados del diagnóstico" la activan. Encapsula el sistema de dos capas (madre/trabajo), paleta, tipografía, logo, voz y plantillas listas por familia de pieza.
---

# Marca · Horizonte Sostenible (v2026.06)

## Cuándo usar esta skill
Úsala SIEMPRE que Juan Felipe pida **diseñar, maquetar o producir cualquier pieza visual** de Horizonte Sostenible S.A.S. B.I.C.: carruseles y posts de redes, UI del diagnóstico/producto, one-pagers, propuestas visuales, papelería (tarjeta, membrete, firma de correo), portadas, banners. Actívala aunque Juan no diga "marca" o "manual" — frases como "arma el carrusel de X", "necesito una portada para Y", "maqueta el one-pager de Z", "dame la firma de correo de W", o "diséñame la pantalla de resultados del diagnóstico" la activan.

El objetivo es que **toda pieza salga con la identidad v2026.06 a la primera**, sin que Juan tenga que recordar tokens ni reglas.

## Antes de generar (obligatorio)
1. **Decide la CAPA primero** (ver "Sistema de dos capas"). Es la decisión raíz. Si la pieza no encaja claramente en una, pregunta a Juan.
2. **Confirma la línea de servicio** si la pieza es de una línea específica (LSO / ESG / Formación), porque define el color de acento.
3. **Confirma formato de salida**: HTML→PDF (Playwright) para piezas imprimibles/enviables; HTML interactivo para web/producto. Si es ambiguo, pregunta.
4. No inventes copy regulatorio ni cifras. Datos y normas en mono, y si no estás seguro de un código (GRI/SASB/ESRS/NIIF) usa "por confirmar".

## La marca en una frase
Horizonte llega **preparado antes de que arranque el reloj regulatorio**. Ayuda a las empresas a **ordenar, activar y comunicar** su gestión ESG y su licencia social ante juntas, clientes y comunidades. No vende miedo ni humo: vende **llegar a tiempo, con criterio**.

- **Tagline:** "No vendemos sostenibilidad. Hacemos que pase."
- **Tono:** directo, técnico-claro, honesto, territorial. Un par técnico que ya hizo el trabajo, no un proveedor persiguiendo una venta.
- **La marca nunca es:** alarmista · vende-humo · decorativa · genérica.

## Sistema de dos capas (REGLA CENTRAL)
Ni oscura ni clara: las dos, con reglas. Una pieza entra por la **madre** y, al llegar a la zona de "hacer", baja a la capa de **trabajo**. **Nunca se mezclan las dos temperaturas en un mismo bloque.** La transición es intencional, no un degradado.

| | CAPA MADRE (oscura) | CAPA DE TRABAJO (clara) |
|---|---|---|
| **Cuándo** | Cuando la marca *se presenta* | Donde *se trabaja* |
| **Usos** | Hero, portadas, propuestas, **carruseles**, navegación | Cuerpo web, **formularios, diagnóstico**, tablas, SaaS |
| **Fondo** | Verde madre `#0E2A1A` | Gris-papel frío `#E4E6E3` |
| **Texto** | Crema `#F1EFE6` | Tinta `#16201A` |
| **Acento** | Ámbar `#E1A62E` (≤8%) | Bordes negros 2px |

## Color
**Capa madre:** verde 900 `#0A2114` · verde madre `#0E2A1A` · verde 700 `#16341F` · verde raíz `#1C6B3C` · ámbar `#E1A62E` · dorado rigor `#C9881F` · crema `#F1EFE6`.
**Capa de trabajo:** papel `#E4E6E3` · panel `#EDEEEA` · input `#FFFFFF` · tinta `#16201A` · dato `#5A635B` · línea `#CDD0CC`.

**Mezcla en la capa madre: 70 / 22 / 8** → 70% verde, 22% crema, 8% ámbar. **El ámbar es acento, no superficie. Si todo brilla, nada resalta.** Verde profundo y vivo, no fúnebre.

### Acentos por línea de servicio (dosis pequeñas: una franja, un ícono, un dato)
- **Licencia Social (LSO)** → verde raíz `#1C6B3C` · territorio, comunidades, confianza en campo.
- **Consultoría ESG** → dorado rigor `#C9881F` · técnico/cuantitativo: doble materialidad, NIIF S2, indicadores.
- **Formación** → terracota humano `#C75B33` · pedagogía, personas, el lado humano.

## Tipografía
- **Familjen Grotesk** (tracking −0.022em) → la VOZ. Títulos, tesis, énfasis en *itálica*. Bold 700 titulares, Semibold 600 subtítulos, Medium italic 500 énfasis.
- **IBM Plex Sans** → cuerpo, lead, etiquetas. Light 300 entradilla, Regular 400 cuerpo, Medium 500 énfasis.
- **IBM Plex Mono** → DATO: figuras, etiquetas, referencias normativas (EUDR · 30 JUN / NIIF S2 / GRI). **Nunca párrafos largos en mono.**

Las tres están en Google Fonts; `assets/tokens.css` ya las carga. No necesitas archivos locales.

## Logo / isotipo
Hoja + esfera entrelazadas con **tres destellos ✦** (los únicos elementos en ámbar; son la firma gráfica). El isotipo nunca se redibuja, deforma, rota, recolorea, ni se le añade brillo/sombra.

Variantes en `assets/` (PNG, fondo transparente):
- `isotipo-color.png` — **principal**, sobre claro (por defecto).
- `isotipo-crema.png` — reversa, sobre verde madre y foto oscura.
- `isotipo-ambar.png` — 1 tinta ámbar (grabado, sellos, monocromo).
- `isotipo-verde.png` — 1 tinta verde (documentos a una tinta sobre papel).

**Sobre fondos:** sobre verde → crema; sobre claro → color. **Nunca el isotipo a color sobre fondo oscuro** (pierde sus separadores). Tamaño mínimo: digital 32px, impreso 12mm. Área de protección = altura de un destello alrededor del isotipo.

> Falta la versión vectorial (SVG/AI) registrada — la entrega el titular de marca. Hasta entonces usa los PNG.

## Iconografía y textura
- **Glifo de marca: el destello ✦ de cuatro puntas** (con mesura). El bullet `▸` sirve en bloques mono.
- Reglas, números, etiquetas mono y la estructura hacen el trabajo de los íconos. Si de verdad se necesitan íconos de UI → **Lucide, trazo 1.5–2px**.
- **PROHIBIDO**: hojas decorativas, planetas, brotes, manos con plántulas, emoji como íconos, SVG "eco" dibujados a mano, íconos multicolor.
- Textura: trama diagonal 135° a ~2.5% blanco (`.hs-trama`) para cuerpo de "papel técnico" sin ruido.
- Radios 3·4·6·8px. Bordes 1px hairline / 2px tablero. Callout = regla de 2px + texto mono, **nunca una caja de color rellena**.

## Voz y tono
✓ **Sí:** "Protege tu negocio antes de que el reloj regulatorio arranque." · "Diagnóstico real, aunque incomode." → anticipación, no urgencia.
✕ **No:** "O cumples o te multan." · "Transformación 360° sinérgica." · "Juntos por un planeta mejor." → miedo, humo, decoración.
Reglas: sentence case · UN énfasis ámbar por titular · datos en mono · glifo ✦ · sin emoji · es-CO.

## Sí / No de diseño (lo que separa la marca del look genérico de IA)
✓ **SÍ:** elige la capa primero (madre o trabajo, nunca mezcladas) · ámbar ≤8% · datos y etiquetas en mono · verde profundo y vivo · estructura de dossier (reglas, números, ✦) · bordes 2px en capa de trabajo · la tesis a saturación.

✕ **NO — el look genérico de IA:** crema Anthropic + serif editorial + subrayados finos en titulares · morado/añil, degradados de texto, brillo neón no pedido · Inter / Geist / Instrument Serif · bento, glassmorphism, "hero + 3 tarjetas" · cliché eco (hojas, planetas, brotes, gradiente verde→azul) · emoji como íconos.

## Plantillas
En `templates/` hay arranques listos por familia de pieza. Cópialos al directorio de trabajo y adáptalos — no edites los originales.
- `carrusel-madre.html` — carrusel redes (capa madre). 1080×1350 4:5. Portada / dato / CTA.
- `diagnostico-trabajo.html` — UI producto / pantalla de resultados (capa de trabajo).
- `onepager-propuesta.html` — one-pager o propuesta visual (madre→trabajo, transición intencional).
- `papeleria.html` — tarjeta, membrete y firma de correo.

## Especificaciones de redes
Carrusel 1080×1350 (4:5, PDF) · Post 1080×1080 (1:1) · Story/Reel 1080×1920 (9:16) · Video ≤90s, 5GB · LinkedIn horizontal 1920×1080.

## Producción
- **HTML→PDF:** Playwright/Chromium. Patrón fiable: escribir HTML a disco → `viewport` al tamaño de la pieza → navegar vía `file://` → esperar ~2000ms para cargar fuentes → `page.pdf(print_background=True, margin=0)`. Para QA, rasterizar con pdf2image a 85–90 DPI.
- **HTML interactivo:** entregar HTML autocontenido; `tokens.css` puede ir embebido en `<style>` o enlazado.
- Siempre referencia los tokens de `assets/tokens.css` en vez de hardcodear hex sueltos.
