#
# Conditional build:
%bcond_with	xmlrpc			# Enable XmlRpc functionality
%bcond_without	unicode			# unicode version of wxGTK2
#
Summary:	CHM viewer for UNIX
Summary(pl.UTF-8):	Przeglądarka CHM dla Uniksów
Name:		xchm
Version:	1.13
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/xchm/%{name}-%{version}.tar.gz
# Source0-md5:	b444e36d6f1c7b3d772d1986ea9929dc
Source1:	%{name}.desktop
Patch0:		%{name}-compile.patch
URL:		http://xchm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	chmlib-devel
BuildRequires:	gettext-devel >= 0.14.3
BuildRequires:	wxGTK2-%{?with_unicode:unicode-}devel >= 2.6.0
%{?with_xmlrpc:BuildRequires:	xmlrpc++-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xCHM is a CHM viewer for UNIX, based on Jed Wing's CHMLIB and written
with wxWidgets.

%description -l pl.UTF-8
xCHM to przeglądarka plików CHM dla Uniksa, napisana w oparciu o
CHMLIB Jeda Winga, z użyciem wxWidgets.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_xmlrpc:--enable-xmlrpc} \
	WX_CONFIG_NAME=%{_bindir}/wx-gtk2-%{!?with_unicode:ansi}%{?with_unicode:unicode}-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install art/xchm-48.xpm	$RPM_BUILD_ROOT%{_pixmapsdir}/xchm.xpm
install %{SOURCE1}	$RPM_BUILD_ROOT%{_desktopdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{pt_PT,pt}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%if %{with xmlrpc}
%doc README.xmlrpc
%endif
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.xpm
