#!/usr/bin/env bash
# Task: https://exercism.org/tracks/bash/exercises/error-handling
if [[ $# -eq 0 ||  $# -gt 1 ]]
then
    echo "Usage: error_handling.sh <person>"
    exit 1
else
    echo "Hello, $@"
fi