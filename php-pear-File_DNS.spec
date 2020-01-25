%define		_status		devel
%define		_pearname	File_DNS
Summary:	%{_pearname} - Manipulate RFC1033-style DNS Zonefiles
Summary(pl.UTF-8):	%{_pearname} - Manipulacja plikami stref DNS w formacie RFC1033
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	65d7a55c5ea30cb2fb11ed99f41abf98
URL:		http://pear.php.net/package/File_DNS/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-File
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The File_DNS class provides a way to read, edit and write RFC1033
style DNS Zones.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa File_DNS dostarcza łatwego w użyciu sposobu do odczytu, edycji
oraz zapisu plików stref DNS w stylu RFC1033.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv docs/%{_pearname}/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/File/DNS.php

%{_examplesdir}/%{name}-%{version}
