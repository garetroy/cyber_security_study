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

# Determine if lvlpsswd is a private key or password
if { [string first "PRIVATE KEY" $lvlpsswd] >= 0 } {
    # Create a temporary file to store the private key
    set key_file "/tmp/temp_private_key"
    set f [open $key_file w]
    puts -nonewline $f $lvlpsswd
    close $f
    exec chmod 600 $key_file

    # Use the private key for SSH
    if { $cmd != "" } {
        spawn ssh -i $key_file bandit$lvl@bandit.labs.overthewire.org -p 2220 $cmd
    } else {
        spawn ssh -i $key_file bandit$lvl@bandit.labs.overthewire.org -p 2220
    }
} else {
    # Use password for SSH
    if { $cmd != "" } {
        spawn ssh bandit$lvl@bandit.labs.overthewire.org -p 2220 $cmd
    } else {
        spawn ssh bandit$lvl@bandit.labs.overthewire.org -p 2220
    }
    expect "password:"
    send "$lvlpsswd\r"
}

log_user 1

interact

# Clean up the private key file if created
if { [info exists key_file] } {
    exec rm $key_file
}

