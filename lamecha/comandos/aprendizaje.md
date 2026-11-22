---
description: Revisa qué ha funcionado y ajusta marca, mezcla y siguientes semanas
argument-hint: "[cliente] [periodo, p. ej. últimas 2 semanas]  (puedes pegar métricas)"
---

Revisa qué ha funcionado y ajusta el sistema. Argumentos y datos: $ARGUMENTS

## 1. Reunir datos
- Cliente: el que se nombre; si no, `moncu`. Periodo: el que se diga; si no, los últimos 14 días.
- Lee `lamecha/CLAUDE.md`, `marca.md`, `historial.md` y las semanas del periodo.
- Métricas, por este orden:
  1. Las que se peguen en el mensaje (capturas, tablas, números).
  2. Instagram vía Supermetrics (`instagram_insights` o `data_query`) si está conectado: por publicación, alcance, reproducciones, retención media / % a los 3 s si existe, guardados, compartidos, comentarios, seguidores ganados.
  3. Si no hay ninguna fuente, dilo y pide los datos. **No inventes ni estimes cifras.**

## 2. Analizar
Cruza cada pieza con sus métricas y agrupa por: formato, pilar, enfoque, tipo de gancho (número, pregunta, pique, humor), duración, día de la semana y escenario/portada. Busca:
- Las 3 mejores y las 3 peores piezas, y qué tienen en común.
- Qué formato/pilar/enfoque rinde por encima o por debajo de la media.
- Qué mueve guardados y compartidos (valor) frente a qué mueve alcance (gancho).
- Si alguna regla de `marca.md` no se sostiene con los datos.
- No saques conclusiones con una sola pieza: di cuántas hay detrás de cada hallazgo.

## 3. Ajustar
- `historial.md` → sección "Resultados": una línea por pieza con sus métricas.
- `marca.md` → sección "Lo que funciona (datos)": `- (<fecha>) hallazgo (n piezas) → qué cambiamos`.
- `marca.md` → si los datos lo justifican, ajusta la "Mezcla semanal de referencia" o una regla de formato. Cambios de tono o de marca no se hacen solos: propónlos y espera un sí.
- Semanas ya generadas y no aprobadas: si algún hallazgo les afecta, propón los cambios concretos (no los apliques sin `/cambios`).
- Moncu: si un hallazgo afecta a vídeos o portadas, añádelo también a `docs/reglas-lucia.md`.

## 4. Cerrar
- Commit ("<Cliente>: aprendizaje <periodo>") y push.
- Responde en el chat con:
  - **Lo que funciona** (3 puntos máx.).
  - **Lo que no** (3 puntos máx.).
  - **Qué cambio desde ya** (reglas y mezcla actualizadas).
  - **Qué te propongo** (lo que necesita tu sí).
