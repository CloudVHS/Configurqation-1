#!/bin/bash


if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

file=$1


if [ ! -f "$file" ]; then
    echo "File not found!"
    exit 1
fi


grep -oE '\b[a-zA-Z_][a-zA-Z0-9_]*\b' "$file" | \
    grep -vE '^[0-9]' |                            
    sort | uniq                                    
