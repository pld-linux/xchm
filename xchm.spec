Summary:	CHM viewer for UNIX
Name:		xchm
Version:	0.5
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://belnet.dl.sourceforge.net/sourceforge/xchm/xchm-0.5.tar.gz
# Source0-md5:	18710e070c953b13be81953a8ce06637
URL:		http://xchm.sourceforge.net/
BuildRequires:	chmlib-devel
BuildRequires:	wxWindows-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CHM is a CHM viewer for UNIX, based on Jed Wing's CHMLIB and written with wxWindows.

%prep
%setup -q 

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
