# !/bin/sh
# License: GPLv3+

pkg=$1

mkdir -p ~/rpmbuild/SOURCES/ ~/rpmbuild/SPECS/

if test -z "${pkg}" ; then
  echo 'needs package name'
  exit
fi

if test -f ${pkg}.spec -a -f ${pkg}-commit.sh ; then 
  echo 'have spec for ' ${pkg}
else
  echo 'missing spec or commit for' ${pkg}
  exit
fi

cp ${pkg}.spec ~/rpmbuild/SPECS/

. ./${pkg}-commit.sh
# Source0:  https://github.com/pollei/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
wget https://github.com/pollei/${pkg}/archive/${commit}.tar.gz -nc -O ~/rpmbuild/SOURCES/${pkg}-${commit:0:7}.tar.gz 

