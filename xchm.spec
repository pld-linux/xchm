Summary:	CHM viewer for UNIX
Summary(pl):	Przegl±darka CHM dla Uniksów
Name:		xchm
Version:	0.9.5
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/xchm/%{name}-%{version}.tar.gz
# Source0-md5:	743c03c91a009a394fc1231f4a1d1e84
Source1:	%{name}.desktop
URL:		http://xchm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	chmlib-devel
BuildRequires:	gettext-devel >= 0.11
BuildRequires:	wxGTK2-devel >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XCHM is a CHM viewer for UNIX, based on Jed Wing's CHMLIB and written
with wxWindows.

%description -l pl
XCHM to przegl±darka plików CHM dla Uniksa, napisana w oparciu o
CHMLIB Jeda Winga, z u¿yciem wxWindows.

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	WX_CONFIG_NAME=/usr/bin/wxgtk2-2.4-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install art/xchm-48.xpm	$RPM_BUILD_ROOT%{_pixmapsdir}/xchm.xpm
install %{SOURCE1}	$RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/xchm.xpm
