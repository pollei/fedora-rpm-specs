Name: pki-usgov-dod-cacerts
Version: 0.0.6
Release: 2%{?dist}
Summary: A collection of U.S. Government CA Certs that DOD uses
BuildArch: noarch
# This package is security sensitive,
#   certs are used to authenticate military websites
# security@lists.fedoraproject.org
License: Public Domain

%global commit0 8dc419c5644fc7305f757ec571406f5b2e0a96af
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
URL: https://github.com/pollei/pki-usgov-dod-cacerts
Source0:  https://github.com/pollei/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildRequires: perl(MIME::Base64) perl(Digest::CRC) openssl
%description
A collection of U.S. Government CA Certs that the DOD uses.
Has Department of Defense, and Federal Common Policy certs.
Useful for Army, Navy, Air Force, and Marines.
%prep
%setup -qn %{name}-%{commit0}

%build
./extract_x509.sh

%install
mkdir -p ${RPM_BUILD_ROOT}/etc/pki/usgov-dod/cacerts/
mkdir -p ${RPM_BUILD_ROOT}/%{_datadir}/pki-usgov-dod/
cp pki-usgov-dod/cacerts/*.{pem,crt} ${RPM_BUILD_ROOT}/etc/pki/usgov-dod/cacerts/
cat pki-usgov-dod/cacerts/*.txt > ${RPM_BUILD_ROOT}/%{_datadir}/pki-usgov-dod/cacert-list.txt

%files
%config /etc/pki/usgov-dod/cacerts/
%{_datadir}/pki-usgov-dod/
%doc README

%changelog
* Mon Jan 11 2016 Steve Pollei <stephen.pollei@gmail.com> 0.0.6-2
- updated description with periods and a little better grammar
* Mon Jan 11 2016 Steve Pollei <stephen.pollei@gmail.com> 0.0.6-1
- lowered perl version to 5.10 to hopefully work in epel6
- added perl(MIME::Base64) to buildrequires to work in rawhide
* Mon Jan 11 2016 Steve Pollei <stephen.pollei@gmail.com> 0.0.5-1
- spec file white space removal
- changed /etc/pki/usgov_dod to /etc/pki/usgov-dod
- got rid of noreplace
- installs crt files in der format as well as pem
* Fri Oct 23 2015 Steve Pollei <stephen.pollei@gmail.com> 0.0.4-2
- added openssl to Buildrequires
* Fri Oct 23 2015 Steve Pollei <stephen.pollei@gmail.com> 0.0.4-1
- transitioned over to using github
* Thu Oct 22 2015 Steve Pollei <stephen.pollei@gmail.com> 0.0.3-1
- Changed name from usgov_pki_ca_certs to pki-usgov-dod-cacerts IAW Packaging:NamingGuidelines 
- moved human readable cert info into one big text file in /usr/share/pki-usgov-dod
* Wed Oct 21 2015 Steve Pollei <stephen.pollei@gmail.com> 0.0.2-1
- Noarch
- following https://fedoraproject.org/wiki/PackagingDrafts/Certificates
-   moved certs from /usr/share/foo to /etc/pki/usgov_dod/cacerts
