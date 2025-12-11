#
# Conditional build:
#
%define		qtver		6.6.0

Summary:	LXQt system administration tool
Summary(pl.UTF-8):	Narzędzie LXQt do administrowania systemem
Name:		lxqt-admin
Version:	2.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	https://github.com/lxqt/lxqt-admin/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	904f6d464b52e3a68ca6df9fd7e79d16
URL:		http://www.lxqt.org/
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	liblxqt-devel >= 2.3.0
BuildRequires:	polkit-qt6-1-devel
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides tools to adjust settings of the operating system
LXQt is running on. Both can be launched from GUI "Configuration
Center".

GUI "Time and date configuration", binary lxqt-admin-time, can be used
to adjust the system time of the operating system as well as the
timezone.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia do dostosowywania ustawień systemu
operacyjnego, na którym działa LXQt. Oba można uruchomić z graficznego
interfejsu użytkownika „Centrum konfiguracji”.

GUI „Konfiguracja czasu i daty”, plik binarny lxqt-admin-time,
umożliwia dostosowanie czasu systemowego oraz strefy czasowej.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-admin-time
%attr(755,root,root) %{_bindir}/lxqt-admin-user
%{_desktopdir}/lxqt-admin-time.desktop
%{_desktopdir}/lxqt-admin-user.desktop
%attr(755,root,root) %{_bindir}/lxqt-admin-user-helper
%{_datadir}/polkit-1/actions/org.lxqt.lxqt-admin-user.policy
# for the lang files
%dir %{_datadir}/lxqt/translations/%{name}-time
%dir %{_datadir}/lxqt/translations/%{name}-user
