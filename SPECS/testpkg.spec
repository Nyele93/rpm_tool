Name:	        testpkg	
Version:	1.0.0
Release:	1%{?dist}
Summary:	A simple rpm package to check for existence of a Mariadb Database Service
BuildArch:      noarch

Group:		Unspecified
License:	GPL
URL:		https://github.com/Nyele93/rpm_tool
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	bash
BuildRequires:  gcc
Requires:	bash

%description
A simple rpm package to check for existence of a Mariadb Database Service

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{name} $RPM_BUILD_ROOT/%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc
%{_bindir}/%{name}


%changelog
* Sat Oct  29 2022 Michael Amadi <michael_amadi@myemal.com> - 1.0.0
- First version being packaged
