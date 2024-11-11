import os

CACHE_FILE = "bandit.cache"

class BanditCache:
    def __init__(self, cache_file=CACHE_FILE):
        self.cache_file = cache_file
        self.cache = self.load_cache()

    def load_cache(self):
        cache = {}
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as file:
                for line in file:
                    if line.strip():
                        level, result = line.split(":", 1)
                        cache[level] = result.strip()
        return cache

    def save_cache(self):
        with open(self.cache_file, 'w') as file:
            for level, result in self.cache.items():
                file.write(f"{level}:{result}\n")
    
    def get_level_password(self, level):
        return self.cache.get(str(level))

    def set_level_password(self, level, result):
        self.cache[str(level)] = result
        self.save_cache()