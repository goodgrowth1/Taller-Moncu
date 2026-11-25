# Reglas de Lucía (prevalecen sobre estilo.md si chocan)

## Marca
- Se escribe "Moncu" (con C). La moneda se llama "Moncus", nunca "puntos".
- Logo = cara del mono con gorra (`assets/brand/logo_cara.png`). Nunca la palabra "MONCU" en una caja blanca como logo. Moncus siempre con la moneda oficial (`moneda_moncu.png`). Premios con las imágenes reales de producto (`prod_*.png`).
- **El morado manda.** Santi quiere menos amarillo: el lima #E5F38B solo como toque puntual (una palabra o un detalle, por ejemplo las medallas de una portada). Nunca varios elementos lima.
- Premium siempre en dorado #E8B84A.
- Profesional y sobrio, nada infantil ni con muchos colores.

## Mono
- No dibujar cuerpos ni poses nuevas a mano: queda "cutre". Usar los fotogramas oficiales (`assets/mono/m00-m46.png`, ciclo `floor(t*24)%47`) y las poses de `assets/poses/`. Retoques pequeños sobre fotogramas oficiales (cara de preocupación, bocadillo de pensamiento) sí.
- Variar el plano: zoom, congelado, plano corto. No siempre corriendo de lado.

## Guiones (voz ElevenLabs, Mark Dou – Global Modern Narrator)
- Hook potente en los 3 primeros segundos; el runner tiene que sentirse identificado y llevarse valor.
- Moncu solo entra como último punto de la lista (ver plantilla). Siempre habla como Moncu ("En Moncu nos dimos cuenta…"), nunca "hay apps como Moncu".
- Variar estructura (no siempre "3 consejos: 1, 2, 3") y tono. No empezar con "tranquilo". No abusar de "compi".
- Voz humana, rápida, con coletillas. Nunca "morir" (usar "sufrir").
- Con energía y ritmo: los guiones planos se rechazan.
- **Acento castellano de España, nunca latino** (Lucía, 23 nov: "Baja de 25" salió con acento latino y hay que rehacerlo). Al pedir la voz, elegir en ElevenLabs una voz con acento de España y comprobarlo antes de montar.
- **Más corto y con más ritmo** (Lucía, 23 nov, sobre "Baja de 25": unos 15 s, no 30). Ritmo en todo: en lo que se dice, en cómo se dice y en el montaje. Guion de ~40 palabras para 15 s.

## Plantilla obligatoria de reel (18 nov 2026, datos de retención de Instagram)
Los reels pierden el 40-46 % en los 3 primeros segundos si arrancan con una pantalla de texto quieta, y la gente se va hacia el segundo 12-20. "6 trucos para ahorrar" es el único con meseta (~45 % hasta el final de la lista) y "47 insignias" (16 s, acaba en la app) es el que más convierte.
1. **Duración 20-30 s, nunca más de 30** (guion de ~70 palabras como máximo). Si una idea necesita más, no es un reel: avisa a Lucía para hacerla carrusel.
2. **Segundo 0-1: el mono corriendo con la promesa encima**, con un número y un beneficio concretos ("6 trucos para ahorrar"). Nunca una pantalla de texto quieta. Promesa amplia, que enganche a cualquier runner, no solo a quien tiene el problema.
3. **Segundo 1-25: lista rápida, ~3 s por punto**, con "Truco 1", "Truco 2"... en pantalla y un antes y un después visual cuando se pueda.
4. **El último punto de la lista es Moncu, dentro de la lista y nunca después** ("y el último: que te paguen por correr"). Luego solo 1-2 s de cierre con el logo real y "link en la bio".
5. El humor con el que el runner se identifica es lo que más se comparte: úsalo en el gancho y en los puntos.
Esta plantilla prevalece sobre "pilares 1, 2 y 4 no venden": ahora todos los reels rematan con Moncu como último punto.

## Vídeo
- Música muy baja, nunca protagonista.
- No acelerar vídeos enteros de forma uniforme (se nota). Si hay que dar ritmo, se retoca por bloques.
- Sincronía exacta: cada tarjeta/texto entra cuando la voz lo dice.
- Logo real al final (cara con gorra), con "LINK EN LA BIO" cuando el vídeo es de Pilar 3.
- **El logo del cierre (cuando invitamos a descargar la app) es SIEMPRE la cara del mono (`logo_cara.png` o `icon.png`), nunca un cuadrado con la palabra "MONCU".** Lucía, 23 nov: ya se había pedido muchas veces. Revisar el último fotograma de cada vídeo que se toque, también los de Santi (p. ej. "Medallas que no te puedes poner" llevaba la palabra; corregido en moncu_medallas_v2).

