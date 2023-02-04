#!/usr/bin/env bash
# https://exercism.org/tracks/bash/exercises/armstrong-numbers
or=$1
len=${#or}
res=0
armstrong=0
num=$or
while [ $num -ne 0 ]
do
  rem=$(($num % 10))
  armstrong=$(($armstrong + $rem ** $len))
  num=$(($num / 10))
done
if [ $armstrong -eq $or ]
then
  echo "true"
else
  echo "false"
fi
