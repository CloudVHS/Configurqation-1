#!/bin/bash

# Проверка наличия двух аргументов
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <directory> <extension>"
    exit 1
fi

# Путь к директории и расширение файлов
directory=$1
extension=$2

# Проверка существования директории
if [ ! -d "$directory" ]; then
    echo "Directory not found!"
    exit 1
fi

# Формирование имени архива
archive_name="archive_$(date +%Y%m%d%H%M%S).tar"

# Поиск файлов с указанным расширением и создание архива
find "$directory" -type f -name "*.$extension" | tar -cvf "$archive_name" -T -

# Проверка успешности создания архива
if [ $? -eq 0 ]; then
    echo "Archive created successfully: $archive_name"
else
    echo "Failed to create archive."
    exit 1
fi
