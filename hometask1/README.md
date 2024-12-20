# Эмулятор для оболочки языка OS

## 1. Общее описание

Этот проект представляет собой эмулятор оболочки языка OS, реализованный на Python. Эмулятор поддерживает базовые команды командной строки, такие как `ls`, `cd`, `exit`, `mkdir`, `clear` и `rmdir`. Все действия пользователя логируются в формате JSON с временными метками, а виртуальная файловая система загружается из архива zip.

### Основные особенности:
- Эмуляция команд UNIX-подобной оболочки.
- Поддержка виртуальной файловой системы, загружаемой из архива zip.
- Логирование всех действий пользователя.
- Поддержка базовых команд для работы с файлами и директориями.

### Описание всех функций и настроек

- **Описание**: Инициализирует эмулятор оболочки.
- **Параметры**:
  - `username`: Имя пользователя для эмулятора.
  - `fs_path`: Путь к архиву tar с виртуальной файловой системой.
  - `log_path`: Путь к файлу для записи логов.

## 2. Запуск
Запуск эмулятора
```bash
python emulator.py
```

## 3. Запуск тестов
```bash
python tests.py
```

## 4. Пример использования:

![image](https://github.com/CloudVHS/Configurqation-1/blob/main/hometask1/test_emulator.jpg)

## 5. Результаты прогона тестов:

![image](https://github.com/CloudVHS/Configurqation-1/blob/main/hometask1/test_photo.png)
