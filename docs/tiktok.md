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
- Antes de programar, revisar el final del vídeo: tiene que acabar con el mono (logo_cara), nunca con la palabra MONCU. Si la lleva, se corrige tapando la palabra y poniendo el logo (ver work/fixlogo en la sesión del 23 nov: drawbox con el color de fondo + overlay de logo_cara a 150 px con fundido).
- Límites del conector: Drive solo descarga archivos de menos de 10 MB y solo se pueden subir archivos de menos de ~3,1 MB. Los vídeos de 40-55 s pesan 7-27 MB.
- Por eso TODO lo programado está en BORRADOR en Metricool (no se publica) y la revisión diaria está pausada hasta que Lucía decida cómo seguir.

## Programado el 23 nov 2026 (ahora en borrador) (Metricool, TikTok)
- 23 nov 20:30 ¿De qué lado corres tú?
- 24 nov 13:30 Correr lento · 20:30 6 trucos para ahorrar
- 25 nov 13:30 Carbono · 20:30 El ticket del runner
- 26 nov 13:30 Rodilla km 8 · 20:30 El jueves
- 27 nov 13:30 3 trucos ganas de correr · 20:30 Sales a tope
- 28 nov 13:30 Fuerza vs estirar · 20:30 Periostitis

## Pendientes
- 47 insignias (14 nov, 2875 views IG): no está en el Drive, pedir a Lucía.
- Behobia (9 nov): evento pasado, preguntar a Lucía antes (archivo 1DFpU-NAbTGqSUKIVSTuJfZqblpe5tXWj).
