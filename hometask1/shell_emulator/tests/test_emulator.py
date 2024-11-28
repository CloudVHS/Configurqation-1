import unittest
import tempfile
import shutil
import zipfile
import os
from emulator import ShellEmulator
import json
import io
import sys
from unittest import mock
import pathlib


class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.config_path = os.path.join(self.temp_dir, "config.toml")
        self.vfs_path = os.path.join(self.temp_dir, "vfs.zip")
        self.log_path = os.path.join(self.temp_dir, "emulator.log")

        with open(self.config_path, "w") as f:
            f.write(f"""
user = "testuser"
vfs_path = "{self.vfs_path}"
log_path = "{self.log_path}"
""")

        with zipfile.ZipFile(self.vfs_path, 'w') as zipf:
            zipf.writestr("file1.txt", "content1")
            zipf.writestr("subdir/file2.txt", "content2")


    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_ls_empty(self):
        emulator = ShellEmulator(self.config_path)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        emulator._ls(["/nonexistent"]) #Проверка несуществующей директории
        sys.stdout = sys.__stdout__
        self.assertIn("Директория не найдена.", captured_output.getvalue())

    def test_ls_non_empty(self):
        emulator = ShellEmulator(self.config_path)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        emulator._ls([])  # Проверка текущей директории
        sys.stdout = sys.__stdout__
        self.assertIn("file1.txt", captured_output.getvalue())


    def test_cd_success(self):
        emulator = ShellEmulator(self.config_path)
        emulator._cd(["subdir"])
        self.assertEqual(emulator.current_dir, os.path.join(emulator._load_vfs(), "subdir"))

    def test_cd_failure(self):
        emulator = ShellEmulator(self.config_path)
        emulator._cd(["nonexistent"])
        self.assertEqual(emulator.current_dir, emulator._load_vfs()) # Проверка, что директория не изменилась


    @mock.patch('builtins.input', return_value='exit')
    def test_exit_success(self, mock_input):
        emulator = ShellEmulator(self.config_path)
        emulator.run()
        with open(self.log_path, 'r') as f:
            log_data = json.load(f)
            self.assertEqual(len(log_data), 1)
            self.assertEqual(log_data[0]['command'], 'exit')

    @mock.patch('builtins.input', side_effect=['', 'exit']) #Дополнительный пустой ввод для проверки обработки
    def test_exit_with_empty_input(self, mock_input):
        emulator = ShellEmulator(self.config_path)
        emulator.run()
        with open(self.log_path, 'r') as f:
            log_data = json.load(f)
            self.assertEqual(len(log_data), 2) # Два действия: пустой ввод + exit
            self.assertEqual(log_data[1]['command'], 'exit')


    def test_clear_empty(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        emulator = ShellEmulator(self.config_path)
        emulator._clear()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "")

    def test_clear_with_output(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print("Some text")
        emulator = ShellEmulator(self.config_path)
        emulator._clear()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "")


    def test_mkdir_success(self):
        temp_test_dir = tempfile.mkdtemp()
        emulator = ShellEmulator(self.config_path)
        emulator.current_dir = temp_test_dir
        emulator._mkdir(["newdir"])
        self.assertTrue(os.path.exists(os.path.join(temp_test_dir, "newdir")))
        shutil.rmtree(temp_test_dir)

    def test_mkdir_failure(self):
        temp_test_dir = tempfile.mkdtemp()
        os.makedirs(os.path.join(temp_test_dir, "newdir")) #Создаем существующую директорию
        emulator = ShellEmulator(self.config_path)
        emulator.current_dir = temp_test_dir
        captured_output = io.StringIO()
        sys.stdout = captured_output
        emulator._mkdir(["newdir"]) #Пробуем создать уже существующую
        sys.stdout = sys.__stdout__
        self.assertIn("Директория уже существует.", captured_output.getvalue())
        shutil.rmtree(temp_test_dir)


    def test_rmdir_success(self):
        temp_test_dir = tempfile.mkdtemp()
        os.makedirs(os.path.join(temp_test_dir, "testdir"))
        emulator = ShellEmulator(self.config_path)
        emulator.current_dir = temp_test_dir
        emulator._rmdir(["testdir"])
        self.assertFalse(os.path.exists(os.path.join(temp_test_dir, "testdir")))
        shutil.rmtree(temp_test_dir)


    def test_rmdir_failure(self):
        temp_test_dir = tempfile.mkdtemp()
        os.makedirs(os.path.join(temp_test_dir, "testdir"))
        pathlib.Path(os.path.join(temp_test_dir, "testdir", "file.txt")).touch() #Создаем файл внутри директории
        emulator = ShellEmulator(self.config_path)
        emulator.current_dir = temp_test_dir
        captured_output = io.StringIO()
        sys.stdout = captured_output
        emulator._rmdir(["testdir"]) #Пробуем удалить непустую директорию
        sys.stdout = sys.__stdout__
        self.assertIn("Ошибка удаления директории:", captured_output.getvalue())
        shutil.rmtree(temp_test_dir)

    def test_log_single_command(self):
        emulator = ShellEmulator(self.config_path)
        emulator._ls([])
        emulator._save_log()
        with open(self.log_path, 'r') as f:
            log_data = json.load(f)
            self.assertEqual(len(log_data), 1)
            self.assertEqual(log_data[0]['command'], 'ls')

    def test_log_multiple_commands(self):
        emulator = ShellEmulator(self.config_path)
        emulator._ls([])
        emulator._cd(["subdir"])
        emulator._save_log()
        with open(self.log_path, 'r') as f:
            log_data = json.load(f)
            self.assertEqual(len(log_data), 2)
            self.assertEqual(log_data[0]['command'], 'ls')
            self.assertEqual(log_data[1]['command'], 'cd')


if __name__ == '__main__':
    unittest.main()