#!/bin/bash

# input 1: username
# input 2: accesstoken
# input 3: old version
# input 4: new version
# input 5: prerelease

echo $1

for repo in core9 bash lib9 prefab9
do
    bash jumpscale_prepare_release.sh $3 $4 "/root/gig/code/github/jumpscale/$repo"
done
python3 createrelease.py - u $1 - t $2 - o jumpscale - r bash core9 lib9 prefab9 - v v$4 - b $4 - p $5 - f releasenotes.md
