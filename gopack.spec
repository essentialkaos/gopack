###############################################################################

Summary:         Tool for packing Go package sources
Name:            gopack
Version:         1.5.0
Release:         0%{?dist}
Group:           Development/Tools
License:         EKOL
URL:             https://github.com/essentialkaos/gopack

Source0:         https://source.kaos.io/%{name}/%{name}-%{version}.tar.bz2

BuildArch:       noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:        golang git mercurial curl

Provides:        %{name} = %{version}-%{release}

###############################################################################

%description
Simple tool for packing golang packages sources with all dependencies.

###############################################################################

%package build

Summary:         Tool for building binaries from sources archive
Version:         1.0.0
Release:         0%{?dist}
Group:           Development/Tools

%description build
Tool for building binaries from sources archive.

###############################################################################

%prep
%setup -q

%build
%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_bindir}
install -pm 775 %{name} %{buildroot}%{_bindir}/%{name}
install -pm 775 %{name} %{buildroot}%{_bindir}/%{name}-build

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.EN LICENSE.RU
%{_bindir}/%{name}

%files build
%defattr(-,root,root,-)
%doc LICENSE.EN LICENSE.RU
%{_bindir}/%{name}-build

###############################################################################

%changelog
* Thu May 11 2017 Anton Novojilov <andy@essentialkaos.com> - 1.5.0-0
- [gopack] Improved usage info output
- [gopack] Improved glide support
- [gopack] Added dep support

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
