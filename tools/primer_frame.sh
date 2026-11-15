#!/bin/bash
# Uso: tools/primer_frame.sh video.mp4 portada.png salida.mp4  -> mete la portada 0,1 s al inicio
set -e
ffmpeg -y -loglevel error -i "$1" -loop 1 -t 0.1 -i "$2" -filter_complex "[1:v]scale=1080:1920,fps=30,format=yuv420p[c];[0:v]format=yuv420p[v];[c][v]concat=n=2:v=1:a=0[o];[0:a]adelay=100|100[a]" -map "[o]" -map "[a]" -c:v libx264 -preset veryfast -crf 20 -c:a aac -b:a 192k "$3"
