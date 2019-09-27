#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA8041FA839E16E36 (ldv@altlinux.org)
#
Name     : strace
Version  : 5.3
Release  : 40
URL      : https://github.com/strace/strace/releases/download/v5.3/strace-5.3.tar.xz
Source0  : https://github.com/strace/strace/releases/download/v5.3/strace-5.3.tar.xz
Source1 : https://github.com/strace/strace/releases/download/v5.3/strace-5.3.tar.xz.asc
Summary  : A diagnostic, debugging and instructional userspace tracer
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.1 LGPL-2.1+
Requires: strace-bin = %{version}-%{release}
Requires: strace-license = %{version}-%{release}
Requires: strace-man = %{version}-%{release}
BuildRequires : btrfs-progs-dev
BuildRequires : libunwind-dev
BuildRequires : valgrind
Patch1: show_path.patch

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
%setup -q -n strace-5.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569616896
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --with-libunwind
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1569616896
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/strace
cp COPYING %{buildroot}/usr/share/package-licenses/strace/COPYING
cp tests-m32/COPYING %{buildroot}/usr/share/package-licenses/strace/tests-m32_COPYING
cp tests-mx32/COPYING %{buildroot}/usr/share/package-licenses/strace/tests-mx32_COPYING
cp tests/COPYING %{buildroot}/usr/share/package-licenses/strace/tests_COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/strace

%files extras
%defattr(-,root,root,-)
/usr/bin/strace-graph
/usr/bin/strace-log-merge

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/strace/COPYING
/usr/share/package-licenses/strace/tests-m32_COPYING
/usr/share/package-licenses/strace/tests-mx32_COPYING
/usr/share/package-licenses/strace/tests_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/strace-log-merge.1
/usr/share/man/man1/strace.1
