# Трисветов Ричард Вунгович, ИКБО-63-23
# Практическое занятие №1. Введение, основы работы в командной строке.
Цель работы: Научиться выполнять простые действия с файлами и каталогами в Linux из командной строки. Сравнить работу в командной строке Windows и Linux.
## Задача №1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).
### Решение.
``` grep '.*' /etc/passwd | cut -d: -f1 | sort ```
### Пояснение.
` grep '.*' /etc/passwd ` — команда grep с регулярным выражением ` .* ` выводит все строки файла ` /etc/passwd `. Паттерн ` .* ` означает "любое количество любых символов" (включая пустую строку), поэтому это просто эквивалент чтения всего файла.

` cut -d: -f1 ` — команда cut разделяет строки по символу ` : ` и выводит первое поле, которое содержит имена пользователей.

` sort ` — команда сортирует полученные имена в алфавитном порядке.

Данную команду можно ещё упростить, отказавшись от использования ` grep `, т.к. оно избыточное, результат будет такой же, как если просто передать файл напрямую команде ` cut `.
Альтернативное решение: ` cut -d: -f1 /etc/passwd | sort `

### Результат.
```
localhost:/etc# grep '.*' /etc/passwd | cut -d: -f1 | sort
adm
at
bin
cron
cyrus
daemon
dhcp
````

## Задача №2
Вывести данные ` /etc/protocols ` в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:
```
[root@localhost etc]# cat /etc/protocols ...
142 rohc
141 wesp
140 shim6
139 hip
138 manet
```
### Решение.
``` awk '{print $2, $1}' /etc/protocols | sort -nr | head -n 5 ```
### Пояснение.
` awk '{print $2, $1}' ` — с помощью awk меняем местами столбцы (номер протокола и его имя). В файле ` /etc/protocols ` формат такой: сначала идет имя протокола, потом номер, поэтому с помощью awk выводим сначала номер, а потом имя.

` sort -nr ` — сортируем по номеру протокола в числовом порядке (` -n `), при этом в обратном порядке (` -r `), то есть от большего к меньшему.

` head -n 5 ` — выводим первые 5 строк результата.

### Результат.
```
localhost:~# awk '{print $2, $1}' /etc/protocols | sort -nr | head -n 5
103 pim
98 encap
94 ipip
89 ospf
81 vmtp
```

## Задача №3
Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):
```
[root@localhost ~]# ./banner "Hello from RTU MIREA!"
+-----------------------+
| Hello from RTU MIREA! |
+-----------------------+
```
### Решение.
Скрипт к задаче приведен ниже.
Чтобы использовать скрипт (для mac), нужно сделать скрипт исполняемым ` chmod +x banner.sh `, и запустить его, введя путь до скрипта с желаемым текстом.

```
#!/bin/bash

text="$*"
length=${#text}

# Создаем строку границы
line=$(printf '%*s' $((length + 2)) | tr ' ' '-')

# Выводим баннер
echo "+${line}+"
echo "| ${text} |"
echo "+${line}+"

```
### Пояснение.
` #!/bin/bash ` - эта строка сообщает операционной системе, что скрипт должен быть выполнен с помощью Bash (оболочка командной строки).

` text="$*" ` - ` $* ` собирает все аргументы командной строки в одну строку. Если вы запустите скрипт с аргументом "Hello", то text будет равно "Hello".
` "$*" ` заключает аргументы в двойные кавычки, чтобы сохранить пробелы в тексте.

` length=${#text} ` -  ` ${#text} ` вычисляет количество символов в переменной text. Если text равно "Hello", то length будет равно 5.

` line=$(printf '%*s' $((length + 2)) | tr ' ' '-') ` - ` printf '%*s' $((length + 2)) ` создает строку с пробелами. ` '%*s' ` — это формат для вывода строки фиксированной длины, где ` $((length + 2)) ` задает длину строки.
Команда ` tr ' ' '-' ` заменяет все пробелы в строке на символы ` - `.
Итоговая строка ` line ` будет содержать символы - и иметь длину на два символа больше, чем text. Например, если text — "Hello", то line будет "------".

```
echo "+${line}+"
echo "| ${text} |"
echo "+${line}+"
```
` echo "+${line}+" ` выводит строку с символами ` + ` и ` - ` сверху баннера.
` echo "| ${text} |" ` выводит текст с боковыми границами ` | `.
` echo "+${line}+" ` выводит строку с символами ` + ` и ` - ` снизу баннера.

### Результат.
```
(base) richardtrisvetov@MacBook-Air-3 ~ % /Users/richardtrisvetov/Desktop/config/prac1_3.sh "Hello from RTU MIREA"
+----------------------+
| Hello from RTU MIREA |
+----------------------+
```

## Задача №4
Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).

Пример для hello.c:

` h hello include int main n printf return stdio void world `
### Решение.
Ниже представлен скрипт.
```
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

```
### Пояснение.
` if [ "$#" -ne 1 ]; then ` - проверка, что передается только один аргумент (программа .c)

