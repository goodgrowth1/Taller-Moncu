---
description: Aplica tus correcciones a una semana y guarda lo aprendido
argument-hint: "[cliente] [semana] tus correcciones  (o \"aprobado\" para cerrar la semana)"
---

Aplica estas correcciones: $ARGUMENTS

## 1. Situarte
- Cliente: el que se nombre; si no, `moncu`.
- Semana: la que se nombre (fecha o "esta"/"la que viene"); si no, el archivo más reciente de `lamecha/clientes/<cliente>/semanas/`.
- Lee `lamecha/CLAUDE.md`, `marca.md` y el archivo de la semana antes de tocar nada.

## 2. Aplicar las correcciones
- Cambia solo lo que se pide. No reescribas piezas que no se han mencionado.
- Si la corrección afecta a algo repetido en otras piezas de la semana (por ejemplo, "no uses 'compi'"), aplícala en todas y dilo.
- Si una pieza cambia de idea o título, comprueba que la nueva no está en `historial.md`.
- Si una corrección choca con `marca.md`, aplícala igualmente (la persona manda) y pregunta si debe pasar a ser regla.
- Si algo es ambiguo, haz la versión más probable y señálalo; no bloquees por una duda pequeña.

## 3. ¿Es una regla para siempre?
Para cada corrección decide:
- **Solo de esta pieza** (un dato, un cambio de gusto puntual) → se queda en la semana.
- **Sirve para el futuro** (tono, palabra prohibida, estructura, estilo visual, formato) → además añádela a `marca.md`, sección "Reglas aprendidas", así: `- (<fecha de hoy>, <quién>) <regla en una línea>`. Si deja obsoleta una regla anterior, actualiza la anterior en su sitio y dilo.
  - Moncu: si la regla afecta a vídeos o portadas, añádela también a `docs/reglas-lucia.md` para que la tarea nocturna de montaje la sepa.
- En la duda, pregunta al final en una línea: "¿Guardo X como regla?".

## 4. Si dice "aprobado" (toda la semana o piezas sueltas)
1. Cambia `Estado:` del archivo a `aprobado` (o marca las piezas aprobadas con ✅).
2. Pasa las piezas aprobadas a `historial.md` (sección "Publicado o hecho", con estado "Aprobado") y quítalas de "Ya planificado" si estaban.
3. Moncu: vuelca al calendario de Google Sheets las piezas aprobadas, solo en filas sin link y sin estado "Publicado…": columna **H Copy / notas** (conservando cualquier "Nota:" que ya hubiera debajo) y **F Estado** = `Guion listo` en los Reels (IA) con guion. Nunca borres ni reordenes filas. Para Reels (IA) añade el guion al Google Doc "Guiones para voz" de la carpeta *Voces Claude* como indica `../RUNBOOK.md`. Si no puedes escribir en Google, dilo y deja el contenido listo en el archivo.

## 5. Cerrar
- Guarda, commit ("<Cliente>: cambios semana del <d mes>") y push.
- Responde breve: qué has cambiado (una línea por pieza), qué reglas nuevas has guardado y cualquier pregunta pendiente.
