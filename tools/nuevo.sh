#!/bin/bash
# Uso: tools/nuevo.sh <slug>   -> crea work/<slug> listo para montar
set -e; R=$(cd "$(dirname "$0")/.." && pwd); D=$R/work/$1; mkdir -p $D
[ -d $R/node_modules ] || (cd $R && npm install --silent)
ln -sfn $R/assets/brand $D/brand; ln -sfn $R/assets/mono $D/gif; ln -sfn $R/assets/poses $D/poses; ln -sfn $R/node_modules $D/node_modules
cp $R/tools/render.js $D/; echo $D
