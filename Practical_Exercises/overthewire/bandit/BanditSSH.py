import subprocess
import os
import tempfile
import argparse

class BanditSSH:
    def __init__(self, level, credential, command=None):
        self.level = level
        self.credential = credential
        self.command = command
        self.host = "bandit.labs.overthewire.org"
        self.port = 2220
        self.username = f"bandit{level}"
        self.key_file = None

    def is_private_key(self):
        return "PRIVATE KEY" in self.credential

    def prepare_key_file(self):
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

    def execute(self):
        try:
            if self.is_private_key():
                self.prepare_key_file()
                ssh_command = [
                    "ssh", "-i", self.key_file.name, "-p", str(self.port),
                    f"{self.username}@{self.host}"
                ]
            else:
                ssh_command = [
                    "sshpass", "-p", self.credential,
                    "ssh", "-p", str(self.port), f"{self.username}@{self.host}"
                ]

            if self.command:
                _ = subprocess.run(
                    ssh_command + ["echo ''"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                result = subprocess.run(
                    ssh_command + [self.command],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                command_output = result.stdout.strip()
                return command_output

            else:
                subprocess.call(ssh_command)

        finally:
            self.cleanup()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Connect to the Bandit server")
    parser.add_argument("level", help="The Bandit level (e.g., 17)")
    parser.add_argument("credential", help="Password or private key content for the Bandit level")
    parser.add_argument("command", nargs="?", default=None, help="Optional command to execute on the server")

    args = parser.parse_args()

    bandit_ssh = BanditSSH(level=args.level, credential=args.credential, command=args.command)
    bandit_ssh.execute()
