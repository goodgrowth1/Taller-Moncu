# Instagram → TikTok (y más adelante Shorts)

Lucía (23 nov 2026): todo reel que se publique en Instagram tiene que acabar también en TikTok, sin que ella tenga que apuntarlo en el sheet. Lo hace Claude solo. **Excepción: sorteos o vídeos de un evento concreto (p. ej. Behobia): preguntar antes a Lucía.**
YouTube Shorts: la cuenta aún no está activa. Cuando lo esté, subir allí los que mejor funcionen en TikTok, manteniendo la continuidad.

## Cómo
- Metricool, marca `8302615` (Instagram y TikTok: moncu_es), zona horaria Europe/Madrid.
- Qué hay publicado: `getAnalyticsDataByMetrics` con IGRE02, IGRE03, IGRE06, IGRE23 (Instagram reels) y TKPO02, TKPO05, TKPO03, TKPO07 (TikTok). Un reel está "subido" si el texto o el tema coincide con un vídeo de TikTok. Mira también `getScheduledPosts` para no programar dos veces.
- El vídeo sale del Drive (link del Título en el sheet o búsqueda por nombre). Metricool solo lo lee si Google Drive está vinculado en Metricool o el archivo está compartido como "cualquiera con el enlace".
- `createScheduledPost` con `providers:[{"network":"tiktok"}]`, `tiktokData.title` obligatorio (frase corta del vídeo), texto = copy de Instagram.
- Ritmo: 2 al día, a las 13:30 y a las 20:30, empezando por los que más views tuvieron en Instagram. Lo nuevo de Instagram, al día siguiente.

## Pendientes a 23 nov 2026 (orden de subida)
| Reel de Instagram | Views IG | Archivo Drive |
|---|---|---|
| ¿De qué lado corres tú? (12 nov) | 5456 | 1Mwon9Rq5AIVuYdZgVBpZ3jpS1p9fziS- |
| Correr lento te hace más rápido (13 nov) | 4701 | 1o_uiU3fXrnha06RuQmkJZo_bu4QRTp78 |
| 6 trucos para ahorrar (17 nov) | 4076 | 1SbZm4SMgYTxk9T5jOeuc6GbQAab7PeaT |
| Las de carbono (20 nov) | 3045 | 1qhHu6m1ESS_OWm88UCewAVdX16zYeFCx |
| El ticket del runner (21 nov) | 2934 | 1Dq0emKEz5kPN0Kwav1kTngRXjl9W0yhE |
| Rodilla a partir del km 8 (16 nov) | 2279 | 1vWbulac9WtYjBLE2udy81VKgGV3kDRxF |
| El lunes modo bestia, el jueves mejor mañana (19 nov) | 2014 | 1gRYCMv2S5bU20A5ZDTQvbX_FBIgB2Pxo |
| 3 trucos para tener ganas de correr (17 nov) | 1829 | 1y_6BjxrBNP1zCOXQdtsY90pEESzSgnbm |
| Sales a tope y a los 3 km te ahogas (10 nov) | 1708 | 1Mu3XZWXlxJXuXRTXra3VeRg6fsnG9UFW |
| Fuerza vs estirar (11 nov) | 1557 | 10YPTQGgZmhTK1gLGT9mcJMep251j3m4S |
| Periostitis (18 nov) | 261 | 1Z7B8bzqYhcKwufQHOLAptWsUOb6kd-XV |
| 47 insignias (14 nov) | 2875 | no encontrado en el Drive: pedir a Lucía |
| Behobia (9 nov) | 768 | 1DFpU-NAbTGqSUKIVSTuJfZqblpe5tXWj: evento pasado, preguntar |
