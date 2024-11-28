import zipfile
import os
import json
import toml
import shutil
from pathlib import Path
import datetime

class ShellEmulator:
    def __init__(self, config_path):
        self.config = toml.load(config_path)
        self.user = self.config['user']
        self.vfs_path = self.config['vfs_path']
        self.log_path = self.config['log_path']
        self.current_dir = "/"  # Начальная директория
        self.vfs = self._load_vfs()
        self.log = []


    def _load_vfs(self):
        """Загружает виртуальную файловую систему из zip-архива."""
        # Временная директория для распаковки
        temp_dir = "temp_vfs"
        Path(temp_dir).mkdir(exist_ok=True)
        with zipfile.ZipFile(self.vfs_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        return temp_dir


    def _log_action(self, command, args):
        """Логирует действие."""
        timestamp = datetime.datetime.now().isoformat() # Добавлено для отметки времени
        action = {"user": self.user, "command": command, "args": args}
        self.log.append(action)


    def run(self):
        """Запускает эмулятор."""
        while True:
            print(f"{self.user}@{self.current_dir}$ ", end="")
            command = input().strip().split()
            if not command:
                continue

            cmd = command[0]
            args = command[1:]

            self._log_action(cmd, args)

            if cmd == "ls":
                self._ls(args)
            elif cmd == "cd":
                self._cd(args)
            elif cmd == "mkdir":
                self._mkdir(args)
            elif cmd == "rmdir":
                self._rmdir(args)
            elif cmd == "clear":
                self._clear()
            elif cmd == "exit":
                break
            else:
                print("Неизвестная команда.")

        self._save_log()
        shutil.rmtree("temp_vfs")


    def _ls(self, args):
        path = self._get_absolute_path(args[0] if args else "")
        try:
            entries = os.listdir(path)
            print('\n'.join(entries))
        except FileNotFoundError:
            print("Директория не найдена.")


    def _cd(self, args):
        if not args:
            self.current_dir = "/"
            return

        new_dir = args[0]
        path = self._get_absolute_path(new_dir)
        try:
            if os.path.isdir(path):
                self.current_dir = path
            else:
                print("Директория не найдена.")
        except FileNotFoundError:
            print("Директория не найдена.")


    def _mkdir(self, args):
        if not args:
          print("Укажите имя директории")
          return

        path = os.path.join(self.current_dir, args[0])
        try:
            os.makedirs(path, exist_ok=False)
        except FileExistsError:
            print("Директория уже существует.")
        except OSError as e:
            print(f"Ошибка создания директории: {e}")


    def _rmdir(self, args):
        if not args:
          print("Укажите имя директории")
          return

        path = os.path.join(self.current_dir, args[0])
        try:
            os.rmdir(path)
        except FileNotFoundError:
            print("Директория не найдена.")
        except OSError as e:
            print(f"Ошибка удаления директории: {e}")


    def _clear(self, args=None):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _get_absolute_path(self, relative_path):
        return os.path.normpath(os.path.join(self._load_vfs(), relative_path))

    def _save_log(self):
        with open(self.log_path, 'w') as f:
            json.dump(self.log, f, indent=4)


if __name__ == "__main__":
    emulator = ShellEmulator("config.toml")
    emulator.run()