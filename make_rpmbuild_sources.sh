# !/bin/sh
# License: GPLv3+

# create the tar ball
tar czf pki-usgov-dod-0.0.3.tar.gz pki-usgov-dod/ --transform=s/pki-usgov-dod/pki-usgov-dod-cacerts-0.0.3/ 

mkdir -p ~/rpmbuild/SOURCES/ ~/rpmbuild/SPECS/
git ls-remote https://github.com/pollei/lojban_utils
git ls-remote https://github.com/pollei/pki-usgov-dod-cacerts
git ls-remote https://github.com/pollei/firefox-usgov-dod-cfg


cp pki-usgov-dod-0.0.3.tar.gz ~/rpmbuild/SOURCES/
cp firefox-usgov-dod-cfg-cli.pl ~/rpmbuild/SOURCES/

cp fedora-pki-usgov-dod-cacerts.spec ~/rpmbuild/SPECS/pki-usgov-dod-cacerts-0.0.3.spec
cp fedora-pki-usgov-dod-cacerts.spec ~/rpmbuild/SPECS/pki-usgov-dod-cacerts.spec

cp fedora-firefox-usgov-dod-cfg.spec ~/rpmbuild/SPECS/firefox-usgov-dod-cfg-0.0.1.spec
cp fedora-firefox-usgov-dod-cfg.spec ~/rpmbuild/SPECS/firefox-usgov-dod-cfg.spec



