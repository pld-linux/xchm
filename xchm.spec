#
# Conditional build:
%bcond_with	xmlrpc		# enable XmlRpc functionality
%bcond_without	unicode		# unicode version of wxGTK2
#
Summary:	CHM viewer for UNIX
Summary(pl.UTF-8):	Przeglądarka CHM dla Uniksów
Name:		xchm
Version:	1.23
Release:	4
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/xchm/%{name}-%{version}.tar.gz
# Source0-md5:	486d029bd81071a2d04e7181909b1602
Source1:	%{name}.desktop
Patch0:		wxWidgets3.patch
Patch1:		%{name}-pl.po-update.patch
URL:		http://xchm.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	chmlib-devel
BuildRequires:	gettext-tools >= 0.14.3
BuildRequires:	wxGTK2-%{?with_unicode:unicode-}devel >= 2.8.0
%if %{with xmlrpc}
# for configure check
BuildRequires:	openssl-devel
BuildRequires:	xmlrpc++-devel
%endif
Requires(post,postun):	desktop-file-utils
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
%patch1 -p1

%{__rm} po/stamp-po

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

# unify to short code pt=pt_PT
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{pt_PT,pt}
# fix Greek language code
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{gr,el}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README %{?with_xmlrpc:README.xmlrpc}
%attr(755,root,root) %{_bindir}/xchm
%{_desktopdir}/xchm.desktop
%{_pixmapsdir}/xchm*.png
%{_pixmapsdir}/xchm*.xpm
