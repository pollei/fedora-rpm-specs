   
Name: pki-usgov-dod-cacerts
Version: 0.0.4
Release: 2%{?dist}
Summary: A collection of U.S. Government CA Certs that DOD uses
BuildArch: noarch

# This package is security sensitive,
#   certs are used to authenticate military websites
# security@lists.fedoraproject.org

   
License: Public Domain
# these certs are public domain for two reasons
#  1) 17 USC 105 -- Government can't have copyright
#  2) they are highly constrained "facts"

%global commit0 a6b97e18190871d99609d39eb473bf23cadcd656
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
URL: https://github.com/pollei/pki-usgov-dod-cacerts
   
   
   
Source0:  https://github.com/pollei/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

   

BuildRequires: perl(Digest::CRC) openssl
   

%description
A collection of U.S. Government CA Certs that DOD uses
 Department of Defense, Federal Common Policy
 Useful for Army, Navy, Air Force, and Marines
%prep
   
%setup -qn %{name}-%{commit0}


%build
./extract_x509.sh

%install
   
mkdir -p ${RPM_BUILD_ROOT}/etc/pki/usgov_dod/cacerts/
mkdir -p ${RPM_BUILD_ROOT}/%{_datadir}/pki-usgov-dod/
   
cp pki-usgov-dod/cacerts/*.{pem,crt} ${RPM_BUILD_ROOT}/etc/pki/usgov_dod/cacerts/
cat pki-usgov-dod/cacerts/*.txt > ${RPM_BUILD_ROOT}/%{_datadir}/pki-usgov-dod/cacert-list.txt


   
   


%files
   
%config(noreplace) /etc/pki/usgov_dod/cacerts/
%{_datadir}/pki-usgov-dod/
%doc README
   

# https://fedoraproject.org/wiki/PackagingDrafts/Certificates

%changelog
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

