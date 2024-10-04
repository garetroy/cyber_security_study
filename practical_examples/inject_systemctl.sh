#/bin/sh

if [ "$#" -ne 2 ]; then
    echo "Enables a service to call <command> on <service-name>"
    echo "(i.e. systemctl <command> <service-name>)"
    echo "Usage: $0 <command> <service-name>"
    exit 1
fi

command="$1"
service_name="$2"

# Line to be injected into the sudoers file
sudoers_line="$(whoami) ALL=(ALL) NOPASSWD: /bin/systemctl $command $service_name"

# Check if the line already exists in the sudoers file to avoid duplicates
if sudo grep -qF "$sudoers_line" /etc/sudoers; then
    echo "Entry $sudoers_line already exists in sudoers file."
else
    # Add the line to the sudoers file
    echo "$sudoers_line" | sudo EDITOR='tee -a' visudo
fi
