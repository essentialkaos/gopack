###############################################################################

Summary:         Tool for packing go package sources
Name:            gopack
Version:         1.1.0
Release:         0%{?dist}
Group:           Development/Tools
License:         EKOL
URL:             https://essentialkaos.com
Vendor:          ESSENTIAL KAOS

Source0:         https://source.kaos.io/%{name}/%{name}-%{version}.tar.bz2

BuildArch:       noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:        golang git mercurial

Provides:        %{name} = %{version}-%{release}

###############################################################################

%description
Simple tool for packing go package sources.

###############################################################################

%prep
%setup -q

%build
%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_bindir}
install -pm 775 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.EN LICENSE.RU
%{_bindir}/%{name}

###############################################################################

%changelog
* Wed Apr 27 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1.0-0
- Different output formats support

* Thu Apr 21 2016 Anton Novojilov <andy@essentialkaos.com> - 1.0.2-0
- Fixed typo in help content

* Wed Mar 30 2016 Anton Novojilov <andy@essentialkaos.com> - 1.0.1-0
- Fixed bug with installing packages after downloading

* Sat Mar 19 2016 Anton Novojilov <andy@essentialkaos.com> - 1.0.0-0
- Initial release
