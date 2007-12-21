%define	module	Text-SimpleTable
%define	name	perl-%{module}
%define version 0.03
%define release %mkrel 3

Summary:	Simple Eyecandy ASCII Tables
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
BuildRequires:  perl(Module::Build)
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch

%description
Simple eyecandy ASCII tables, as seen in Catalyst.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%buildroot

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Text/*
%{_mandir}/man3/*

