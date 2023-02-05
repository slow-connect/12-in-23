#!/usr/bin/env bash
# Task: https://exercism.org/tracks/bash/exercises/acronym
phrase=$@
phrase_no_punc=${phrase//[^A-Za-z -]/}
phrase_no_punc=${phrase_no_punc//-/ }
accronym=${phrase_no_punc:0:1}
for (( i=0; i<${#phrase_no_punc}; i++ )); do
  if [ "${phrase_no_punc:$i:1}" = " " ]; then
    accronym="${accronym}${phrase_no_punc:$i:2}"
accronym=${accronym// /}
  fi
done
echo $accronym | tr a-z A-Z
