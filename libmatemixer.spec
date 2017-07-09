%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major		0
%define libname		%mklibname matemixer %{major}
%define develname	%mklibname -d matemixer

Summary:	A mixer library for MATE desktop
Name:		libmatemixer
Version:	1.18.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Sound
Url:		https://www.mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	gtk-doc
BuildRequires:	mate-common
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(alsa)

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides libmatemixer, a mixer library for MATE desktop.

libmatemixer provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Requires:	matemixer-backend

%description -n %{libname}
This package contains libraries used by %{name}.

%files -n %{libname} -f %{name}.lang
%doc AUTHORS COPYING README
%{_libdir}/%{name}.so.%{major}*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}-null.so

#---------------------------------------------------------------------------

%package -n matemixer-backend-pulse
Summary:	PulseAudio backend for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	matemixer-backend = %{version}-%{release}

%description -n matemixer-backend-pulse
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package is part of libmatemixer, a mixer library for MATE desktop.

libmatemixer provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

This package provides PulseAudio backend for libmatemixer. If you prefer to
use ALSA or OSS backend install matemixer-backend-alsa or
matemixer-backend-oss packages.

%files -n matemixer-backend-pulse
%{_libdir}/%{name}/%{name}-pulse.so

#---------------------------------------------------------------------------

%package -n matemixer-backend-alsa
Summary:	ALSA backend for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	matemixer-backend = %{version}-%{release}

%description -n matemixer-backend-alsa
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package is part of libmatemixer, a mixer library for MATE desktop.

libmatemixer provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

This package provides ALSA backend for libmatemixer. If you prefer to
use PulseAudio or OSS backend install matemixer-backend-pulse or
matemixer-backend-oss packages.

%files -n matemixer-backend-alsa
%{_libdir}/%{name}/%{name}-alsa.so

#---------------------------------------------------------------------------

%package -n matemixer-backend-oss
Summary:	OSS backend for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	matemixer-backend = %{version}-%{release}

%description -n matemixer-backend-oss
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package is part of libmatemixer, a mixer library for MATE desktop.

libmatemixer provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

This package provides OSS backend for libmatemixer. If you prefer to
use PulseAudio or ALSA backend install matemixer-backend-pulse or
matemixer-backend-alsa packages.

%files -n matemixer-backend-oss
%{_libdir}/%{name}/%{name}-oss.so

#---------------------------------------------------------------------------

%package -n %{develname}
Group:		Development/C
Summary:	Devel files for Mate Mixer Library
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains libraries and includes files for developing programs
based on %{name}.

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/%{name}
%{_libdir}/libmatemixer.so
%{_libdir}/pkgconfig/libmatemixer.pc
%{_includedir}/mate-mixer/

#---------------------------------------------------------------------------

%prep
%setup -q

%build
#NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-oss \
	--enable-gtk-doc \
	%{nil}
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome --all-name

