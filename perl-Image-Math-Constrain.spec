%define upstream_name    Image-Math-Constrain
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Scaling math used in image size constraining (such
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Image/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
There are a number of different modules and systems that constrain image
sizes, such as thumbnailing. Every one of these independantly implement the
same logic. That is, given a width and/or height constraint, they check to
see if the image is bigger than the constraint, and if so scale the image
down proportionally so that it fits withint the constraints.

Of course, they all do it slightly differnetly, and some do it better than
others.

'Image::Math::Constrain' has been created specifically to implement this
logic once, and implement it properly. Any module or script that does image
size constraining or thumbnailing should probably be using this for its
math.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.20.0-2mdv2011.0
+ Revision: 654240
- rebuild for updated spec-helper

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 471089
- import perl-Image-Math-Constrain


* Sun Nov 29 2009 cpan2dist 1.02-1mdv
- initial mdv release, generated with cpan2dist
