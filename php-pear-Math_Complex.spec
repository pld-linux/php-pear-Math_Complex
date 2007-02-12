%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Complex
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_class}_%{_subclass} - Classes that define complex numbers and their operations
Summary(pl.UTF-8):   %{_class}_%{_subclass} - Klasy definiujące liczby zespolone i operacje na nich
Name:		php-pear-%{_pearname}
Version:	0.8.5
Release:	4
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	dcaa0672d9f0b29232d906b87e0cd3bf
URL:		http://pear.php.net/package/Math_Complex/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear-Math_TrigOp >= 1.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes that represent and manipulate complex numbers. Contain
definitions for basic arithmetic functions, as well as trigonometric,
inverse trigonometric, hyperbolic, inverse hyperbolic, exponential and
logarithms of complex numbers.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasy służące do reprezentacji i operacji na liczbach zespolonych.
Zawierają definicje podstawowych działań arytmetycznych, jak i
działania trygonometryczne, odwrotne do trygonometrycznych,
hiperboliczne, odwrotne do hiperbolicznych, wykładnicze i
logarytmiczne.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):   Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
