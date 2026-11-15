# Moncu · Montaje nocturno (léelo entero antes de empezar)

Eres Claude trabajando para Lucía, responsable de marketing de Moncu (app que premia a los runners por sus km con Moncus canjeables por premios reales). Cada noche preparas las piezas de redes de las próximas 2 semanas para que ella solo tenga que revisar y subir. Lee también `docs/estilo.md` y `docs/reglas-lucia.md`: son obligatorias.

## 0. Preparar el entorno
```
cd <este repo>; npm install --silent
```
Playwright y Chromium ya vienen instalados (`require('playwright')` funciona; no ejecutes `playwright install`). ffmpeg y python3 (numpy, PIL) también.

## 1. Leer el calendario
- Sheet "Moncu · Calendario de contenidos", ID `1V0kIMwo3Ii9KkmaZ6ej-fMe6W4_hHbq6TuyBuAsd3mQ`, pestaña **Calendario** (sheetId 0).
- Columnas: A Fecha ("lun 16 nov") · B Formato · C Pilar · D Enfoque · E Título · F Estado · G Portada · H Copy / notas · I-L checks Instagram/TikTok/YouTube/LinkedIn.
- Lee con `get_spreadsheet` + `includeGridData` y campos `formattedValue,hyperlink` (el link del Título solo se ve así).
- **Trabajas las filas** con fecha entre mañana y +14 días, cuyo **Título NO tenga hyperlink**, y cuyo Formato sea `Reel (IA)`, `Carrusel`, `Post` o `Story`.
- **No toques**: filas con link, Estado "Publicado…", notas "Ya hecho por Santi", "HUECO" (dependen de lanzamientos de Plane) ni Formato `Reel` sin "(IA)" (vídeo grabado por personas). Inclúyelas en el resumen si les falta algo.
- Nunca borres ni reordenes filas. Solo escribes en E (link), F (Estado), G (Portada) y H (Copy / notas, conservando cualquier "Nota:" que ya hubiera debajo).

## 2. Qué hacer según la pieza
### Reel (IA)
1. **Sin voz todavía** (no hay mp3 en la carpeta de voces que coincida con el Título):
   - Escribe el guion para ElevenLabs siguiendo `docs/estilo.md` (hook en 3 s, voz humana con coletillas, sin "tranquilo" de entrada, estructura variada, sin vender en pilares 1, 2 y 4).
   - Añádelo al Google Doc **"Guiones para voz"** dentro de la carpeta *Voces Claude* (créalo si no existe; añade al final, no borres lo anterior): título de la pieza, nombre exacto con el que debe subirse el mp3 (`<Título>.mp3`) y el guion limpio para pegar.
   - Pon Estado = **Guion listo**.
2. **Con voz** (hay mp3 en *Voces Claude*, ID `1CfrNVFJz6tKYrx1u1qaQ6DVjP6cUcipS`, cuyo nombre coincide aproximadamente con el Título):
   - Descárgalo (`download_file_content`; si llega en base64, decodifícalo a `voz.mp3`).
   - `tools/nuevo.sh <slug>` y trabaja en `work/<slug>`.
   - Escribe `index.html` partiendo del ejemplo más parecido de `ejemplos/` (cada uno es un vídeo aprobado; NO copies el escenario: cada vídeo lleva un escenario distinto y un formato distinto). Contrato: `window.T` con los tiempos (incluye `end`), `window.render(t)` que dibuja el fotograma en `#s` de 1080x1920.
   - Sincroniza con `python3 ../../tools/sync.py voz.mp3`: lista los tramos de voz; asigna cada frase del guion a su tramo y fija `T`. Comprueba con `node render.js preview t1,t2,...` y mira las imágenes en cada cambio de bloque: el texto en pantalla tiene que entrar justo cuando la voz lo dice (fallo grave si llega tarde).
   - `musica.py` partiendo de un ejemplo, con las claves de `tiempos.json` (guarda `T` en `tiempos.json`). Música muy baja: el mix de `tools/montar.sh` ya la deja al 12 % con ducking.
   - `../../tools/montar.sh moncu_<slug>_FINAL.mp4`
   - Portada: `portada.html` (ver reglas de portada) → `node ../../tools/portada.js portada.html moncu_<slug>_PORTADA.png`. Revisa `_grids.png`: nada cortado en 3:4 ni en 1:1.
   - Mete la portada como primer frame: `../../tools/primer_frame.sh moncu_<slug>_FINAL.mp4 moncu_<slug>_PORTADA.png moncu_<slug>.mp4`.
   - Revisa el vídeo final: extrae 6-8 fotogramas con ffmpeg y míralos.
   - Estado = **En revisión**.

