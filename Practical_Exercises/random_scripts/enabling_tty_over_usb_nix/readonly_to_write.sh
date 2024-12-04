#/bin/sh
if [ "$#" -ne 1 ]; then
    echo "Remounts the directory from ro to rw"
    echo "Usage: $0 <directory>"
    exit 1
fi

directory="$1"

# Check if the root filesystem is mounted as read-only
echo "Checking if \"$directory\" mounted as read-only..."

mount_status=$(mount | grep " on $directory " | grep "(ro,")
if [ -n "$mount_status" ]; then
    echo "\"$directory\" is currently mounted as read-only."
    
    # Attempt to remount the filesystem as read-write
    echo "Attempting to remount \"$directory\" as read-write..."
    if sudo mount -o remount,rw $directory; then
        echo "Successfully remounted \"$directory\" as read-write."
    fi
else
    echo "\"$directory\" is already mounted as read-write."
fi
