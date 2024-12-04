import subprocess
import os
import tempfile
import argparse
import json

COMMAND_FILE = 'levels.json'

class LeviathanSSH:
    def __init__(self, level, credential=None, command=None, script_path=None, remote_path="/tmp/wow"):
        self.level = int(level)
        self.command = command
        self.script_path = script_path
        self.remote_path = remote_path
        self.host = "leviathan.labs.overthewire.org"
        self.port = 2223
        self.username = f"leviathan{level}"
        self.key_file = None

        if credential is not None:
            self.credential = credential
        else:
            self.credential = self.get_last_password()

    def get_last_password(self):
        with open(COMMAND_FILE, 'r') as file:
            json_data = json.load(file)
            return json_data.get(str(self.level-1), {}).get("password", None)

    def is_private_key(self):
        return "PRIVATE KEY" in self.credential

    def prepare_key_file(self):
        if self.key_file is not None:
            return 

        self.key_file = tempfile.NamedTemporaryFile(delete=False)

        begin = "-----BEGIN RSA PRIVATE KEY-----"
        end = "-----END RSA PRIVATE KEY-----"
        self.credential = self.credential.replace(begin, f"{begin}\n")
        self.credential = self.credential.replace(end, f"\n{end}")

        self.key_file.write(self.credential.encode())
        self.key_file.close()
        os.chmod(self.key_file.name, 0o400)

    def cleanup(self):
        if self.key_file:
            os.remove(self.key_file.name)

    def get_login_command(self, is_scp=False):
        ssh_operator = "scp" if is_scp else "ssh"
        if self.is_private_key():
            self.prepare_key_file()
            result = [
                ssh_operator, "-i", self.key_file.name, "-p", str(self.port),
                self.script_path if is_scp  else None,
                f"{self.username}@{self.host}"
            ]
        else:
            result = [
                "sshpass", "-p", self.credential,
                ssh_operator, "-p", str(self.port), 
                self.script_path if is_scp  else None,
                f"{self.username}@{self.host}"
            ]
        
        return [item for item in result if item != None]

    def execute(self):
        login_command = self.get_login_command()

        try:
            if self.script_path is not None:
                subprocess.run(
                    login_command + ["mkdir -p /tmp/wow"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                subprocess.run(
                    self.get_login_command(True), 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE, 
                    text=True
                )

                command_to_run = f"chmod +x {self.remote_path} && {self.remote_path}"
                result = subprocess.run(
                    login_command + [command_to_run],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                return result.stdout.strip()

            elif self.command:
                result = subprocess.run(
                    login_command + [self.command],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                return result.stdout.strip()

            else:
                subprocess.call(login_command)

        finally:
            self.cleanup()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Connect to the Leviathan server")
    parser.add_argument("level", help="The Leviathan level (e.g., 3)")
    parser.add_argument("credential", nargs="?", help="Password or private key content for the Leviathan level", default=None)
    parser.add_argument("command", nargs="?", help="Optional command to execute on the server", default=None)
    parser.add_argument("--script_path", help="Local path of the script to inject", default=None)
    parser.add_argument("--remote_path", help="Remote path to inject the script (default: /tmp/wow)", default="/tmp/wow")

    args = parser.parse_args()

    leviathan_ssh = LeviathanSSH(
        level=args.level,
        credential=args.credential,
        command=args.command,
        script_path=args.script_path,
        remote_path=args.remote_path
    )

    output = leviathan_ssh.execute()
    if output:
        print(output)
