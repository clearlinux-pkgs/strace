#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA8041FA839E16E36 (ldv@altlinux.org)
#
Name     : strace
Version  : 6.1
Release  : 58
URL      : https://github.com/strace/strace/releases/download/v6.1/strace-6.1.tar.xz
Source0  : https://github.com/strace/strace/releases/download/v6.1/strace-6.1.tar.xz
Source1  : https://github.com/strace/strace/releases/download/v6.1/strace-6.1.tar.xz.asc
Summary  : Tracks and displays system calls associated with a running process
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.1 LGPL-2.1+
Requires: strace-bin = %{version}-%{release}
Requires: strace-license = %{version}-%{release}
Requires: strace-man = %{version}-%{release}
BuildRequires : btrfs-progs-dev
BuildRequires : libunwind-dev
BuildRequires : valgrind

%description
The strace program intercepts and records the system calls called and
received by a running process.  Strace can print a record of each
system call, its arguments and its return value.  Strace is useful for
diagnosing problems and debugging, as well as for instructional
purposes.

Install strace if you need a tool to track the system calls made and
received by a process.

%package bin
Summary: bin components for the strace package.
Group: Binaries
Requires: strace-license = %{version}-%{release}

%description bin
bin components for the strace package.


%package extras
Summary: extras components for the strace package.
Group: Default

%description extras
extras components for the strace package.


%package license
Summary: license components for the strace package.
Group: Default

%description license
license components for the strace package.


%package man
Summary: man components for the strace package.
Group: Default

%description man
man components for the strace package.


%prep
%setup -q -n strace-6.1
cd %{_builddir}/strace-6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670894829
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --with-libunwind \
--enable-mpers=no
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1670894829
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/strace
cp %{_builddir}/strace-%{version}/COPYING %{buildroot}/usr/share/package-licenses/strace/5e5aac2444f406ba1f796ceff6887fc3b1def247 || :
cp %{_builddir}/strace-%{version}/bundled/linux/COPYING %{buildroot}/usr/share/package-licenses/strace/3f9f7be18936296d848182000ba3a63a240e0db1 || :
cp %{_builddir}/strace-%{version}/debian/copyright %{buildroot}/usr/share/package-licenses/strace/d3cbcf91f3a68d195eb9a558d54fd07c55f4faea || :
cp %{_builddir}/strace-%{version}/tests-m32/COPYING %{buildroot}/usr/share/package-licenses/strace/c25e42893e9414a57ab2948804b87f37b1ee8c1a || :
cp %{_builddir}/strace-%{version}/tests-mx32/COPYING %{buildroot}/usr/share/package-licenses/strace/c25e42893e9414a57ab2948804b87f37b1ee8c1a || :
cp %{_builddir}/strace-%{version}/tests/COPYING %{buildroot}/usr/share/package-licenses/strace/c25e42893e9414a57ab2948804b87f37b1ee8c1a || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/strace

%files extras
%defattr(-,root,root,-)
/usr/bin/strace-log-merge

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/strace/3f9f7be18936296d848182000ba3a63a240e0db1
/usr/share/package-licenses/strace/5e5aac2444f406ba1f796ceff6887fc3b1def247
/usr/share/package-licenses/strace/c25e42893e9414a57ab2948804b87f37b1ee8c1a
/usr/share/package-licenses/strace/d3cbcf91f3a68d195eb9a558d54fd07c55f4faea

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/strace-log-merge.1
/usr/share/man/man1/strace.1
