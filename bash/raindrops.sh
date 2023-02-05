#!/usr/bin/env bash
# Task: https://exercism.org/tracks/bash/exercises/raindrops
a=$1
str=''
if (($a % 3 == 0))
then
  str="${str}Pling"
fi
if (($a % 5 == 0))
then
  str="${str}Plang"
fi
if (($a % 7 == 0))
then
  str="${str}Plong"
fi
if [ "$str" == "" ]
then
  echo $a
else
  echo $str
fi