## Portadas
- **Variar el estilo de cada portada** (Lucía, 19 nov): no repetir siempre la plantilla "icono + pill morada + titular + firma". Alternar conceptos visuales (pase VIP con sello, gráfica, objeto protagonista, textura de fondo, composición en diagonal...) manteniendo colores de marca y zona segura del grid.
- Gancho que genere ganas de entrar; se entiende en un segundo. Nada tachado ni confuso.
- Todo centrado entre y≈440 y y≈1480 para sobrevivir al recorte del grid (3:4 y 1:1). Comprobar siempre con `_grids.png`.
- Pill morada con la pregunta/contexto + titular enorme en Anton blanco con una parte en #B6A4FF o lima puntual. Firma pequeña logo + MONCU.
- Sin coletillas tipo "Spoiler…" debajo del titular salvo que se pida.
- La portada va como primer frame del vídeo.
- **La portada NO replica el vídeo** (Lucía, 22 nov): concepto, fondo y recurso distintos a los del vídeo (p. ej. vídeo oscuro con cronómetro → portada morado vivo con el mono y un bocadillo). Titular clarísimo y directo, lo primero que se lee.
- Portadas de reel: morado vivo o fondos de marca, texto centrado y un toque divertido (bocadillo, líneas de velocidad, sticker). El fondo lavanda claro es solo para carruseles.
- En el sheet, la celda Portada lleva solo el texto **lista** con el link a la imagen; nunca la descripción.

