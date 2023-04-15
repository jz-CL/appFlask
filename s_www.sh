#!/bin/bash


if [ "$1" = "--n" ]; then
    argument=$2
    echo "+----------------------------------------+"
    echo "nazwa:  $argument."
    export FLASK_APP=$argument
    flask run
    echo "+----------------------------------------+"


else
    echo "Błąd: 
    
    --n nazwa"	
fi
