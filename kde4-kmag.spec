%define		_state		stable
%define		orgname		kamera
%define		qtver		4.8.1

Summary:	K Desktop Environment - A screen magnifier
Summary(pl.UTF-8):	K Desktop Environment - Powiększalnik ekranu
Name:		kde4-kamera
Version:	4.9.0
Release:	1
License:	GPLv2
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	7b15ced4fc547941ff943462ba4a2bdc
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	perl
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	xorg-lib-libX11-devel
Requires:	kde4-kaccessible >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K Desktop Environment - A screen magnifier.

%description -l pl.UTF-8
K Desktop Environment - Powiększalnik ekranu.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_kamera.so
%attr(755,root,root) %{_libdir}/kde4/kio_kamera.so
%{_datadir}/kde4/services/kamera.desktop
%{_datadir}/kde4/services/camera.protocol
%{_kdedocdir}/en/kcontrol/kamera
%{_datadir}/apps/solid/actions/solid_camera.desktop