#!/usr/bin/env bash
# Task: https://exercism.org/tracks/bash/exercises/hamming
if [[ $# -eq 0 || $# -eq 1 ]]
then
  echo "Usage: hamming.sh <string1> <string2>"
  exit 1
fi
dna1=$1
dna2=$2
if [ ${#dna1} == ${#dna2} ]
then
  numMismatches=0
for (( i=0; i<${#dna1}; i++ )); do
  if [ "${dna1:$i:1}" != "${dna2:$i:1}" ]; then
    numMismatches=$(($numMismatches + 1))
  fi
done
  echo $numMismatches
else
  echo "strands must be of equal length"
  exit 1
fi
