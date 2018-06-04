#!/bin/bash

# current Git branch
branch=$(git symbolic-ref HEAD | sed -e 's,.*/\(.*\),\1,')

# v1.0.0, v1.5.2, etc.

echo $1
echo $2
echo $3
echo "---------------------"

versionFrom=$1
versionTo=$2
versionLabel=v$versionTo
repo=$3

# establish branch and tag name variables
masterBranch=master
releaseBranch=$versionTo

echo "---------" $repo "-------------"
cd $repo
git checkout $masterBranch
git pull

# create the release branch from the -develop branch
# git checkout -b $releaseBranch 
 
# file in which to update version number
setupFile="setup.py"
 
# find version number assignment ("= v1.5.5" for example)
# and replace it with newly specified version number
sed -i.backup -E "s/(JumpScale9[A-Za-z]*)>=$versionFrom/\1>\=$versionTo/" $setupFile $setupFile
sed -i.backup -E "s/version='[0-9.]+'/version\='$versionTo'/" $setupFile $setupFile
 
# remove backup file created by sed command
rm $setupFile.backup
 
# commit version number increment
git commit -am "Bump version number to $versionLabel"

# git push -u origin $releaseBranch
 
# merge release branch with the new version number into master
git checkout $masterBranch
git merge --no-ff $releaseBranch

git push -u origin $masterBranch
 
 
