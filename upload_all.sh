#!/bin/bash

# Directory containing Python files to upload
directory="$1"

# Device to upload files to
device="$2"

# Path to the pyboard.py tool
# pyboard_tool="micropython/tools/pyboard.py"
pyboard_tool="${PYBOARD_TOOL_PATH}"

# Check if the PYBOARD_TOOL environment variable is set
if [ -z "$pyboard_tool" ]; then
    echo "Error: PYBOARD_TOOL_PATH environment variable is not set."
    exit 1
fi

# Check if the directory is provided
if [ -z "$directory" ]; then
    echo "Usage: $0 <directory> <device>"
    exit 1
fi

# Check if the device is provided
if [ -z "$device" ]; then
    echo "Usage: $0 <directory> <device>"
    exit 1
fi

# Verify if the directory exists
if [ ! -d "$directory" ]; then
    echo "Error: Directory '$directory' does not exist."
    exit 1
fi

# Loop through all Python files in the directory
for file in "$directory"/*.py; do
    # Check if there are Python files in the directory
    if [ ! -e "$file" ]; then
        echo "No Python files found in the directory '$directory'."
        exit 1
    fi

    # Upload the file to the MicroPython board
    echo "Uploading $file to device $device..."
    python3 "$pyboard_tool" --device "$device" -f cp "$file" :$(basename "$file")

    # Check if the upload was successful
    if [ $? -ne 0 ]; then
        echo "Failed to upload $file."
        exit 1
    fi

done

echo "All files uploaded successfully."