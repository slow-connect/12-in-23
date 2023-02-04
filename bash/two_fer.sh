#!/usr/bin/env bash
# https://exercism.org/tracks/bash/exercises/two-fer
if [ $# -eq 0 ]
then
    echo "One for you, one for me."
else
    echo "One for $1, one for me."
fi
