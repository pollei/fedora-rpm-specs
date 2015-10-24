#! /bin/sh
# License: GPLv3+
## git_base=https://github.com/pollei
pkg=$1
## head=$2
## head=${head+HEAD}
## tag=$3
commit=' xx '

##  export GIT_ASKPASS='/bin/false'
# if given bogus pkg can hang and ask password, just fail instead
# still asks for username, wish I knew how to make it fail faster

## echo $git_base $pkg $head $commit
# commits=`git ls-remote ${git_base}/${pkg} -h ${head} | cut -c-40`
## commits=`git ls-remote ${git_base}/${pkg} -h ${head} `
## commit=${commits:0:40}
## echo $commits
## echo $git_base $pkg $commit

if test -z "${pkg}" ; then
  echo 'needs package name'
  exit
fi

## echo beforeif $pkg $commit
if test -f ./${pkg}-commit.sh ; then
   echo 'using cache for ' ${pkg}
   . ./${pkg}-commit.sh
else 
   echo 'fetching for ' ${pkg}
   . ./fetch-git-commit.sh
fi
## echo afterif $pkg $commit
  

# http://www.grymoire.com/Unix/Sed.html
# I don't write very much sed better keep a reference handy
sed -e "s/^%global commit0 [0-9a-fA-F]*/%global commit0 ${commit}/" \
    -e "s/^## .*$/   /"  < ${pkg}.tspec > $pkg.spec
