#!/bin/bash
grep -i "python" data/*.csv | wc -l > _output/python_count.txt
echo "Python keyword count saved to _output/python_count.txt"

