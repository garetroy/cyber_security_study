#!/run/current-system/sw/bin/expect

set timeout -1

set lvl [lindex $argv 0]
set lvlpsswd [lindex $argv 1]

# Check if a third argument (command) is provided
if { [llength $argv] > 2 } {
    set cmd [lindex $argv 2]
} else {
    set cmd ""
}

log_user 0

# Construct the ssh command dynamically based on whether $cmd is populated
if { $cmd != "" } {
    spawn ssh bandit$lvl@bandit.labs.overthewire.org -p 2220 $cmd
} else {
    spawn ssh bandit$lvl@bandit.labs.overthewire.org -p 2220
}

expect "password:"
send "$lvlpsswd\r"

log_user 1

interact

