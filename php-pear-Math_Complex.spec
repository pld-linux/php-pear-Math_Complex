%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Complex
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Classes that define complex numbers and their operations
Summary(pl):	%{_class}_%{_subclass} - Klasy definiuj±ce liczby zespolone i operacje na nich
Name:		php-pear-%{_pearname}
Version:	0.8
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	5f68870729e50c796ccd81e3487d7673
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes that represent and manipulate complex numbers. Contain
definitions for basic arithmetic functions, as well as trigonometric,
inverse trigonometric, hyperbolic, inverse hyperbolic, exponential and
logarithms of complex numbers.

This class has in PEAR status: %{_status}.

%description -l pl
Klasy s³u¿±ce do reprezentacji i operacji na liczbach zespolonych.
Zawieraj± definicje podstawowych dzia³añ arytmetycznych, jak i
dzia³ania trygonometryczne, odwrotne do trygonometrycznych,
hiperboliczne, odwrotne do hiperbolicznych, wyk³adnicze i
logarytmiczne.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
