#! /bin/sh
# License: GPLv3+
git_base=https://github.com/pollei
pkg=$1
head=$2
head=${head+HEAD}
tag=$3
commit=' xx '

export GIT_ASKPASS='/bin/false'
# if given bogus pkg can hang and ask password, just fail instead
# still asks for username, wish I knew how to make it fail faster

# echo $git_base $pkg $head $commit
# commits=`git ls-remote ${git_base}/${pkg} -h ${head} | cut -c-40`
commits=`git ls-remote ${git_base}/${pkg} -h ${head} `
commit=${commits:0:40}
#echo $commits
echo $git_base $pkg $commit

echo  "commit=${commit}" > ${pkg}-commit.sh


# http://www.grymoire.com/Unix/Sed.html
# I don't write very much sed better keep a reference handy
## sed "s/^%global commit0 [0-9a-fA-F]*/%global commit0 ${commit}/" < ${pkg}.tspec > $pkg.spec
