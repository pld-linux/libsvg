Summary:	A generic SVG library
Summary(pl):	Ogólna biblioteka SVG
Name:		libsvg
Version:	0.1.3
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	80c4a481eac386a9fef17811186b8ee9
Patch0:		%{name}-link.patch
URL:		http://www.xsvg.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.7
BuildRequires:	pkgconfig
Requires:	libxml2 >= 2.4.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libsvg provides a parser for SVG content in files or buffers. It
doesn't do any rendering, but instead provides a function-based
interface that can be used by various rendering engines.

%description -l pl
libsvg udostêpnia parser dla danych SVG z plików lub buforów. Nie
wykonuje ¿adnego renderingu, dostarcza jedynie oparty na funkcjach
interfejs, który mo¿na wykorzystaæ w ró¿nych silnikach renderuj±cych.

%package devel
Summary:	Header files for libsvg library
Summary(pl):	Pliki nag³ówkowe biblioteki libsvg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libxml2-devel >= 2.4.7

%description devel
Header files for libsvg library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libsvg.

%package static
Summary:	Static libsvg library
Summary(pl):	Statyczna biblioteka libsvg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsvg library.

%description static -l pl
Statyczna biblioteka libsvg.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
