import os
import importlib
import re

from BanditCache import BanditCache
from BanditSSH import BanditSSH

class BanditLevel:
    def __init__(self, command: str, file_path: str, password: str = None) -> None:
        self.command = command
        self.file_path = file_path

        self.level = self.get_current_level()

        if password is None or password == "None":
            self.password = self.get_previous_password()
        else:
            self.password = password

    
    def get_current_level(self) -> int:
        current_script = os.path.basename(self.file_path)

        match = re.search(r'\d+', current_script)
        return int(match.group()) 

    def get_previous_password(self) -> None:
        return BanditCache().get_level_password(self.level-1)

    def get_next_password(self) -> None:
        bandit = BanditSSH(self.level, self.password, self.command)
        return bandit.execute().replace('\r', '').replace('\n', '')