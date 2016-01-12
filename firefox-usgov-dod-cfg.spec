Name: firefox-usgov-dod-cfg
Version: 0.0.3
Release: 1%{?dist}
Summary: Help install certs and cac-card in a firefox profile
BuildArch: noarch
# This package is security sensitive
# it activates the use of CA in firefox that are used to access foo.mil sites via tls
License: GPLv3+
%global commit0 4616f609909ed974128c45490e21bb9044521e69
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
URL: https://github.com/pollei/firefox-usgov-dod-cfg
Source0:  https://github.com/pollei/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

Requires: pki-usgov-dod-cacerts perl firefox nss-util perl(Convert::ASN1) perl(Convert::PEM) perl(Crypt::X509) coolkey perl(Gtk3)
%description
Help install certs and cac-card in a firefox profile

firefox-usgov-dod-cfg-cli.pl
  The command that installs certs, and sets up coolkey for cac-card access
  It changes only one firefox profile
  example usage: `./dod_firefox_cli_cfg.pl DOD-default`
 TODO Useful for Army, Navy, Air Force, and Marines TODO
 **WARN** Early alpha read the source before use **WARN**
 WIP Work in progress aka doesn't do what description says yet WIP
%prep
%setup -qn %{name}-%{commit0}

%build

%install
mkdir -p ${RPM_BUILD_ROOT}/%{_bindir}
cp firefox-usgov-dod-cfg-cli.pl ${RPM_BUILD_ROOT}/%{_bindir}

%files
%{_bindir}/firefox-usgov-dod-cfg-cli.pl
%doc README

%changelog
* Mon Jan 11 2016 Steve Pollei <stephen.pollei@gmail.com> 0.0.3-1
- whitespace cleanup
- added comments to source
- added rough draft of desktop file
* Tue Oct 27 2015 Steve Pollei <stephen.pollei@gmail.com> 0.0.2-2
- added perl(Gtk3)
* Fri Oct 23 2015 Steve Pollei <stephen.pollei@gmail.com> 0.0.2-1
- Transitioned over to using github
- added README
* Thu Oct 22 2015 Steve Pollei <stephen.pollei@gmail.com> 0.0.1-1
- first packaging