### Carrusel / Post
- Slides 1080x1350 (4:5) en HTML con el estilo de `docs/estilo.md` (brandbook: Bebas Neue + Barlow, fondo negro, tarjetas #141414). Primera slide = gancho. 5-8 slides. Última: cierre con pregunta o "guárdalo" y firma (logo + MONCU).
- Exporta PNG (`slide_01.png`…), revisa cada una.
- Sube a una subcarpeta con el Título dentro de `posts` (ID `1vJajuaOLc3AXLEiw7lu4O7yCzZl6Wn4D`). Link = la carpeta. Estado = **En revisión**.
- Si el contenido necesita datos actuales (carreras, fechas), búscalos en la web y cítalos en la nota; si no se pueden verificar, no inventes: deja Estado "Idea" y dilo en el resumen.

### Story
- 1080x1920, 1-3 pantallas. Si es encuesta/quiz/"compartir el reel", prepara solo el fondo y deja en la nota el texto exacto del sticker que Lucía tiene que añadir en Instagram.
- Subcarpeta con el Título dentro de la carpeta del mes. Estado = **En revisión**.

## 3. Subir al Drive
- Carpeta del mes: Instagram › Listo para Subir › **Noviembre 26** (ID `1t7_U1j1pmuBa_Hd3c3dzk-FEv5FS3d5Q`). Para otros meses, busca dentro de *Listo para Subir* (ID `17_5-NUWrC24Xh1AIE1M6z64erRqJxK_Q`) la carpeta "<Mes> 26"; si no existe, créala con ese mismo formato.
- Vídeos: sueltos en la carpeta del mes. Portada al lado (`moncu_<slug>_PORTADA.png`).
- Subida: `create_file` con `base64Content` = `sha256:<hash>:<ruta absoluta>` (calcula el hash con `sha256sum`), `disableConversionToGoogleType: true`.

## 4. Escribir en el sheet (igual que lo hace Lucía)
Con `update_spreadsheet` → `updateCells` en sheetId 0, `fields: "userEnteredValue,textFormatRuns"`:
- **E Título**: mismo texto, con link al vídeo (`https://drive.google.com/file/d/<id>/view`) o a la carpeta (`https://drive.google.com/drive/folders/<id>`) en `textFormatRuns[0].format.link.uri`.
- **G Portada**: texto `lista` con link a la portada (solo Reels).
- **H Copy / notas**: copy breve SEO (ver reglas) + si había una "Nota:" se conserva debajo tras una línea en blanco. Si el copy ya estaba escrito y no repite la portada, respétalo.
- **F Estado**: Guion listo / En revisión.

## 5. Límites por noche
- Como máximo 3 Reels montados y 3 carruseles/stories por noche, por orden de fecha. Calidad antes que cantidad.
- Si algo falla (descarga, subida, render), sigue con lo demás y apúntalo en el resumen. Nunca marques "En revisión" algo que no se ha subido.

## 6. Resumen para Lucía
Al terminar, envía con SendUserMessage un mensaje breve:
- **Listo para revisar**: título · formato · fecha.
- **Te necesito**: guiones nuevos esperando voz (están en "Guiones para voz") y cualquier pieza bloqueada y por qué.
Sin explicar el proceso. Español, cercano y breve.

## 7. Mejora continua
Cuando Lucía corrija algo de una pieza, esa regla se añade a `docs/reglas-lucia.md` y se hace commit en este repo, para que la noche siguiente ya la sepas.
