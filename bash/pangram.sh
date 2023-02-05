#!/usr/bin/env bash
# Task: https://exercism.org/tracks/bash/exercises/pangram/
ALPHABET=(a b c d e f g h i j k l m n o p q r s t u v w x y z)

phrase=$@
for letter in "${ALPHABET[@]}"
do
  if [[ "$phrase" != *"$letter"* && "$phrase" != *"${letter^^}"* ]]
  then
    echo "false"
    exit 0
  fi
done
echo "true"
exit 0
