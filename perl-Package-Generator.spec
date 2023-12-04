#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Package-Generator
Version  : 1.106
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Package-Generator-1.106.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Package-Generator-1.106.tar.gz
Summary  : 'generate new packages quickly and easily'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Package-Generator-license = %{version}-%{release}
Requires: perl-Package-Generator-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Package-Generator,
version 1.106:
generate new packages quickly and easily

%package dev
Summary: dev components for the perl-Package-Generator package.
Group: Development
Provides: perl-Package-Generator-devel = %{version}-%{release}
Requires: perl-Package-Generator = %{version}-%{release}

%description dev
dev components for the perl-Package-Generator package.


%package license
Summary: license components for the perl-Package-Generator package.
Group: Default

%description license
license components for the perl-Package-Generator package.


%package perl
Summary: perl components for the perl-Package-Generator package.
Group: Default
Requires: perl-Package-Generator = %{version}-%{release}

%description perl
perl components for the perl-Package-Generator package.


%prep
%setup -q -n Package-Generator-1.106
cd %{_builddir}/Package-Generator-1.106

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Package-Generator
cp %{_builddir}/Package-Generator-1.106/LICENSE %{buildroot}/usr/share/package-licenses/perl-Package-Generator/1a2aa060407832e95b9058a74659a83d9679c308
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Package::Generator.3
/usr/share/man/man3/Package::Reaper.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Package-Generator/1a2aa060407832e95b9058a74659a83d9679c308

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
