Summary: GNU libmicrohttpd is a small C library that is supposed to make it easy to run an HTTP server as part of another application
Name: libmicrohttpd
Version: 0.9.50
Release: 1%{?dist}
License: GNU LGPL v2.1
Group: Libraries/Databases
URL: https://www.gnu.org/software/libmicrohttpd/

Source: http://ftp.gnu.org/gnu/libmicrohttpd/libmicrohttpd-0.9.50.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
#Requires: pango

%description
GNU libmicrohttpd is a small C library that is supposed
to make it easy to run an HTTP server as part of another application.

%package devel
Summary: libmicrohttpd development headers and static library
Group: Development/Libraries
#Requires: %{name} = %{version}

%description devel
GNU libmicrohttpd is a small C library that is
supposed to make it easy to run an HTTP server as part of another
application.  This package provides libraries and headers for
development

%package doc
Summary: libmicrohttpd documentation
Group: Development/Libraries
#Requires: %{name} = %{version}

%description doc
GNU libmicrohttpd is a small C library that is
supposed to make it easy to run an HTTP server as part of another
application.  This package provides documentation

%prep
%setup

%build
%configure --disable-shared --enable-static

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%pre

%post

%files

%files doc
%defattr(-, root, root, 0755)
%exclude %{_infodir}/dir
%{_infodir}/libmicrohttpd-tutorial.info.gz
%{_infodir}/libmicrohttpd.info.gz
%{_mandir}/man3/libmicrohttpd.3.gz

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/microhttpd.h
%{_libdir}/libmicrohttpd.a
%{_libdir}/libmicrohttpd.la
%{_libdir}/pkgconfig/libmicrohttpd.pc

%changelog
* Tue Nov 8 2016 rinigus <rinigus.git@gmail.com> - 0.9.50
- initial packaging release for SFOS
