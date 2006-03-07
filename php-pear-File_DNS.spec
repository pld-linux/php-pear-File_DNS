%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	DNS
%define		_status		devel
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Manipulate RFC1033-style DNS Zonefiles
Summary(pl):	%{_pearname} - Manipulacja plikami stref DNS w formacie RFC1033
Name:		php-pear-%{_pearname}
Version:	0.0.8
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3479d0aee8cc42cd2a811fd3fbc9ef8a
URL:		http://pear.php.net/package/File_DNS/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-File
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The File_DNS class provides a way to read, edit and write RFC1033
style DNS Zones.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa File_DNS dostarcza ³atwego w u¿yciu sposobu do odczytu, edycji
oraz zapisu plików stref DNS w stylu RFC1033.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
