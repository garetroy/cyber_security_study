import json
import os
import importlib.util

from BanditCache import BanditCache

CACHE_FILE = "bandit.cache"

class BanditLevelGenerator:
    def __init__(self, requested_level: str):
        self.requested_level = int(requested_level)
        self.cache = BanditCache()
    
    def create_script(self, level, command, password=None):
        filename = f"BanditLevel{level}.py"
        with open(filename, 'w') as file:
            file.write(f"""
from BanditLevel import BanditLevel

class BanditLevel{level}(BanditLevel):
    def __init__(self):
        super().__init__("{command}", __file__, password="{password}")

    def get_next_password(self):
        return super().get_next_password()
""")

    def import_and_run_class(self, level):
        module_name = f"BanditLevel{level}"
        file_path = f"{module_name}.py"

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        bandit_class = getattr(module, f"BanditLevel{level}")
        instance = bandit_class()
        
        result = instance.get_next_password()
        
        os.remove(file_path)
        
        return result

    def generate_and_run(self, cmd, password):
        cache_result = self.cache.get_level_password(self.requested_level)
        if cache_result is None:
            self.create_script(self.requested_level, cmd, password)
            cache_result = self.import_and_run_class(self.requested_level)

            if cache_result is None or len(cache_result) == 0:
                raise ValueError(f'No value returned from bandit session - {self.requested_level}')

            self.cache.set_level_password(self.requested_level, cache_result)

        return cache_result
