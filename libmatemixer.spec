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
libmatemixer is a mixer library for MATE desktop.
It provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

Documentation for the API is provided with gtk-doc

%package -n %{libname}
Group:		System/Libraries
Summary:	%{summary}
Requires:	matemixer-backend

%description -n %{libname}
libmatemixer is a mixer library for MATE desktop.
It provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

%package -n %{develname}
Group:		Development/C
Summary:	Devel files for Mate Mixer Library
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files with mateweather libraries.

%package -n matemixer-backend-pulse
Group:		System/Libraries
Summary:	PulseAudio backend for %{name}
Requires:	%{libname} = %{version}-%{release}
Provides:	matemixer-backend = %{version}-%{release}
Obsoletes:	mate-settings-daemon-pulse
Obsoletes:	mate-media-pulse

%description -n matemixer-backend-pulse
libmatemixer is a mixer library for MATE desktop.
It provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

This package provides PulseAudio backend for libmatemixer.
If you want to use ALSA or OSS backend install 
matemixer-backend-alsa or matemixer-backend-oss packages.

%package -n matemixer-backend-alsa
Group:		System/Libraries
Summary:	ALSA backend for %{name}
Requires:	%{libname} = %{version}-%{release}
Provides:	matemixer-backend = %{version}-%{release}
Obsoletes:	mate-settings-daemon-gstreamer
Obsoletes:	mate-media-gstreamer

%description -n matemixer-backend-alsa
libmatemixer is a mixer library for MATE desktop.
It provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

This package provides ALSA backend for libmatemixer.
If you want to use PulseAudio or OSS backend install 
matemixer-backend-pulse or matemixer-backend-oss packages.

%package -n matemixer-backend-oss
Group:		System/Libraries
Summary:	OSS backend for %{name}
Requires:	%{libname} = %{version}-%{release}
Provides:	matemixer-backend = %{version}-%{release}
Obsoletes:	mate-settings-daemon-gstreamer
Obsoletes:	mate-media-pulse-gstreamer

%description -n matemixer-backend-oss
libmatemixer is a mixer library for MATE desktop.
It provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

This package provides OSS backend for libmatemixer.
If you want to use PulseAudio or ALSA backend install 
matemixer-backend-pulse or matemixer-backend-alsa packages.

%prep
%setup -q

%build
#NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-oss \
	%{nil}
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome --all-name

%files -n %{libname} -f %{name}.lang
%doc AUTHORS COPYING README
%{_libdir}/%{name}.so.%{major}*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}-null.so

%files -n matemixer-backend-pulse
%{_libdir}/%{name}/%{name}-pulse.so

%files -n matemixer-backend-alsa
%{_libdir}/%{name}/%{name}-alsa.so

%files -n matemixer-backend-oss
%{_libdir}/%{name}/%{name}-oss.so

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/%{name}
%{_libdir}/libmatemixer.so
%{_libdir}/pkgconfig/libmatemixer.pc
%{_includedir}/mate-mixer/

