import os
import json
import toml
import zipfile
from datetime import datetime
from pathlib import Path


class ShellEmulator:
    def __init__(self, config_path):
        self.load_config(config_path)
        self.current_dir = Path(".")  # Начальная директория
        self.previous_dir = None
        self.file_system = {}
        self.log = []

        self.load_virtual_fs()
        self.commands = {
            "ls": self.ls,
            "cd": self.cd,
            "mkdir": self.mkdir,
            "clear": self.clear,
            "rmdir": self.rmdir,
            "pwd": self.pwd,
            "exit": self.exit_shell
        }

    def load_config(self, config_path):
        config = toml.load(config_path)
        self.username = config.get("username", "user")
        self.fs_path = config["fs_path"]
        self.log_path = config["log_path"]

    def load_virtual_fs(self):
        with zipfile.ZipFile(self.fs_path, 'r') as zip_ref:
            for file in zip_ref.namelist():
                self.file_system[Path(file)] = None

    def log_action(self, action):
        self.log.append({"user": self.username, "action": action, "time": str(datetime.now())})

    def save_log(self):
        with open(self.log_path, "w") as log_file:
            json.dump(self.log, log_file, indent=4)

    def ls(self, *args):
        items_in_current_dir = [str(p) for p in self.file_system.keys() if p.parent == self.current_dir]

        if items_in_current_dir:
            print("\n".join(items_in_current_dir))
        else:
            print("No items in current directory.")

        self.log_action("ls")

    def pwd(self, *args):
        print(self.current_dir)
        self.log_action("pwd")

    def cd(self, path):
        if path == "..":
            if self.current_dir != Path("."):
                self.previous_dir = self.current_dir
                self.current_dir = self.current_dir.parent
                print(f"Changed directory to {self.current_dir}")
            else:
                print("Cannot move up from root directory.")
        else:
            new_dir = Path(path)
            if new_dir in self.file_system:
                self.previous_dir = self.current_dir
                self.current_dir = new_dir
                print(f"Changed directory to {self.current_dir}")
            else:
                print(f"No such directory: {path}")
        self.log_action(f"cd {path}")

    def mkdir(self, dirname):
        new_dir = self.current_dir / dirname
        if new_dir not in self.file_system:
            self.file_system[new_dir] = None
            print(f"Directory {dirname} created.")
        else:
            print(f"Directory {dirname} already exists.")
        self.log_action(f"mkdir {dirname}")

    def clear(self, *args):
        os.system("cls" if os.name == "nt" else "clear")
        self.log_action("clear")

    def rmdir(self, dirname):
        target_dir = self.current_dir / dirname
        if target_dir in self.file_system:
            del self.file_system[target_dir]
            print(f"Directory {dirname} removed.")
        else:
            print(f"No such directory: {dirname}")
        self.log_action(f"rmdir {dirname}")

    def exit_shell(self, *args):
        self.log_action("exit")
        self.save_log()
        print("Exiting shell...")
        exit()

    def run(self):
        while True:
            command = input(f"{self.username}@emulator:{self.current_dir}$ ").strip().split()
            if command:
                cmd, *args = command
                if cmd in self.commands:
                    self.commands[cmd](*args)
                else:
                    print(f"Command not found: {cmd}")


if __name__ == "__main__":
    emulator = ShellEmulator("config.toml")
    emulator.run()