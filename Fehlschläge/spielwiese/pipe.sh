#!/bin/bash

pipe=/tmp/hugepackage_pipe

if [[ ! -p $pipe ]]; then
    mkfifo $pipe
fi

echo "Test" >$pipe
echo "Next" >$pipe


