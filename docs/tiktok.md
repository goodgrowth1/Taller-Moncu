# Instagram → TikTok (y más adelante Shorts)

Lucía (23 nov 2026): todo reel que se publique en Instagram tiene que acabar también en TikTok, sin que ella tenga que apuntarlo en el sheet. Lo hace Claude solo. **Excepción: sorteos o vídeos de un evento concreto (p. ej. Behobia): preguntar antes a Lucía.**
YouTube Shorts: la cuenta aún no está activa. Cuando lo esté, subir allí los que mejor funcionen en TikTok, manteniendo la continuidad.

## Cómo
- Metricool, marca `8302615` (Instagram y TikTok: moncu_es), zona horaria Europe/Madrid.
- Qué hay publicado: `getAnalyticsDataByMetrics` con IGRE02, IGRE03, IGRE06, IGRE23 (Instagram reels) y TKPO02, TKPO05, TKPO03, TKPO07 (TikTok). Un reel está "subido" si el texto o el tema coincide con un vídeo de TikTok. Mira también `getScheduledPosts` para no programar dos veces.
- El vídeo sale del Drive (link del Título en el sheet o búsqueda por nombre). Metricool (plan gratis) no puede vincular Drive, así que: **copia el vídeo con `copy_file` a la carpeta "TikTok copias con enlace (no tocar)" (ID `12PcmLRPJUOjqAQXAGDf3-9OJhpqcjAIc`, compartida como cualquiera con el enlace) con nombre `tt_<tema>.mp4`** y pasa a Metricool el link de la copia. Los originales se quedan privados. Funciona también con los vídeos de Santi.
- `createScheduledPost` con `providers:[{"network":"tiktok"}]`, `tiktokData.title` obligatorio (frase corta del vídeo), texto = copy de Instagram.
- Ritmo: 2 al día, a las 13:30 y a las 20:30, empezando por los que más views tuvieron en Instagram. Lo nuevo de Instagram, al día siguiente.

## Límites y estado (23 nov, noche)
- Antes de programar, mirar el final: el logo del cierre tiene que ser la cara del mono, nunca la palabra MONCU.
- Límites del conector: Drive solo descarga archivos de menos de 10 MB y solo se suben archivos de menos de ~3,1 MB (comprimir con crf 28 y tune animation si hace falta).
- Lado (ahora 29 nov 20:30), Rodilla, Sales a tope y Fuerza se quedaron en BORRADOR en Metricool (llevan la marca de agua MONCU pequeña y el sistema no dejó volver a activarlos desde aquí). Lucía puede activarlos en Metricool o pedírmelo. El resto sigue programado.

## Programado el 23 nov 2026 (Metricool, TikTok)
- 23 nov 20:30 ¿De qué lado corres tú?
- 24 nov 13:30 Correr lento · 20:30 6 trucos para ahorrar
- 25 nov 13:30 Carbono · 20:30 El ticket del runner
- 26 nov 13:30 Rodilla km 8 · 20:30 El jueves
- 27 nov 13:30 3 trucos ganas de correr · 20:30 Sales a tope
- 28 nov 13:30 Fuerza vs estirar · 20:30 Periostitis

## Revisión 24 nov 2026 (mañana)
- En Instagram no hay reels nuevos desde el 21 nov. Todo lo del 9 al 21 nov está publicado, programado o en borrador en TikTok, salvo los pendientes de abajo. No se ha programado nada.
- Borradores sin tocar: Lado 29 nov 20:30, Rodilla 26 nov 13:30, Sales a tope 27 nov 20:30, Fuerza 28 nov 13:30.

## Revisión 25 nov 2026 (mañana)
- Programado: «Baja de 25 min en tu 5K» (IG 23 nov, 4797 views) para el 29 nov 13:30. Copia `tt_baja25_5k.mp4` (ID `1UUTQ0tmYqnXEd4FPHgwQ59U8Wi1w9_jP`). Final comprobado: cara del mono y «LINK EN LA BIO», sin la palabra MONCU.
- 24 nov 13:30 Correr lento y 20:30 6 trucos: publicados en TikTok.
- Borradores sin tocar: Lado 29 nov 20:30, Rodilla 26 nov 13:30, Sales a tope 27 nov 20:30, Fuerza 28 nov 13:30.
- Calendario TikTok lleno hasta el 29 nov. Primer hueco libre: 30 nov 13:30.

## Revisión 26 nov 2026 (mañana)
- Programado: «Gemelos siempre cargados» (IG 25 nov, 317 views) para el 30 nov 13:30. Copia `tt_gemelos.mp4` (ID `1QCi7_52UcjNmjMBaRPSszrMllTgbIFhI`). Final comprobado: cara del mono y «GUÁRDALO», sin la palabra MONCU.
- 25 nov Carbono y Ticket: ya no están en la cola, se dan por publicados.
- Borradores sin tocar: Lado 29 nov 20:30, Rodilla 26 nov 13:30, Sales a tope 27 nov 20:30, Fuerza 28 nov 13:30.
- Calendario TikTok lleno hasta el 30 nov 13:30. Primer hueco libre: 30 nov 20:30.

## Pendientes
- Black Friday «¿Cuántos Moncus necesitas…? Cero» (IG 24 nov, 716 views, y 25 nov, 158 views; vídeos en el Drive: `Reel 1 · Tragaperras Black Friday.mp4` ID `1yKphVCtXwV7u_T3i1kK9QwMz3EQKqz-v` y `Reel 2 · Ticket Black Friday.mp4` ID `1-9ZNckrGk12Xgl9oxg4AFWERbW0dwHu0`). Campaña con fecha (hasta el 29 nov) y los huecos de 13:30 y 20:30 están llenos hasta el 30. No programado: preguntar a Lucía si los quiere en TikTok (en otro horario antes del 29 o en lugar de algún borrador).
- «Comenta garmin y participa!» (IG 24 nov, 173 views): sorteo, preguntar a Lucía.
- Tres reels del 24 nov en Instagram que no están en el sheet ni en el Drive: «Comenta GARMIN y gana miles de premios» (1 view), «Comenta CORRER y gana miles de premios GRATIS!» (16 views) y «Comenta CORRER, la app que te premia por correr» (149 views). Hablan de premios, sorteos, «gratis» y «puntos». Preguntar a Lucía si se suben a TikTok y dónde está el vídeo.
- 47 insignias (14 nov, 2875 views IG): no está en el Drive con ese nombre. El único vídeo parecido es `moncu_medallas_v2.mp4` (ID `10Ie_PkdU6xs89Wvf1pk-bZruNdb8FmDa`, 17 s, «Tu app te da una medalla», acaba con la cara del mono), pero no es seguro que sea el mismo y lleva «GRATIS» y la zapatilla Adidas. Preguntar a Lucía antes de subirlo.
- Reel del 29 sep («Quién te diga que correr no te da productos gratis», 688 views IG): no está en TikTok ni se encuentra en el Drive. Además dice «gratis» y lleva 11 hashtags con marcas. Preguntar a Lucía si se sube.
- Behobia (9 nov): evento pasado, preguntar a Lucía antes (archivo 1DFpU-NAbTGqSUKIVSTuJfZqblpe5tXWj).