` if [ ! -f "$file" ]; then ` - проверка на то, что файл существует

` grep -oE '\b[a-zA-Z_][a-zA-Z0-9_]*\b' ` - извлекает слова, которые могут быть идентификаторами.

` grep -vE '^[0-9]' ` - исключает слова, начинающиеся с цифры.

` sort | uniq ` сортирует и удаляет дубликаты в одном шаге.

### Результат.
```
(base) richardtrisvetov@MacBook-Air-3 ~ % /Users/richardtrisvetov/Desktop/config/prac1_4.sh /Users/richardtrisvetov/Desktop/config/prac1_4/prac1_4/main.c
Function
arg1
arg2
exampleFunction
h
implementation
include
int
main
return
stdio
void
x
y
````

## Задача №5
Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).

Например, пусть программа называется reg:

```
./reg banner
```

В результате для banner задаются правильные права доступа и сам banner копируется в /usr/local/bin.
### Решение.
Ниже скрипт.
```
#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <command>"
    exit 1
fi

command=$1

if [ ! -f "$command" ]; then
    echo "File '$command' not found!"
    exit 1
fi

if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root!"
    exit 1
fi

cp "$command" /usr/local/bin/

chmod +x /usr/local/bin/"$command"

echo "'$command' has been registered successfully."
```
### Пояснение.
Первый блок - проверка на один переданный аргумент

Второй - проверка на наличие файла

Третий - проверка прав суперпользователя

Четвертый - копирование файла в ` /usr/local/bin `

Пятый - установка прав на выполнение

### Результат.
```
sudo /Users/richardtrisvetov/Desktop/config/prac1_5.sh banner
'banner' has been registered successfully.
```

## Задача №6
Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.

### Решение.
Скрипт ниже.
```
#!/bin/bash

# Проверка наличия аргументов
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <file1> <file2> ... <fileN>"
    exit 1
fi

# Проверка каждого переданного файла
for file in "$@"; do
    # Проверка расширения файла
    if [[ "$file" =~ \.(c|js|py)$ ]]; then
        # Проверка существования файла
        if [ ! -f "$file" ]; then
            echo "$file: File not found!"
            continue
        fi

        # Чтение первой строки файла
        first_line=$(head -n 1 "$file")
        
        # Проверка комментария в первой строке
        if [[ "$file" == *.c ]]; then
            if [[ "$first_line" =~ ^\s*// ]]; then
                echo "$file: Comment found"
            else
                echo "$file: No comment in the first line"
            fi
        elif [[ "$file" == *.js ]]; then
            if [[ "$first_line" =~ ^\s*// ]]; then
                echo "$file: Comment found"
            else
                echo "$file: No comment in the first line"
            fi
        elif [[ "$file" == *.py ]]; then
            if [[ "$first_line" =~ ^\s*# ]]; then
                echo "$file: Comment found"
            else
                echo "$file: No comment in the first line"
            fi
        fi
    else
        echo "$file: Unsupported file type"
    fi
done
```

### Результат.
```
/Users/richardtrisvetov/Desktop/config/prac1_6.c: No comment in the first line
/Users/richardtrisvetov/Desktop/config/prac1_6.js: Comment found
/Users/richardtrisvetov/Desktop/config/prac1_6.py: Comment found
````

## Задача №7
Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).

### Решение.
Скрипт ниже.
```
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
```

### Результат.
```
d41d8cd98f00b204e9800998ecf8427e  /Users/richardtrisvetov/Desktop/file1.txt
d41d8cd98f00b204e9800998ecf8427e  /Users/richardtrisvetov/Desktop/file2.txt
d41d8cd98f00b204e9800998ecf8427e  /Users/richardtrisvetov/Desktop/prac1/file4.txt
````

## Задача №8
Написать программу, которая находит все файлы в данном каталоге с расширением, указанным в качестве аргумента и архивирует все эти файлы в архив tar.

### Решение.
Скрипт ниже.
```
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
```

### Результат.
На одних данных, создал архив с файлами. На другом - пустой архив.
```
Archive created successfully: archive_20230919123045.tar
Archive created successfully: archive_20230919123045.tar
````

## Задача №9
Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.

### Решение.
Скрипт ниже.
```
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
```

### Результат.
```
This\tis\t\t a\t\t test.
Another\tline\twith\tspaces.
````


## Задача №10
Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром.

### Решение.
Скрипт ниже.
```
#!/bin/bash

# Проверка наличия одного аргумента
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

# Поиск пустых текстовых файлов и вывод их имен
find "$directory" -type f -name "*.txt" -size 0 -print

# Проверка успешности выполнения команды
if [ $? -eq 0 ]; then
    echo "Search complete."
else
    echo "Failed to perform search."
    exit 1
fi
```

### Результат.
```
/Users/richardtrisvetov/Desktop/file11.txt
/Users/richardtrisvetov/Desktop/file221.txt
Search complete.
````

# Заключение:
По истечению этой работы я научился выполнять простые действия с файлами и каталогами в Linux из командной строки, а также работать с bash и скриптами.
