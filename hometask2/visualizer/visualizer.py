import requests
from bs4 import BeautifulSoup
import subprocess
import sys


def search_package(package_name):
    sites = [
        "jammy",
        "noble",
        "oracular",
        "plucky"
    ]

    for site in sites:
        print(f"Ищу пакет {package_name} на сайте версии ОС {site}")

        url = f"https://packages.ubuntu.com/{site}/{package_name}"

        response = requests.get(url)

        if response.status_code != 200:
            print(f"Пакет не найден на сайте версии ОС {site}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        dep_lists = soup.find_all('ul', class_='uldep')

        if dep_lists:
            print(f"Пакет найден на сайте версии ОС {site}")
            return True
        else:
            print(f"Пакет не найден на сайте версии ОС {site}")

    print(f"Пакет {package_name} не найден на всех сайтах")
    return False


def fetch_dependencies_from_sites(package_name, max_depth, visited=None):
    if visited is None:
        visited = set()

    if not search_package(package_name):
        return {}

    url = f"https://packages.ubuntu.com/focal/{package_name}"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Ошибка загрузки страницы для {package_name}: {response.status_code}")
        return {}

    soup = BeautifulSoup(response.text, 'html.parser')

    dep_lists = soup.find_all('ul', class_='uldep')

    if not dep_lists:
        print(f"Зависимости для пакета {package_name} не найдены.")
        return {package_name: set()}

    dependencies = set()

    for dep_list in dep_lists:
        for link in dep_list.find_all('a'):
            dep_package = link.get_text().strip()
            if dep_package:
                dependencies.add(dep_package)

    if not dependencies:
        print(f"Зависимости для пакета {package_name} не найдены.")
        return {package_name: set()}

    for dep in dependencies.copy():
        if dep not in visited:
            visited.add(dep)
            sub_dependencies = fetch_dependencies_from_sites(dep, max_depth, visited)
            dependencies.update(sub_dependencies)

    return {package_name: dependencies}


def generate_plantuml(dependencies, output_filename):
    with open(output_filename, 'w') as file:
        file.write('@startuml\n')
        for package, deps in dependencies.items():
            for dep in deps:
                print(f"Создаю связь: {package} --> {dep}")
                file.write(f'"{package}" --> "{dep}"\n')
        file.write('@enduml\n')

    print(f".puml файл с зависимостями записан в {output_filename}")


def render_plantuml(plantuml_path, puml_file):
    result = subprocess.run(['java', '-jar', plantuml_path, puml_file],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Ошибка при генерации изображения:", result.stderr.decode())
    else:
        print("Изображение успешно сгенерировано.")


def main(package_name, plantuml_path, max_depth=3):
    print(f"Ищем зависимости для пакета {package_name}...")
    dependencies = fetch_dependencies_from_sites(package_name, max_depth)

    if not dependencies:
        print(f"Зависимости для {package_name} не найдены.")
        return

    output_filename = f"{package_name}_dependencies.puml"
    generate_plantuml(dependencies, output_filename)

    render_plantuml(plantuml_path, output_filename)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python visualizer.py <package_name> [max_depth]")
        sys.exit(1)

    package_name = sys.argv[1]
    plantuml_path = "./plantuml.jar"
    max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else 2

    main(package_name, plantuml_path, max_depth)
