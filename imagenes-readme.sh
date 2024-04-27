#!/bin/sh

# Borro todas las viejos links que tenia a las imagenes 
sed -i '/!\[foto](.\/informe-imagenes\/informe-[[:digit:]].png)/d' README.md

cantFotos=$(ls informe-imagenes/ | wc -l)

for ((i = 0; i < $cantFotos; i++)); do
    echo "![foto](./informe-imagenes/informe-"${i}".png)" >> README.md 
done
