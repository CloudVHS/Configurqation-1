#!/bin/bash

text="$*"
length=${#text}

# Создаем строку границы
line=$(printf '%*s' $((length + 2)) | tr ' ' '-')

# Выводим баннер
echo "+${line}+"
echo "| ${text} |"
echo "+${line}+"
