import subprocess
import unittest
from unittest.mock import patch, MagicMock
import os

# Импортируем функции из основного скрипта
from visualizer import search_package, fetch_dependencies_from_sites, generate_plantuml, render_plantuml


class TestDependencyVisualizer(unittest.TestCase):

    @patch('requests.get')
    def test_search_package_on_sites_found(self, mock_get):
        # Подменяем ответ для успешного поиска пакета на сайте
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '<html><ul class="uldep"><li><a href="#">libc6</a></li></ul></html>'
        mock_get.return_value = mock_response

        # Тестируем успешный поиск
        result = search_package('curl')
        self.assertTrue(result)
        mock_get.assert_called()

    @patch('requests.get')
    def test_search_package_on_sites_not_found(self, mock_get):
        # Подменяем ответ для случая, когда пакет не найден
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '<html></html>'
        mock_get.return_value = mock_response

        # Тестируем неудачный поиск
        result = search_package('nonexistent-package')
        self.assertFalse(result)
        mock_get.assert_called()

    @patch('requests.get')
    def test_fetch_dependencies_from_sites(self, mock_get):
        # Подменяем ответ для успешного поиска зависимостей
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '<html><ul class="uldep"><li><a href="#">libc6</a></li><a href="#">libcurl4</a></li></ul></html>'
        mock_get.return_value = mock_response

        # Тестируем извлечение зависимостей
        dependencies = fetch_dependencies_from_sites('curl', max_depth=1)
        self.assertIn('curl', dependencies)
        self.assertIn('libc6', dependencies['curl'])
        self.assertIn('libcurl4', dependencies['curl'])
        mock_get.assert_called()

    def test_generate_plantuml(self):
        # Тестируем генерацию файла .puml
        dependencies = {
            'curl': {'libc6', 'libcurl4', 'zlib1g'},
            'libc6': {'zlib1g'}
        }
        output_filename = 'test_output.puml'
        generate_plantuml(dependencies, output_filename)

        # Проверяем, что файл был создан
        self.assertTrue(os.path.exists(output_filename))

        # Удаляем файл после теста
        os.remove(output_filename)

    @patch('subprocess.run')
    def test_render_plantuml(self, mock_run):
        # Подменяем subprocess.run, чтобы проверить, что функция была вызвана
        mock_run.return_value = MagicMock(returncode=0)

        # Тестируем рендеринг PlantUML
        plantuml_path = '/path/to/plantuml.jar'
        puml_file = 'test_output.puml'
        render_plantuml(plantuml_path, puml_file)

        mock_run.assert_called_with(['java', '-jar', plantuml_path, puml_file], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

    @patch('requests.get')
    def test_search_package_on_multiple_sites(self, mock_get):
        # Подменяем ответ для всех сайтов
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '<html><ul class="uldep"><li><a href="#">libc6</a></li></ul></html>'
        mock_get.return_value = mock_response

        # Тестируем поиск по нескольким сайтам
        result = search_package('curl')
        self.assertTrue(result)
        mock_get.assert_called()

    @patch('requests.get')
    def test_fetch_dependencies_with_multiple_sites(self, mock_get):
        # Подменяем ответ для всех сайтов
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '<html><ul class="uldep"><li><a href="#">libc6</a></li></ul></html>'
        mock_get.return_value = mock_response

        # Тестируем поиск зависимостей по нескольким сайтам
        dependencies = fetch_dependencies_from_sites('curl', max_depth=1)
        self.assertIn('curl', dependencies)
        self.assertIn('libc6', dependencies['curl'])
        mock_get.assert_called()


if __name__ == '__main__':
    unittest.main()
