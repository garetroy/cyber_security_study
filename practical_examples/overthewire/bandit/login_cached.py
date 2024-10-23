import os
import subprocess
import hashlib
import base64

CACHE_FILE = "bandit.cache"

def generate_cache_key(level, cmd):
    key_string = f"lvl{level}-{cmd}"
    return hashlib.md5(key_string.encode()).hexdigest()

def obfuscate_value(value):
    return base64.b64encode(value.encode()).decode()

def deobfuscate_value(value):
    return base64.b64decode(value.encode()).decode()

def load_cache():
    cache = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            for line in f:
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    cache[key] = deobfuscate_value(value)
    return cache

def save_to_cache(key, value):
    obfuscated_value = obfuscate_value(value)
    with open(CACHE_FILE, 'a') as f:
        f.write(f"{key}:{obfuscated_value}\n")

def run_login_script(level, password, cmd):
    if cmd:
        command = ['./login.sh', level, password, cmd]
    else:
        command = ['./login.sh', level, password]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

def main(level, password, cmd=""):
    cache = load_cache()
    cache_key = generate_cache_key(level, cmd)
    if cache_key in cache:
        print(cache[cache_key])
    else:
        output = run_login_script(level, password, cmd)
        save_to_cache(cache_key, output)
        print(output)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python login_wrapper.py <level> <password> [command]")
        sys.exit(1)
    
    level = sys.argv[1]
    password = sys.argv[2]
    cmd = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else ""
    main(level, password, cmd)

