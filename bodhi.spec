%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

Name:           bodhi
Version:        0.2.0
Release:        1%{?dist}
Summary:        A modular web-system that facilitates the process of publishing updates for a Fedora-based software distribution

Group:          Applications/Internet
License:        GPLv2
URL:            https://hosted.fedoraproject.org/projects/bodhi
Source0:        bodhi-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-setuptools

%description
Bodhi is a modular web system that facilitates the process of publishing
updates for a software distribution.

%package client
Summary: Bodhi Client
Group: Applications/Internet

%description client 
Client tools for interacting with bodhi


%package server
Summary: Bodhi Server
Group: Applications/Internet
Requires: TurboGears createrepo python-TurboMail yum-utils intltool mash

%description server
The bodhi server

%prep
%setup -q


%build
make build


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT


%files server
%defattr(-,root,root,-)
%doc README
%{_bindir}/start-bodhi.py*
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py%{pyver}.egg-info

%files client
%{_bindir}/bodhi


%changelog
* Thu Sep 13 2007 Luke Macken <lmacken@redhat.com> - 0.2.0-1
- Split spec file into client/server subpackages
