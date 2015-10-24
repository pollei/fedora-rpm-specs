#! /bin/sh

for pkg in firefox-usgov-dod-cfg pki-usgov-dod-cacerts ; do
  ./make_git_spec.sh ${pkg}
  ./fetch-git-tar.sh ${pkg}
  rpmbuild -ba ~/rpmbuild/SPECS/${pkg}.spec
done
