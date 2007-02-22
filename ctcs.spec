#
%include	/usr/lib/rpm/macros.perl
#
Summary:	CTorrent Control Server
Summary(pl.UTF-8):	Serwer sterujący dla CTorrent
Name:		ctcs
Version:	1.2
Release:	1
License:	distributable
Group:		Applications
Source0:	http://www.rahul.net/dholmes/ctorrent/%{name}-%{version}.tar.gz
# Source0-md5:	cd8f9b28a846f89b1d35827d28489abc
URL:		http://www.rahul.net/dholmes/ctorrent/ctcs.html
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CTorrent Control Server (CTCS) is an interface for monitoring and managing
Enhanced CTorrent clients. It can manage allocation of bandwidth, provide
status information, and allow changes to the running configuration of each
client. Communication with CTorrent is via a TCP connection, and the user
interface is a web browser.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ctcs.new $RPM_BUILD_ROOT%{_bindir}/ctcs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/ctcs
