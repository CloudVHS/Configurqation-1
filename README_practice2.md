## Задача №1
Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?

### Решение. 1 часть.
``` pip show matplotlib ```

### Результат.
```
(base) richardtrisvetov@MacBook-Air-3 prac2 % pip show matplotlib
Name: matplotlib
Version: 3.5.2
Summary: Python plotting package
Home-page: https://matplotlib.org
Author: John D. Hunter, Michael Droettboom
Author-email: matplotlib-users@python.org
License: PSF
Location: /Users/richardtrisvetov/opt/anaconda3/lib/python3.9/site-packages
Requires: cycler, fonttools, kiwisolver, numpy, packaging, pillow, pyparsing, python-dateutil
Required-by: seaborn
````
### Решение. 2 часть.

Чтобы получить пакет matplotlib без использования менеджера пакетов, вы можете скачать его напрямую из репозитория.

` git clone https://github.com/matplotlib/matplotlib.git ` - создает локальную копию репозитория на пк.

` cd matplotlib ` - переход в директорию пакета

` python setup.py install ` - установка matplotlib


## Задача №2
Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?

### Решение. Часть 1.
Чтобы вывести служебную информацию о пакете express (после того, как были установлены Node.js и npm), нужно ввести следующую команду:

``` npm show express ```

### Результат.
```
npm show express

express@4.21.0 | MIT | deps: 31 | versions: 279
Fast, unopinionated, minimalist web framework
http://expressjs.com/

keywords: express, framework, sinatra, web, http, rest, restful, router, app, api

dist
.tarball: https://registry.npmjs.org/express/-/express-4.21.0.tgz
.shasum: d57cb706d49623d4ac27833f1cbc466b668eb915
.integrity: sha512-VqcNGcj/Id5ZT1LZ/cfihi3ttTn+NJmkli2eZADigjq29qTlWi/hAQ43t/VLPq8+UX06FCEx3ByOYet6ZFblng==
.unpackedSize: 220.8 kB

dependencies:
accepts: ~1.3.8      etag: ~1.8.1         qs: 6.13.0           
body-parser: 1.20.3  finalhandler: 1.3.1  range-parser: ~1.2.1 
content-type: ~1.0.4 fresh: 0.5.2         safe-buffer: 5.2.1   
cookie: 0.6.0        http-errors: 2.0.0   send: 0.19.0         
debug: 2.6.9         methods: ~1.1.2      statuses: 2.0.1      
depd: 2.0.0          on-finished: 2.4.1   type-is: ~1.6.18     
encodeurl: ~2.0.0    parseurl: ~1.3.3     utils-merge: 1.0.1   
escape-html: ~1.0.3  proxy-addr: ~2.0.7   vary: ~1.1.2         
(...and 7 more.)

maintainers:
- wesleytodd <wes@wesleytodd.com>
- dougwilson <doug@somethingdoug.com>
- linusu <linus@folkdatorn.se>
- sheplu <jean.burellier@gmail.com>
- blakeembrey <hello@blakeembrey.com>
- ulisesgascon <ulisesgascondev@gmail.com>
- mikeal <mikeal.rogers@gmail.com>

dist-tags:
latest: 4.21.0  next: 5.0.0     

published 2 weeks ago by wesleytodd <wes@wesleytodd.com>
````
### Решение. Часть 2.
Чтобы получить пакет прямо из репозитория без использования менеджера пакетов, нужно клонировать репозиторий вручную.

``` git clone https://github.com/expressjs/express.git ``` - клонирование репозитория

``` cd express ``` - переход в нужную нам папку

В репозитории есть файл package.json, который содержит информацию о зависимостях, необходимых для работы пакета. Эти зависимости можно скачать и подключить вручную:
для этого надо найти зависимости в разделе "dependencies" файла package.json.
Надо загрузить необходимые библиотеки напрямую из их репозиториев или сайтов и добавить их в проект. Также можно использовать npm.

## Задача №3
Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.
```bash
pipdeptree --packages matplotlib --graph-output dot > matplotlib_deps.dot
### Результат.
Вот такой получился [граф](https://github.com/CloudVHS/Configurqation-1/blob/main/matplotlibgraph.png).

### Решение. Для express.
Аналогично, для express.

``` npm show express dependencies ``` - для вывода зависимостей

На выходе получим:

```
(base) richardtrisvetov@MacBook-Air-4 my-express-app % npm show express dependencies

