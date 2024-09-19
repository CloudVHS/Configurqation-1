# Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).
# Код
grep '.*' /etc/passwd | cut -d: -f1 | sort
# Результат
xartd0@xartd0-Strix-GL504GW-GL504GW:~$ grep '.*' /etc/passwd | cut -d: -f1 | sort
_apt
