#!/bin/bash
set -e
day=$1
if test -e "day$day"; then
    echo "The day exists"
    exit 1
fi
cp -r template "day$day"
echo "Directory day$day created"
echo "See the problem: https://adventofcode.com/2022/day/$day"
echo "Copy the example in example.txt"
echo "Download the input: https://adventofcode.com/2022/day/$day/input"
