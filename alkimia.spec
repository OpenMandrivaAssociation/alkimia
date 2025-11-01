%define major 8
%define libname %mklibname alkimia5 %{major}
%define devname %mklibname alkimia5 -d
%define stable %([ "%(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%global __requires_exclude ^.*cmake.*::.*$

Summary: Common storage and business logic for financial applications
Name: alkimia
Version: 8.2.1
Release: 1
URL: https://community.kde.org/Alkimia
License: GPL
Group: System/Libraries
Source0: http://download.kde.org/%{stable}/alkimia/%{version}/%{name}-%{version}.tar.xz
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6WebEngineCore)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Plasma)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6Package)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(VulkanHeaders)
BuildRequires: pkgconfig(gmpxx)
BuildRequires: doxygen
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
%autosetup -p1
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DAPPDATA_INSTALL_DIR=%{_datadir} \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang alkimia --all-name

%files -f alkimia.lang
%{_datadir}/knsrcfiles/*.knsrc
%{_bindir}/onlinequoteseditor6
%{_datadir}/applications/org.kde.onlinequoteseditor6.desktop
%{_datadir}/icons/hicolor/*/apps/onlinequoteseditor6.*
%{_datadir}/metainfo/org.kde.onlinequoteseditor6.appdata.xml
%{_qtdir}/qml/org/kde/alkimia6
%{_datadir}/plasma/plasmoids/org.wincak.foreigncurrencies26

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/LibAlkimia6-%(echo %{version} |cut -d. -f1-2)
%{_libdir}/pkgconfig/libalkimia6.pc
%{_datadir}/gdb/auto-load%{_libdir}/libalkimia6.so.*-gdb.py