{
  qs: '6.13.0',
  depd: '2.0.0',
  etag: '~1.8.1',
  send: '0.19.0',
  vary: '~1.1.2',
  debug: '2.6.9',
  fresh: '0.5.2',
  cookie: '0.6.0',
  accepts: '~1.3.8',
  methods: '~1.1.2',
  'type-is': '~1.6.18',
  parseurl: '~1.3.3',
  statuses: '2.0.1',
  encodeurl: '~2.0.0',
  'proxy-addr': '~2.0.7',
  'body-parser': '1.20.3',
  'escape-html': '~1.0.3',
  'http-errors': '2.0.0',
  'on-finished': '2.4.1',
  'safe-buffer': '5.2.1',
  'utils-merge': '1.0.1',
  'content-type': '~1.0.4',
  finalhandler: '1.3.1',
  'range-parser': '~1.2.1',
  'serve-static': '1.16.2',
  'array-flatten': '1.1.1',
  'path-to-regexp': '0.1.10',
  setprototypeof: '1.2.0',
  'cookie-signature': '1.0.6',
  'merge-descriptors': '1.0.3',
  'content-disposition': '0.5.4'
}
```

Graphviz использует текстовое описание графа, называемое DOT, чтобы визуализировать зависимости в виде диаграмм. 
Вот код для отображения зависимостей пакета.

```

digraph express_dependencies {
    "express" -> "qs: 6.13.0";
    "express" -> "depd: 2.0.0";
    "express" -> "etag: ~1.8.1";
    "express" -> "send: 0.19.0";
    "express" -> "vary: ~1.1.2";
    "express" -> "debug: 2.6.9";
    "express" -> "fresh: 0.5.2";
    "express" -> "cookie: 0.6.0";
    "express" -> "accepts: ~1.3.8";
    "express" -> "methods: ~1.1.2";
    "express" -> "type-is: ~1.6.18";
    "express" -> "parseurl: ~1.3.3";
}
```
### Результат.
Вот такой получился [граф](https://github.com/CloudVHS/Configurqation-1/blob/main/expressgraph.png).



## Задача №4
Изучить основы программирования в ограничениях. Установить MiniZinc, разобраться с основами его синтаксиса и работы в IDE.
Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.

### Решение.
Я ознакомился с основами синтаксиса MiniZink.

Решение задачи о счастливых билетах:
```
% Определение переменных
array[1..6] of var 0..9: digits; % Цифры билета

% Ограничение на уникальность цифр
constraint all_different(digits);

% Ограничение на сумму первых и последних трех цифр
constraint sum(digits[1..3]) = sum(digits[4..6]);

% Минимизация суммы первых трех цифр
var int: sum_first_three = sum(digits[1..3]);
solve minimize sum_first_three;

% Печать решения
output [
    "Digits: ", show(digits), "\n",
    "Sum of first three digits: ", show(sum_first_three), "\n"
];

 ```

### Результат.
```
Digits: [1, 2, 3, 0, 2, 4]
Sum of first three digits: 6
````
## Задача №5
Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже (рисунок можно найти в методичке).

### Решение.

```
include "globals.mzn";

% Определяем версии пакетов
enum Version = {v1_0_0, v1_1_0, v1_2_0, v1_3_0, v1_4_0, v1_5_0, v1_8_0, v2_0_0, v2_1_0, v2_2_0, v2_3_0};

% Определяем пакеты
enum Package = {root, menu, dropdown, icons};

% Зависимости пакетов
array[Package] of set of Version: dependencies = [
    {v1_0_0, v1_1_0, v1_2_0, v1_3_0, v1_4_0, v1_5_0}, % menu
    {v1_8_0, v2_0_0, v2_1_0, v2_2_0, v2_3_0}, % dropdown
    {v1_0_0, v2_0_0} % icons
];

% Пример ограничения: root зависит от menu версии 1.5.0
constraint root in dependencies[menu];

solve satisfy; какой ответ покажет этот код на minizink

 ```

