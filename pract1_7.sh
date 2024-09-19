#!/bin/bash

# Проверка наличия аргумента
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Путь к директории
directory=$1

# Проверка существования директории
if [ ! -d "$directory" ]; then
    echo "Directory not found!"
    exit 1
fi

# Находим все файлы и их хэши
find "$directory" -type f -exec md5sum {} + | \
    sort | \
    uniq -d -w32 --all-repeated=separate
