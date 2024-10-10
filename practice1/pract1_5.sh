#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <command>"
    exit 1
fi

command=$1

if [ ! -f "$command" ]; then
    echo "File '$command' not found!"
    exit 1
fi

if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root!"
    exit 1
fi

cp "$command" /usr/local/bin/

chmod +x /usr/local/bin/"$command"

echo "'$command' has been registered successfully."
