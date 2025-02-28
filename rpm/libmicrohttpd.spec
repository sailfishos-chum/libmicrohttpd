Summary: library for adding an HTTP server as part of another application
Name: libmicrohttpd
Version: 0.9.77
Release: 1%{?dist}
License: GNU LGPL v2.1
Group: Development/Libraries
URL: https://www.gnu.org/software/libmicrohttpd/

Source: http://ftp.gnu.org/gnu/libmicrohttpd/libmicrohttpd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++ libtool texinfo
#Requires: pango

%description
GNU libmicrohttpd is a small C library that is supposed
to make it easy to run an HTTP server as part of another application.

PackageName: libmicrohttpd
Custom:
  Repo: https://github.com/sailfishos-chum/libmicrohttpd

%package devel
Summary: libmicrohttpd development headers and static library
Group: Development/Libraries
# fedora guidelines for static-only devel package:
Provides: %{name}-static
#Requires: %%{name} = %%{version}

%description devel
GNU libmicrohttpd is a small C library that is
supposed to make it easy to run an HTTP server as part of another
application.  This package provides libraries and headers for
development

PackageName: libmicrohttpd Development
Custom:
  Repo: https://github.com/sailfishos-chum/libmicrohttpd

%prep

%setup -q -n %{name}-%{version}/libmicrohttpd

%build 

%{__make} clean || true

./bootstrap

CFLAGS="$CFLAGS -fPIC"
CXXFLAGS="$CXXFLAGS -fPIC"
%configure --disable-shared --enable-static

%{make_build}

%install
%{make_install}
%{__rm} -rf %{buildroot}%{_infodir}/dir || true
%{__rm} -rf %{buildroot}%{_infodir}/libmicrohttpd* || true
%{__rm} -rf %{buildroot}%{_mandir}/* || true
%{__rm} -rf %{buildroot}%{_libdir}/libmicrohttpd.la || true

#%%files
#%%{_libdir}/libmicrohttpd.so*

%files devel
%{_includedir}/microhttpd.h
%{_libdir}/libmicrohttpd.a
%{_libdir}/pkgconfig/libmicrohttpd.pc

%changelog
* Tue Nov 8 2016 rinigus <rinigus.git@gmail.com> - 0.9.50
- initial packaging release for SFOS
