#!/bin/bash
# Uso (dentro de work/<slug>, con index.html, musica.py, tiempos.json y voz.mp3):
#   ../../tools/montar.sh <nombre_salida.mp4>
set -e; OUT=${1:-video.mp4}
E=$(python3 -c "import json;print(json.load(open('tiempos.json'))['end'])")
rm -rf frames; node render.js full
python3 musica.py
ffmpeg -y -loglevel error -framerate 30 -i frames/f%04d.jpg -i musica.wav -i voz.mp3 -filter_complex \
"[2:a]apad=whole_dur=$E,asplit=2[v1][v2];[1:a]volume=0.12[m];[m][v1]sidechaincompress=threshold=0.03:ratio=8:attack=10:release=400[md];[md][v2]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.95[a]" \
-map 0:v -map "[a]" -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -c:a aac -b:a 192k -t $E "$OUT"
echo "OK $OUT"
