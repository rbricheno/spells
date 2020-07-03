#!/bin/bash
# Creates a string which looks like this:
# 20200427-20200727
# representing a date range between the 27th three months ago and
# the 27th of this month

Y=`date +%Y`
M=`date +%m`

# Cast to int
MEXPR=`expr $M`

# Three months ago
MM=`expr $MEXPR - 3`
YY=$Y

# Correct for wrapping to previous year
if [ $MM -le 1 ]
    then
        MM=MM+12
        YY=Y-1
fi

# Add leading zeroes
MMFIX=$(printf "%02d" $MM)

echo ${YY}${MMFIX}27-${Y}${M}27
