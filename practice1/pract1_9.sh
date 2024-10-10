#!/bin/bash

# Проверка наличия двух аргументов
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <input_file> <output_file>"
    exit 1
fi

# Путь к входному и выходному файлам
input_file=$1
output_file=$2

# Проверка существования входного файла
if [ ! -f "$input_file" ]; then
    echo "Input file not found!"
    exit 1
fi

# Замена последовательностей из 4 пробелов на символ табуляции и запись в выходной файл
sed 's/    /\t/g' "$input_file" > "$output_file"

# Проверка успешности выполнения команды
if [ $? -eq 0 ]; then
    echo "Replacement complete. Output saved to: $output_file"
else
    echo "Failed to perform replacement."
    exit 1
fi
