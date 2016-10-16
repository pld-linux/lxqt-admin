#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-admin
Name:		lxqt-admin
Version:	0.11.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	6aab9917a9cf9f5c2c5d9f542e37ed11
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.11.0
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-admin.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DPULL_TRANSLATIONS=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{name}-time --with-qm
#%find_lang %{name}-user --with-qm -a %{name}-time.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%dir %{_datadir}/lxqt/translations/%{name}-time
#%dir %{_datadir}/lxqt/translations/%{name}-user
%attr(755,root,root) %{_bindir}/lxqt-admin-time
%attr(755,root,root) %{_bindir}/lxqt-admin-user
%{_desktopdir}/lxqt-admin-time.desktop
%{_desktopdir}/lxqt-admin-user.desktop

%attr(755,root,root) %{_bindir}/lxqt-admin-user-helper
%{_datadir}/polkit-1/actions/org.lxqt.lxqt-admin-user.policy
