################################################################################

Summary:    Tool for packing Go package sources
Name:       gopack
Version:    1.13.2
Release:    0%{?dist}
Group:      Development/Tools
License:    Apache License, Version 2.0
URL:        https://kaos.sh/gopack

Source0:    https://source.kaos.st/%{name}/%{name}-%{version}.tar.bz2

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:   golang git curl

Provides:   %{name} = %{version}-%{release}

################################################################################

%description
Simple tool for packing golang packages sources with all dependencies.

################################################################################

%package build

Summary:   Tool for building binaries from sources archive created by gopack
Version:   1.2.6
Release:   0%{?dist}
Group:     Development/Tools

Requires:  golang git curl

%description build
Tool for building binaries from sources archive created by gopack.

################################################################################

%prep
%setup -q

%build
%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_bindir}
install -pm 775 %{name} %{buildroot}%{_bindir}/%{name}
install -pm 775 %{name}-build %{buildroot}%{_bindir}/%{name}-build

%clean
rm -rf %{buildroot}

################################################################################

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/%{name}

%files build
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/%{name}-build

################################################################################

%changelog
* Wed Feb 22 2023 Anton Novojilov <andy@essentialkaos.com> - 1.13.2-0
- [gopack|gopack-build] Fixed --no-color option handling
- [gopack-build] Improved remote file availability check
- [gopack|gopack-build] Code refactoring

* Fri Feb 03 2023 Anton Novojilov <andy@essentialkaos.com> - 1.13.1-0
- [gopack|gopack-build] Code refactoring

* Tue Apr 12 2022 Anton Novojilov <andy@essentialkaos.com> - 1.13.0-0
- [gopack] Added result signing feature

* Thu Aug 26 2021 Anton Novojilov <andy@essentialkaos.com> - 1.12.0-0
- [gopack] Fixed bug with packing sources using 'go mod'
- [gopack] Improved sources cleanup

* Sat Apr 03 2021 Anton Novojilov <andy@essentialkaos.com> - 1.11.0-0
- [gopack] Added clone depth configuration option

* Sat Apr 03 2021 Anton Novojilov <andy@essentialkaos.com> - 1.10.4-0
- [gopack|gopack-build] Code refactoring
- [gopack|gopack-build] Minor UI fixes

* Fri Jun 05 2020 Anton Novojilov <andy@essentialkaos.com> - 1.10.3-1
- [gopack-build] Fixed problems reported by shellcheck

* Wed Dec 04 2019 Anton Novojilov <andy@essentialkaos.com> - 1.10.3-0
- Removed handler for script errors

* Sat Nov 30 2019 Anton Novojilov <andy@essentialkaos.com> - 1.10.2-0
- Added handling of SCRIPT_DEBUG environment variable for enabling debug mode
- Added handler for script errors

* Thu Jul 18 2019 Anton Novojilov <andy@essentialkaos.com> - 1.10.1-0
- Minor UI improvement

* Thu Jul 04 2019 Anton Novojilov <andy@essentialkaos.com> - 1.10.0-0
- [gopack] Added a new way to remove useless source code after installing
  package managers
- [gopack] Added go mod support
- [gopack] Improved source downloading mechanics
- [gopack-build] Added XZ support

* Wed May 01 2019 Anton Novojilov <andy@essentialkaos.com> - 1.9.0-0
- [gopack] Added XZ support
- [gopack] Improved sources cleanup
- [gopack] Minor UI improvements

* Wed Jan 23 2019 Anton Novojilov <andy@essentialkaos.com> - 1.8.4-0
- [gopack] Fixed bug with checking used dependency manager

* Sun May 06 2018 Anton Novojilov <andy@essentialkaos.com> - 1.8.3-0
- [gopack|gopack-build] Minor UI improvements

* Tue Dec 12 2017 Anton Novojilov <andy@essentialkaos.com> - 1.8.2-0
- [gopack|gopack-build] Code refactoring

* Mon Oct 09 2017 Anton Novojilov <andy@essentialkaos.com> - 1.8.1-0
- [gopack] Improved output name generation

* Mon Sep 18 2017 Anton Novojilov <andy@essentialkaos.com> - 1.8.0-0
- [gopack] Always try to find and use used dependency manager
- [gopack] Fixed bug with handling errors while package fetching
- [gopack] Fixed bug with using dep dependency manager

* Thu Aug 10 2017 Anton Novojilov <andy@essentialkaos.com> - 1.7.0-0
- [gopack] Improved default output name generation

* Sat May 20 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.1-0
- [gopack] Improved problems handling with output name generation

* Wed May 17 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.0-0
- [gopack] Improved default output name generation
- [gopack] Added elapsed time for actions

* Fri May 12 2017 Anton Novojilov <andy@essentialkaos.com> - 1.5.1-0
- [gopack] Fixed bug with using relative path in output

* Thu May 11 2017 Anton Novojilov <andy@essentialkaos.com> - 1.5.0-0
- [gopack-build] Improved usage info output
- [gopack] Different dependency management tools support
- [gopack] Improved usage info output
- [gopack] Code refactoring
- [gopack] Empty directories removal

* Mon Apr 24 2017 Anton Novojilov <andy@essentialkaos.com> - 1.4.0-0
- Added gopack-build utility (tool for building binaries from sources archive)
- [gopack] Added handler for TERM/QUIT/INT signals
- [gopack] Arguments parser updated to v3 with fixed stderr output redirection
  for showArgWarn and showArgValWarn functions
- [gopack] Added info about -nc/--no-colors argument
- [gopack] Code refactoring

* Wed Apr 05 2017 Anton Novojilov <andy@essentialkaos.com> - 1.3.4-0
- Fixed output to stderr for a message about an unsupported argument

* Wed Apr 05 2017 Anton Novojilov <andy@essentialkaos.com> - 1.3.3-0
- Output errors to stderr

* Mon Mar 27 2017 Anton Novojilov <andy@essentialkaos.com> - 1.3.2-0
- Added git configuration for pkg.re/gopkg.in

* Wed Feb 15 2017 Anton Novojilov <andy@essentialkaos.com> - 1.3.1-0
- Improved version output

* Sat Nov 26 2016 Anton Novojilov <andy@essentialkaos.com> - 1.3.0-0
- Glide support
- Fixed a bug with packing sources into archive without extension

* Thu Nov 17 2016 Anton Novojilov <andy@essentialkaos.com> - 1.2.0-0
- Code refactoring

* Tue Nov 01 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1.2-0
- UI improvements

* Wed Apr 27 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1.0-0
- Different output formats support

* Thu Apr 21 2016 Anton Novojilov <andy@essentialkaos.com> - 1.0.2-0
- Fixed typo in help content

* Wed Mar 30 2016 Anton Novojilov <andy@essentialkaos.com> - 1.0.1-0
- Fixed bug with installing packages after downloading

* Sat Mar 19 2016 Anton Novojilov <andy@essentialkaos.com> - 1.0.0-0
- Initial release
