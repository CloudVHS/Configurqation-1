import unittest
from unittest.mock import patch
from io import StringIO

from emulator import *


class TestShellEmulator(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_pwd(self, mock_stdout):
        emulator = ShellEmulator("config.toml")
        emulator.pwd()
        self.assertIn(str(emulator.current_dir), mock_stdout.getvalue())  # Проверяем, что путь текущей директории выводится

    @patch('sys.stdout', new_callable=StringIO)
    def test_pwd_empty(self, mock_stdout):
        emulator = ShellEmulator("config.toml")
        emulator.current_dir = Path(".")
        emulator.pwd()
        self.assertIn(".", mock_stdout.getvalue())  # Проверяем другой путь директории

    @patch('sys.stdout', new_callable=StringIO)
    def test_cd_valid(self, mock_stdout):
        emulator = ShellEmulator("config.toml")
        emulator.file_system[Path("dir1")] = None  # Добавляем директорию в виртуальную файловую систему
        emulator.cd("dir1")
        self.assertIn("Changed directory to", mock_stdout.getvalue())  # Проверяем, что команда выполнена

    @patch('sys.stdout', new_callable=StringIO)
    def test_cd_invalid(self, mock_stdout):
        emulator = ShellEmulator("config.toml")
        emulator.cd("non_existent_dir")
        self.assertIn("No such directory: non_existent_dir", mock_stdout.getvalue())  # Проверяем ошибку

    @patch('sys.stdout', new_callable=StringIO)
    def test_ls_empty(self, mock_stdout):
        emulator = ShellEmulator("config.toml")
        emulator.cd("dir2")
        emulator.ls()
        self.assertIn("No items in current directory", mock_stdout.getvalue())  # Проверка вывода при пустой директории

    @patch('sys.stdout', new_callable=StringIO)
    def test_ls_with_items(self, mock_stdout):
        emulator = ShellEmulator("config.toml")
        emulator.ls()
        self.assertIn("dir1\ndir2\nfile2.txt\n", mock_stdout.getvalue())  # Проверяем, что файл выводится

    @patch('sys.stdout', new_callable=StringIO)
    def test_mkdir(self, mock_stdout):
        emulator = ShellEmulator("config.toml")
        emulator.mkdir("new_dir")
        self.assertIn("Directory new_dir created", mock_stdout.getvalue())  # Проверка создания директории

    @patch('sys.stdout', new_callable=StringIO)
    def test_mkdir_existing(self, mock_stdout):
        emulator = ShellEmulator("config.toml")
        emulator.file_system[Path("existing_dir")] = None
        emulator.mkdir("existing_dir")
        self.assertIn("Directory existing_dir already exists", mock_stdout.getvalue())  # Проверка попытки создать уже существующую директорию

    @patch('sys.stdout', new_callable=StringIO)
    def test_rmdir(self, mock_stdout):
        emulator = ShellEmulator("config.toml")
        emulator.file_system[Path("dir_to_remove")] = None
        emulator.rmdir("dir_to_remove")
        self.assertIn("Directory dir_to_remove removed", mock_stdout.getvalue())  # Проверка удаления директории

    @patch('sys.stdout', new_callable=StringIO)
    def test_rmdir_not_found(self, mock_stdout):
        emulator = ShellEmulator("config.toml")
        emulator.rmdir("non_existent_dir")
        self.assertIn("No such directory: non_existent_dir", mock_stdout.getvalue())  # Проверка ошибки при удалении несуществующей директории

    @patch('sys.stdout', new_callable=StringIO)
    @patch('os.system')
    def test_clear(self, mock_system, mock_stdout):
        emulator = ShellEmulator("config.toml")
        emulator.clear()
        mock_system.assert_called_with("cls")  # Проверка вызова команды очистки экрана

    @patch('sys.stdout', new_callable=StringIO)
    def test_exit(self, mock_stdout):
        emulator = ShellEmulator("config.toml")
        with self.assertRaises(SystemExit):
            emulator.exit_shell()  # Проверка вызова выхода из программы
        self.assertIn("Exiting shell...", mock_stdout.getvalue())  # Проверка вывода при выходе из программы

if __name__ == '__main__':
    unittest.main()
