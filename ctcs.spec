Summary:	CTorrent Control Server
Summary(pl.UTF-8):	Serwer sterujący dla CTorrenta
Name:		ctcs
Version:	1.4
Release:	1
License:	distributable
Group:		Applications
Source0:	http://www.rahul.net/dholmes/ctorrent/%{name}-%{version}.tar.gz
# Source0-md5:	9ada24b81665ed8f18c5d3023298c5a3
URL:		http://www.rahul.net/dholmes/ctorrent/ctcs.html
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CTorrent Control Server (CTCS) is an interface for monitoring and
managing Enhanced CTorrent clients. It can manage allocation of
bandwidth, provide status information, and allow changes to the
running configuration of each client. Communication with CTorrent is
via a TCP connection, and the user interface is a web browser.

%description -l pl.UTF-8
CTorrent Control Server (CTCS) to interfejs do monitorowania i
zarządzania klientami rozszerzonego CTorrenta. Może on zarządzać
przydzielaniem pasma, udostępniać informacje o stanie i pozwalać na
zmiany w aktualnej konfiguracji każdego działającego klienta.
Komunikacja z CTorrentem odbywa się przez połączenie TCP, a
interfejsem użytkownika jest przeglądarka WWW.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ctcs $RPM_BUILD_ROOT%{_bindir}/ctcs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/ctcs
