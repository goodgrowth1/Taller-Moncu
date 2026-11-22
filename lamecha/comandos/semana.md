---
description: Genera la semana entera de contenido de un cliente
argument-hint: "[cliente] [fecha del lunes, p. ej. 30 nov]  (por defecto: moncu, la semana que viene)"
---

Genera la semana completa de contenido. Argumentos: $ARGUMENTS

## 1. Situarte
- Cliente: el primero de los argumentos si es una carpeta de `lamecha/clientes/`; si no, `moncu`.
- Semana: de lunes a domingo. Si se da una fecha, la semana que la contiene; si no, la semana que viene (el próximo lunes). El archivo será `lamecha/clientes/<cliente>/semanas/AAAA-MM-DD.md` con la fecha del lunes.
- Si el archivo ya existe, **no lo pises**: dilo y propone `/cambios`.

## 2. Leer (obligatorio, entero)
1. `lamecha/CLAUDE.md`
2. `lamecha/clientes/<cliente>/marca.md`
3. `lamecha/clientes/<cliente>/historial.md`
4. Las 2 últimas semanas de `semanas/`, si existen, para no repetir estructura ni ganchos.
5. Moncu: el calendario de Google Sheets (ID y columnas en `CLAUDE.md`), filas de esa semana. Si no puedes leerlo, sigue con el historial y avísalo al final.

## 3. Decidir el plan
- **Si el calendario ya tiene piezas esa semana**: respétalas (fecha, formato, título). Tu trabajo es desarrollarlas. Puedes proponer cambiar alguna si choca con `marca.md` o repite el historial, pero como sugerencia aparte, sin cambiarla tú.
- **Si hay huecos o la semana está vacía**: completa con la "Mezcla semanal de referencia" de `marca.md`, alternando pilares (no dos reels del mismo pilar el mismo día ni tres seguidos) y tirando del mapa de ángulos (`docs/02-bases-mapa-contenido.md`), con ángulos que no estén en el historial.
- **Fechas señaladas** de la semana (Black Friday, Navidad, San Silvestre, Reyes…): úsalas.
- **HUECOs de lanzamiento** (Plane): no los rellenes sin brief. Déjalos como `HUECO` y apúntalos en "Te necesito".
- Ninguna idea, título ni gancho puede estar ya en `historial.md`.

## 4. Escribir cada pieza
Sigue al pie de la letra las reglas de formato de `marca.md`. Para cada pieza:

- **Reel (IA)**: gancho (seg. 0-1, con número), guion completo para voz (≤70 palabras, ≤30 s, lista con Moncu como último punto), texto en pantalla por bloque, escenario/plano propuesto (distinto de los ya usados), idea de portada (estilo distinto a las anteriores), copy y hashtags.
- **Reel grabado**: idea, planos, texto en pantalla, audio/trend sugerido, copy.
- **Carrusel**: texto de cada slide (6-10), palabra clave destacada por slide, copy y hashtags.
- **Story**: tipo (encuesta, quiz, pregunta, compartir, repost), texto exacto y sticker.
- **LinkedIn / Blog / Newsletter / Post**: texto completo (blog: título SEO, H2 y borrador).
- Datos que no sepas seguro: `[CONFIRMAR: ...]`. Nunca inventes estudios, cifras de la app ni casos.

Antes de dar una pieza por buena, repásala contra las reglas: palabras prohibidas, máximo 5 hashtags, copy que no repite la portada, palabra SEO en la primera línea, duración del reel, morado y lima puntual en lo visual.

## 5. Formato del archivo

```markdown
# <Cliente> · Semana del <lun d mes> al <dom d mes AAAA>
Estado: borrador

## Resumen
| Día | Formato | Pilar | Enfoque | Título |
|---|---|---|---|---|
| lun 23 nov | Reel (IA) | 1 Constancia | Motivación | ... |

## Lunes 23 nov
### Reel (IA) · <Título>
- **Pilar / enfoque**: ...
- **Gancho (0-1 s)**: ...
- **Guion (voz)**: ...
- **En pantalla**: ...
- **Escenario y plano**: ...
- **Portada**: ...
- **Copy**:
  > ...
- **Hashtags**: ...

(…resto de piezas del día y del resto de días…)

## Te necesito
- Datos por confirmar, HUECOs sin brief, sugerencias de cambio en el calendario.
```

## 6. Cerrar
- Guarda el archivo, haz commit ("<Cliente>: semana del <d mes>") y push.
- Responde en el chat solo con: la tabla resumen, la lista "Te necesito" y la ruta del archivo. Sin explicar el proceso.
- No toques el calendario ni el historial todavía: eso pasa cuando se apruebe la semana con `/cambios`.
