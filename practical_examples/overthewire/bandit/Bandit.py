import argparse
import json

from BanditCache import BanditCache
from BanditLevelGenerator import BanditLevelGenerator

COMMAND_FILE = 'levels.json'

class Bandit:
    def __init__(self, requested_level):
        self.cache = BanditCache()
        json_data = None
        with open(COMMAND_FILE, 'r') as file:
            json_data = json.load(file)
        
        self.json_data = json_data
        self.requested_level = requested_level

    def print_pasword(self, level: str, should_print: bool = True) -> None:

        # We have to go through all the bandit levels previous and get their passwords
        if int(level) > 0 and self.cache.get_level_password(int(level) -1) is None:
            self.print_pasword(str(int(level) - 1), False)

        cmd = self.json_data.get(level, {}).get("cmd")
        password = self.json_data.get(level, {}).get("password", None)
        result = BanditLevelGenerator(level).generate_and_run(cmd, password)
        
        if should_print:
            print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the requested bandit level password")
    parser.add_argument("level", help="The Bandit level (e.g., 17)")

    args = parser.parse_args()

    bandit_ssh = Bandit(args.level).print_pasword(args.level)