## Carruseles y stories (Lucía, 22 nov 2026)
- **El mensaje principal es el título, enorme.** Si la pieza va de Black Friday, "BLACK FRIDAY" ocupa media pantalla; nunca en una etiqueta pequeña.
- **Fuera las etiquetas/píldoras pequeñas** ("QUÉ ES", "TIPO 1 DE 6", "BLACK FRIDAY · MONCU"...). Solo si hacen falta de verdad. El "DESLIZA" de la primera slide sí.
- **Menos texto, más imagen.** Producto real (zapatillas, geles, ropa, reloj...) con `assets/brand/prod_*.png`; ilustraciones del mono. Nunca inventar productos ni usar fotos que no sean nuestras.
- **3 slides por defecto** (gancho · contenido · CTA). Más solo si el formato lo pide (listas tipo "tipos de runner").
- Claro, directo, grande y llamativo. Variar el fondo: morado vivo (#7B5CF0 → #5B3FD0) para lo promocional, negro para lo informativo. Nada de todo negro con texto pequeño: queda monótono.
- Tono cercano y directo, hablándole al runner en segunda persona e imperativo: "Baja de 25 min en tu 5K", no "Bajar de 25 min en 5K". Nada de infinitivos ni frases generalistas en títulos, hooks y copies.
- Tono cercano, hablando al runner ("Oye, que esta semana...").
- **Una story = un mensaje.** Si en el calendario una story junta dos cosas (Black Friday + sorteo), se hacen dos stories y se separa la fila en el sheet.
- Referencia aprobada: story del sorteo Trofeo Akiles (morado vivo, titular enorme con caja negra, número gigante).

## Copy
- Breve, SEO (palabras que busca el runner en la primera línea), cierre con pregunta o "Guárdalo".
- **Nunca repetir el texto de la portada**: el copy la complementa.
- **Máximo 5 hashtags** (límite de Instagram desde dic 2025; con más no se publica o se recortan). Específicos del tema antes que genéricos: 1 de nicho del tema, 1-2 de comunidad runner en España, 1 de formato o intención y #moncu. Nunca de relleno (#reels, #explore, #instagood).
- SEO: la palabra que busca el runner va en la primera línea del copy (Instagram indexa el texto, no solo los hashtags).
- Nada de dos puntos en prosa ni frases que suenen a IA.

## Tienda nueva + Black Friday (Lucía, 23 nov 2026)
- La tienda nueva (categorías Nutrición, Salud, Ropa, Zapatillas, Accesorios) y el Black Friday van juntos en un solo mensaje: "abrimos tienda nueva y, por Black Friday, todos los descuentos a 0 Moncus". No separar en piezas que hablan solo de una cosa.
- Nunca llamar a Moncu "marketplace" en el contenido.
- Se pueden usar capturas reales de la app (grabación de Lucía) en vídeos y carruseles.
- **Black Friday es toda la semana**, no solo el viernes. Decirlo siempre ("Black Friday toda la semana", "hasta el domingo 29") para que no parezca que la tienda o los descuentos llegan el viernes.
- **"0 Moncus" tiene que destacar**: es el gancho. Grande, en su propio bloque (tarjeta blanca o número gigante), nunca como una línea más.

## Escritura (Lucía, 23 nov 2026)
- **Nada de "·" entre palabras** (ni en slides, ni en copies, ni en notas): queda a IA. Usar comas, saltos de línea o frases normales.

## Mono en acción (Lucía, 23 nov 2026)
- Si el mono tiene que hacer algo (abrir una persiana, arreglar, señalar), usar la ilustración que encaje (`mantenimiento.webp` para abrir o arreglar, `mapa.webp` recortado para señalar) y animarla con saltos, squash y giros. No el ciclo de correr si no está corriendo.

## Proceso (Lucía, 22 nov 2026)
- **Todo de una vez, sin pedir permiso entre pasos.** Guion → voz en ElevenLabs → montaje → portada → subida al Drive → sheet. Lucía no tiene que pedir cada paso; si un paso se bloquea, se dice en el resumen qué falta exactamente y se deja todo lo demás listo.
- Voz: generarla por la API de ElevenLabs (necesita `api.elevenlabs.io` permitido y la API key). Desde el Chrome de Lucía se puede generar, pero el mp3 se queda en su ordenador: no sirve para la tarea nocturna.

## Voz (Lucía, 23 nov 2026)
- **Voz por defecto: Mark Dou – Global Modern Narrator** (Lucía, 24 nov: le gusta, no quiere voz de señor mayor; nada de Martin Osborne). Tiene que sonar de España: solo salió latina en el vídeo «Baja de 25». Antes de montar, escuchar el audio; si suena latino, regenerar (mismo modelo y ajustes que los audios buenos de Mark Dou, idioma español de España si la interfaz lo permite).
- **Reels cortos: 15-20 s.** Guion de ~40-50 palabras. 3-4 puntos muy breves, sin relleno.
- Nunca el punto medio "·" entre palabras en textos, copies ni piezas: parece escrito por IA.

## Hashtags y sheet (Lucía, 23 nov 2026)
- **Hashtags: siempre con el banco de `docs/seo-redes.md`** (datos reales de Instagram). Nada de inventarlos. 5 máximo: tema + comunidad en español + comunidad España + formato + #moncu.
- **Publicado en el sheet:** cuando Lucía avise de que algo está subido, se marca la fila entera (A-G) con fondo gris #D9D9D9 (el 4.º gris empezando por el blanco). No tocar ese color en otras filas.

## Black Friday y tienda: 0 Moncus NO es gratis (24 nov)
- En Moncu cada producto tiene un descuento que se canjea gastando Moncus. «0 Moncus» = ese descuento se aplica sin gastar Moncus. Nunca decir ni dar a entender que algo es gratis («todo a 0», «TOTAL 0», «PAGADO CON 0»). Fórmula: «descuentos a 0 Moncus».
- Enseñar producto real con su precio, el descuento y los Moncus tachados a 0 (estilo `work/_comun/producto.css`, ejemplo `work/tienda_v2/cards.py`).
- Productos: usar los recortes de `assets/productos/` (capturas de la tienda del 24 nov, fondo limpio). No usar las zapatillas Adidas (`prod_shoe`); de calzado/ropa solo Blue Banana. Si un producto no se recorta bien, pedir a Lucía una captura mejor.
- No llamar «marketplace» a Moncu en el contenido.

## CTA de cierre en reels y carruseles (24 nov)
- Todos los reels y carruseles acaban con el bloque lima «COMENTA [MONCU] / y te mandamos el link para descargarte la app 📲» (clase `.cta` en `work/_comun/base.css`; en reels va en la tarjeta final, con la cara del mono debajo). Sustituye a «Link en la bio».
- En el copy, la línea «Comenta MONCU y te mandamos el link para descargarte la app 📲» va justo antes de los hashtags.

## Portadas de reel y cuadrícula (24 nov)
- La cuadrícula del perfil recorta la portada a 3:4 por el centro (y 240 a 1680 en 1080x1920). Todo el texto y lo importante tiene que caber ahí; comprobar con el recorte antes de subir.
- Fondo negro con rayos para la campaña Black Friday: le gusta.

## Hashtags (24 nov, sustituye a lo anterior)
- Fórmula: 1 de tema + #running #runners #correr #runningespaña (ver docs/seo-redes.md). Nada de #corredores, #correresvida, #carreraspopulares ni tags de frase.
- Palabra clave en la primera frase del copy.

## Reels: ritmo, repetición y CTA (25 nov)
- Máximo 20 s. Muy al grano: gancho, claves y cierre, sin relleno.
- Voz más rápida pero no excitada ni gritona (si hace falta, atempo ~1.1 y pausas cortas).
- No repetir consejos ya usados en otros vídeos (p. ej. «si no puedes hablar, vas rápido» está quemado). Antes de escribir un guion, revisar los guiones y copies anteriores.
- «Comenta MONCU» NO va en todas las piezas: no seguidas ni en todo. Variar el CTA según la pieza: «Guárdalo y mándaselo a tus colegas del run club», guardar, etiquetar, pregunta...
- Si hace falta, crear músicas nuevas para no repetir siempre la misma base.

## No perder lo que ya funciona (25 nov)
- Al aplicar un cambio nuevo, no quitar ni sustituir elementos que ya estaban y le gustaban, salvo que Lucía lo pida expresamente.
- Cierre de reels para guardar: la cara del mono y debajo «GUÁRDALO» en letra blanca grande (el estilo de siempre). No usar la caja lima de «Comenta MONCU» para guardar.
- No meter la coletilla de Moncus al final de los consejos («cada kilómetro suave también suma Moncus»). El cierre es «Guárdalo» y ya está.
