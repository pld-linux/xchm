Summary:	CHM viewer for UNIX
Summary(pl):	Przegl�darka CHM dla uniks�w
Name:		xchm
Version:	0.6.1
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/xchm/%{name}-%{version}.tar.gz
# Source0-md5:	71b2041f45e5984ad549cfbf7ce9e703
Patch0:		%{name}-configure.patch
URL:		http://xchm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	chmlib-devel
BuildRequires:	wxGTK2-devel >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XCHM is a CHM viewer for UNIX, based on Jed Wing's CHMLIB and written
with wxWindows.

%description -l pl
XCHM to przegl�darka plik�w CHM dla uniksa, napisana w oparciu o
CHMLIB Jeda Winga, z u�yciem wxWindows.

%prep
%setup -q
%patch -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	WXCFG=/usr/bin/wxgtk2-2.4-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