### Результат.
```
root = v1_0_0
menu = v1_0_0
dropdown = v1_8_0
icons = v1_0_0
````

## Задача №6
Решить на MiniZinc задачу о зависимостях пакетов для следующих данных:
```
root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0.
foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0.
foo 1.0.0 не имеет зависимостей.
left 1.0.0 зависит от shared >=1.0.0.
right 1.0.0 зависит от shared <2.0.0.
shared 2.0.0 не имеет зависимостей.
shared 1.0.0 зависит от target ^1.0.0.
target 2.0.0 и 1.0.0 не имеют зависимостей.
```

### Решение.

```
include "globals.mzn";

% Определяем версии пакетов
enum Version = {v1_0_0, v1_1_0, v2_0_0};

% Определяем пакеты
enum Package = {root, foo, left, right, shared, target};

% Зависимости пакетов
array[Package] of set of Version: dependencies = [
    {v1_0_0},     % root
    {v1_0_0},     % foo
    {v1_0_0},     % left
    {v1_0_0},     % right
    {v1_0_0, v2_0_0}, % shared
    {v2_0_0}      % target
];

% Ограничения
% root зависит от foo ^1.0.0 и target ^2.0.0
constraint root in dependencies[foo] /\ root in dependencies[target];

% foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0
constraint foo in dependencies[left] /\ foo in dependencies[right];

% left 1.0.0 зависит от shared >=1.0.0
constraint left in dependencies[shared];

% right 1.0.0 зависит от shared <2.0.0
constraint right in dependencies[shared];

% shared 1.0.0 зависит от target ^1.0.0
constraint shared in dependencies[target];

% shared 2.0.0 не имеет зависимостей, поэтому никаких ограничений не нужно

% target 2.0.0 и 1.0.0 не имеют зависимостей, поэтому никаких ограничений не нужно

solve satisfy;

 ```

### Результат.
```
root = v1_0_0
foo = v1_0_0
left = v1_0_0
right = v1_0_0
shared = v1_0_0
target = v2_0_0
````
## Задача №7
Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему ограничений надо построить автоматически, по метаданным.

### Решение.
Для того чтобы представить задачу о зависимостях пакетов в более общем виде, можно использовать структуру данных, такую как словарь в питоне, которая будет содержать метаданные о пакетах и их зависимостях.

Пакет: имя пакета, версии пакета, зависимости (другие пакеты и их версии)
Зависимости: зависимости могут быть описаны как список кортежей, где каждый кортеж содержит название зависимого пакета и его необходимую версию.

Я сделал такую структуру (ниже):
```
packages = {
    "root": {
        "versions": ["1.0.0"],
        "dependencies": [("foo", "1.0.0"), ("target", "2.0.0")]
    },
    "foo": {
        "versions": ["1.0.0", "1.1.0"],
        "dependencies": [("left", "1.0.0"), ("right", "1.0.0")]
    },
    "left": {
        "versions": ["1.0.0"],
        "dependencies": [("shared", ">=1.0.0")]
    },
    "right": {
        "versions": ["1.0.0"],
        "dependencies": [("shared", "<2.0.0")]
    },
    "shared": {
        "versions": ["1.0.0", "2.0.0"],
        "dependencies": [("target", "1.0.0")]  # shared 1.0.0 зависит от target ^1.0.0
    },
    "target": {
        "versions": ["1.0.0", "2.0.0"],
        "dependencies": []
    }
}

 ```
А также функция для проверки зависимостей:

```
def check_dependencies(package_name):
    package = packages[package_name]
    for dependency, version in package["dependencies"]:
        if dependency not in packages:
            return f"Package {dependency} not found."
        
        # Проверяем, соответствует ли версия зависимостям
        if version.startswith(">="):
            min_version = version[2:]
            if not any(v >= min_version for v in packages[dependency]["versions"]):
                return f"Dependency {dependency} does not meet the version requirement."
        elif version.startswith("<"):
            max_version = version[1:]
            if not any(v < max_version for v in packages[dependency]["versions"]):
                return f"Dependency {dependency} does not meet the version requirement."
        else:
            if version not in packages[dependency]["versions"]:
                return f"Dependency {dependency} version {version} not found."

    return f"All dependencies for {package_name} are satisfied."

# Проверка зависимостей для пакета 'root'
print(check_dependencies("root"))

```

### Результат.
```
All dependencies for root are satisfied.
````
