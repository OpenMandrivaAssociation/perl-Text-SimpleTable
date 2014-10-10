%define upstream_name       Text-SimpleTable
%define upstream_version 2.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:	Simple Eyecandy ASCII Tables
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildArch:	noarch

%description
Simple eyecandy ASCII tables, as seen in Catalyst.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL -n INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Text/*
%{_mandir}/man3/*


%changelog
* Fri Mar 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 518485
- update to 2.03

* Wed Mar 10 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.20.0-1mdv2010.1
+ Revision: 517305
- update to 2.02

* Sun Mar 07 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.10.0-1mdv2010.1
+ Revision: 515368
- update to 2.01

* Thu Aug 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.0.0-1mdv2010.0
+ Revision: 410633
- update to 2.0

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.800.0-1mdv2010.0
+ Revision: 408088
- update to 1.8

* Fri Jul 17 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.400.0-1mdv2010.0
+ Revision: 396742
- update to 1.4

* Wed Jul 08 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.200.0-1mdv2010.0
+ Revision: 393406
- update to 1.2
- fixed license field

* Fri Jul 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.100.0-1mdv2010.0
+ Revision: 391954
- new version

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2009.0
+ Revision: 279069
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.03-5mdv2009.0
+ Revision: 242051
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.03-3mdv2008.0
+ Revision: 23640
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Wed Jan 18 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.03-1mdk
- 0.03

* Tue Dec 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-3mdk
- Add BuildRequires

* Mon Dec 19 2005 Buchan Milne <bgmilne@mandriva.org> 0.02-2mdk
- Rebuild
- use mkrel

* Fri Dec 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.02-1mdk
- Initial MDV package

