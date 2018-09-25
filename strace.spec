#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA8041FA839E16E36 (ldv@altlinux.org)
#
Name     : strace
Version  : 4.24
Release  : 33
URL      : https://github.com/strace/strace/releases/download/v4.24/strace-4.24.tar.xz
Source0  : https://github.com/strace/strace/releases/download/v4.24/strace-4.24.tar.xz
Source99 : https://github.com/strace/strace/releases/download/v4.24/strace-4.24.tar.xz.asc
Summary  : Tracks and displays system calls associated with a running process
Group    : Development/Tools
License  : BSD-3-Clause
Requires: strace-bin = %{version}-%{release}
Requires: strace-man = %{version}-%{release}
Requires: strace-license = %{version}-%{release}
Requires: strace-data = %{version}-%{release}
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
Requires: strace-data = %{version}-%{release}
Requires: strace-license = %{version}-%{release}
Requires: strace-man = %{version}-%{release}

%description bin
bin components for the strace package.


%package data
Summary: data components for the strace package.
Group: Data

%description data
data components for the strace package.


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
%setup -q -n strace-4.24
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537911580
%configure --disable-static --with-libunwind
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1537911580
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/strace
cp COPYING %{buildroot}/usr/share/package-licenses/strace/COPYING
cp debian/copyright %{buildroot}/usr/share/package-licenses/strace/debian_copyright
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/strace
/usr/bin/strace-graph
/usr/bin/strace-log-merge

%files data
%defattr(-,root,root,-)
/usr/share/package-licenses/strace/debian_copyright

%files license
%defattr(-,root,root,-)
/usr/share/package-licenses/strace/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/strace-log-merge.1
/usr/share/man/man1/strace.1
