%define major 8
%define libname %mklibname alkimia5 %{major}
%define devname %mklibname alkimia5 -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		alkimia
Version:	8.0.3
Release:	1
Source0: http://download.kde.org/%{stable}/alkimia/%{version}/%{name}-%{version}.tar.xz
Summary: Common storage and business logic for financial applications
URL: http://community.kde.org/Alkimia
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5WebKit)
BuildRequires: cmake(Qt5WebKitWidgets)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: doxygen qt5-assistant
BuildRequires: gmp-devel

%description
Alkimia is the infrastructure for common storage and business logic that will
be used by all financial applications in KDE. The target is to share financial
related information over application boundaries.

%package -n %{libname}
Summary: Common storage and business logic for financial applications
Group: System/Libraries

%description -n %{libname}
Alkimia is the infrastructure for common storage and business logic that will
be used by all financial applications in KDE. The target is to share financial
related information over application boundaries.

%package -n %{devname}
Summary: Development files for the Alkimia financial system
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Alkimia is the infrastructure for common storage and business logic that will
be used by all financial applications in KDE. The target is to share financial
related information over application boundaries.

%prep
%setup -q
%cmake_kde5 \
	-DAPPDATA_INSTALL_DIR=%{_datadir}

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang alkimia --all-name

%files -f alkimia.lang
%{_sysconfdir}/xdg/*.knsrc
%{_bindir}/onlinequoteseditor5
%{_datadir}/applications/org.kde.onlinequoteseditor5.desktop
%{_datadir}/alkimia5/misc/financequote.pl
%{_libdir}/qt5/qml/org/kde/alkimia
%{_datadir}/icons/hicolor/*/apps/onlinequoteseditor5.*
%{_datadir}/kservices5/plasma-applet-org.wincak.foreigncurrencies2.desktop
%{_datadir}/metainfo/org.wincak.foreigncurrencies2.appdata.xml
%{_datadir}/plasma/plasmoids/org.wincak.foreigncurrencies2

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/LibAlkimia5-%(echo %{version} |cut -d. -f1-2)
%{_libdir}/pkgconfig/libalkimia5.pc