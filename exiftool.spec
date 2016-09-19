Name:           Image-ExifTool
Version:        10.25
Release:        1%{?dist}
Summary:        ExifTool parses and processes camera EXIF information

Group:          Utilities
License:        This is free software; you can redistribute it and/or modify it under the same terms as Perl itself. (http://dev.perl.org/licenses/)
URL:            http://www.sno.phy.queensu.ca/~phil/exiftool/index.html
Source0:        http://www.sno.phy.queensu.ca/~phil/exiftool/Image-ExifTool-10.25.tar.gz

BuildRequires:  perl
Requires:       perl

%description


%prep
rm -rf $RPM_BUILD_DIR/Image-ExifTool-10.25
tar xvzf $RPM_SOURCE_DIR/Image-ExifTool-10.25.tar.gz
%setup -q


%build
# there was a percent configure here
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags} DESTDIR=$RPM_BUILD_ROOT

%install
make pure_install %{?_smp_mflags} DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test %{?_smp_mflags} DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc

%{perl_vendorlib}/*
%{_mandir}/man*
/usr/bin/exiftool

%changelog
* Mon Sep 19 2016 James Boyle <james.boyle@canonic.net>
- First build with RPM - let's git'r dun!
- pure_install - yay!
- vendorlib
