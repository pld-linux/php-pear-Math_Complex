%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Complex
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Classes that define complex numbers and their operations
Summary(pl):	%{_class}_%{_subclass} - Klasy definiuj±ce liczby zespolone i operacje na nich
Name:		php-pear-%{_pearname}
Version:	0.8.5
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	dcaa0672d9f0b29232d906b87e0cd3bf
URL:		http://pear.php.net/package/Math_Complex/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes that represent and manipulate complex numbers. Contain
definitions for basic arithmetic functions, as well as trigonometric,
inverse trigonometric, hyperbolic, inverse hyperbolic, exponential and
logarithms of complex numbers.

In PEAR status of this package is: %{_status}.

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
