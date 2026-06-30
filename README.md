# Marca · Horizonte Sostenible — Skill de diseño

Skill de [Claude](https://claude.ai) que aplica automáticamente la identidad de marca de **Horizonte Sostenible S.A.S. B.I.C.** (manual **v2026.06**) a cualquier pieza visual: carruseles, UI de producto, one-pagers, propuestas y papelería.

El objetivo es que cualquier persona del equipo pueda pedirle a Claude *"arma el carrusel de X"* o *"maqueta el one-pager de Y"* y la pieza salga con la identidad correcta **a la primera**, sin tener que recordar tokens, colores ni reglas.

> **Tagline:** *No vendemos sostenibilidad. Hacemos que pase.*

---

## Qué hace

Cuando esta skill está disponible, Claude:

1. Reconoce cualquier petición de diseño de una pieza de Horizonte (aunque no se mencione "marca" o "manual").
2. Decide la **capa** correcta (madre / trabajo) antes de maquetar.
3. Aplica tipografía, paleta, logo, voz y reglas de la identidad v2026.06.
4. Parte de una **plantilla** lista por familia de pieza y la adapta al encargo.
5. Produce el resultado en **HTML→PDF** (Playwright) o **HTML interactivo**, según la pieza.

---

## Estructura del repositorio

```
marca-horizonte-sostenible/
├── SKILL.md                      # Reglas de marca destiladas (lo que Claude lee)
├── README.md                     # Este archivo
├── assets/
│   ├── tokens.css                # Variables CSS + clases de las dos capas
│   ├── isotipo-color.png         # Logo principal (sobre claro)
│   ├── isotipo-crema.png         # Reversa (sobre verde / foto oscura)
│   ├── isotipo-ambar.png         # 1 tinta ámbar (monocromo)
│   └── isotipo-verde.png         # 1 tinta verde (papel, una tinta)
├── templates/
│   ├── carrusel-madre.html       # Carrusel redes · capa madre · 1080×1350
│   ├── diagnostico-trabajo.html  # UI producto · capa de trabajo
│   ├── onepager-propuesta.html   # One-pager / propuesta · madre→trabajo
│   └── papeleria.html            # Tarjeta, membrete y firma de correo
└── scripts/
    └── render.py                 # Renderiza cualquier plantilla a PDF + PNG (QA)
```

---

## Cómo instalarla (para usar la skill con Claude)

La skill vive en el directorio de skills de usuario de Claude. Copia la carpeta completa **sin renombrarla ni separar sus archivos** (las plantillas referencian `../assets/` con rutas relativas):

```bash
git clone https://github.com/Jftorres135-bit/skill-identidad-marca-horizonte-sostenible.git
# Copia la carpeta a tu directorio de skills de Claude
```

Una vez disponible, basta con pedirle a Claude una pieza. No hay que invocar la skill manualmente.

---

## La marca en 30 segundos

### Sistema de dos capas (regla central)
Toda pieza es **una** de estas dos temperaturas. **Nunca se mezclan en un mismo bloque.**

| | **Capa madre** (oscura) | **Capa de trabajo** (clara) |
|---|---|---|
| Cuándo | La marca *se presenta* | Donde *se trabaja* |
| Usos | Hero, portadas, carruseles | Formularios, diagnóstico, tablas |
| Fondo | Verde madre `#0E2A1A` | Papel `#E4E6E3` |
| Texto | Crema `#F1EFE6` | Tinta `#16201A` |
| Acento | Ámbar `#E1A62E` (≤8%) | Bordes negros 2px |

### Tipografía
- **Familjen Grotesk** — títulos, tesis, énfasis. La voz de la marca.
- **IBM Plex Sans** — cuerpo y etiquetas.
- **IBM Plex Mono** — datos, normas y figuras (nunca párrafos).

Las tres se cargan desde Google Fonts en `tokens.css`; no requieren instalación local.

### Acentos por línea de servicio
- **Licencia Social (LSO)** → verde raíz `#1C6B3C`
- **Consultoría ESG** → dorado rigor `#C9881F`
- **Formación** → terracota humano `#C75B33`

El detalle completo de paleta, logo, iconografía, voz y los "sí / no" de diseño está en [`SKILL.md`](./SKILL.md).

---

## Renderizar una pieza a PDF (sin Claude)

Cualquier persona del equipo puede maquetar editando una plantilla y renderizándola:

```bash
pip install playwright pdf2image
playwright install chromium
# (Linux) instalar poppler para los PNG de QA: sudo apt-get install poppler-utils

python scripts/render.py templates/carrusel-madre.html --width 1080 --height 1350
```

Genera un PDF en `out/` y una vista PNG para revisión rápida. Ver `scripts/render.py --help`.

---

## Convenciones para contribuir

- **No edites las plantillas originales** al crear una pieza: cópialas a tu carpeta de trabajo y adapta la copia.
- **No hardcodees colores hex sueltos.** Usa las variables de `tokens.css` (`var(--hs-green)`, etc.).
- Si cambias la identidad (nuevo color, nueva regla), actualiza **`SKILL.md` y `tokens.css` juntos**, y describe el cambio en el commit.
- Mantén el versionado de marca en el encabezado (`v2026.06`). Si hay una revisión de marca, sube la versión.

---

## Pendientes conocidos

- **Isotipo vectorial (SVG/AI):** el manual lo marca como pendiente de entrega por el titular de marca. La skill usa los PNG (nítidos hasta ~512px). Para impresión grande, reemplazar por el vectorial cuando exista — las plantillas lo tomarán sin cambios.

---

*Identidad de marca v2026.06 · Horizonte Sostenible S.A.S. B.I.C. · Uso interno.*
