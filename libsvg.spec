Summary:	A generic SVG library
Summary(pl.UTF-8):	Ogólna biblioteka SVG
Name:		libsvg
Version:	0.1.4
Release:	14
License:	LGPL v2+
Group:		Libraries
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	ce0715e3013f78506795fba16e8455d3
Patch0:		%{name}-link.patch
Patch1:		%{name}-pkgconfig.patch
Patch2:		%{name}-lt.patch
Patch3:		%{name}-libpng.patch
URL:		http://cairographics.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2.4
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
Requires:	libxml2 >= 1:2.6.26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libsvg provides a parser for SVG content in files or buffers. It
doesn't do any rendering, but instead provides a function-based
interface that can be used by various rendering engines.

%description -l pl.UTF-8
libsvg udostępnia parser dla danych SVG z plików lub buforów. Nie
wykonuje żadnego renderingu, dostarcza jedynie oparty na funkcjach
interfejs, który można wykorzystać w różnych silnikach renderujących.

%package devel
Summary:	Header files for libsvg library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsvg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libxml2-devel >= 1:2.6.26

%description devel
Header files for libsvg library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsvg.

%package static
Summary:	Static libsvg library
Summary(pl.UTF-8):	Statyczna biblioteka libsvg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsvg library.

%description static -l pl.UTF-8
Statyczna biblioteka libsvg.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	LIBS="-lm -lz"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libsvg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsvg.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsvg.so
%{_libdir}/libsvg.la
%{_includedir}/svg.h
%{_pkgconfigdir}/libsvg.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsvg.a
