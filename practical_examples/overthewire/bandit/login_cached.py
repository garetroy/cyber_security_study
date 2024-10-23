import os
import subprocess
import hashlib

CACHE_FILE = "bandit.cache"

# Function to generate a cache key from the level and command
def generate_cache_key(level, cmd):
    key_string = f"lvl{level}-{cmd}"
    return hashlib.md5(key_string.encode()).hexdigest()

# Function to load the cache into a dictionary
def load_cache():
    cache = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    cache[key] = value
    return cache

# Function to save output to cache
def save_to_cache(key, value):
    with open(CACHE_FILE, 'a') as f:
        f.write(f"{key}={value}\n")

# Function to run login.sh using subprocess
def run_login_script(level, password, cmd):
    # Prepare the command for subprocess
    if cmd:
        command = ['./login.sh', level, password, cmd]
    else:
        command = ['./login.sh', level, password]

    # Run the Expect script and capture output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Return the captured output as a string
    return result.stdout.decode('utf-8').strip()

# Main function to wrap login.sh and cache the output
def main(level, password, cmd=""):
    # Load the cache
    cache = load_cache()

    # Generate a cache key for the current command
    cache_key = generate_cache_key(level, cmd)

    # Check if the result is already in cache
    if cache_key in cache:
        print(cache[cache_key])
    else:
        # Run the login.sh script and get the result
        output = run_login_script(level, password, cmd)

        # Save the output to the cache
        save_to_cache(cache_key, output)

        # Output the result
        print(output)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python login_wrapper.py <level> <password> [command]")
        sys.exit(1)
    
    # Parse arguments from the command line
    level = sys.argv[1]
    password = sys.argv[2]
    cmd = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else ""

    # Run the main function
    main(level, password, cmd)

