## 1. Команды для сборки и запуска проекта

### Установка необходимых библиотек:

   ```bash
   ppip install -r requirements.txt (requests, beautifulsoup4)
   ```

### Запуск проекта

   ```bash
   python visualizer.py <название пакета> <глубина>
   ```
#### Пример:

   ```bash
   python visualizer.py iptables 2
   ```

### Проверка

   ```bash
    python ./tests.py
   ```
---

## 2. Вывод программы

### После генерации граф может выглядеть так:

![output](https://github.com/CloudVHS/Configurqation-1/blob/main/hometask2/iptables_dependencies.png)

### Результаты прогона тестов:

![image](https://github.com/CloudVHS/Configurqation-1/blob/main/hometask2/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-12-16%20%D0%B2%2015.24.18.png)

---
