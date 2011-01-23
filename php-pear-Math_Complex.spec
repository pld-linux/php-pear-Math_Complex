%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Math_Complex
Summary:	%{_class}_%{_subclass} - Classes that define complex numbers and their operations
Summary(pl.UTF-8):	%{_class}_%{_subclass} - Klasy definiujące liczby zespolone i operacje na nich
Name:		php-pear-%{_pearname}
Version:	0.8.6
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	41e91c490b7d22a0558fab545c5dcaec
URL:		http://pear.php.net/package/Math_Complex/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Math_TrigOp >= 1.0
Obsoletes:	php-pear-Math_Complex-tests
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

%prep
%pear_package_setup

mv docs/Math_Complex/docs/examples .

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
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Math/Complex.php
%{php_pear_dir}/Math/ComplexOp.php

%{php_pear_dir}/data/%{_pearname}

%{_examplesdir}/%{name}-%{version}
