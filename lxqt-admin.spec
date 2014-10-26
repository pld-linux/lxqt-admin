#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-admin
Name:		lxqt-admin
Version:	0.8.0
Release:	0.2
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	9589cab615160b7acc78b9d9c940098f
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.8.0
BuildRequires:	liboobs-devel 
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-about.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DUSE_QT5=ON \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-admin-time
%attr(755,root,root) %{_bindir}/lxqt-admin-user
%{_desktopdir}/lxqt-admin-time.desktop
%{_desktopdir}/lxqt-admin-user.desktop
