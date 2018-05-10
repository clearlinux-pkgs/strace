#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA8041FA839E16E36 (ldv@altlinux.org)
#
Name     : strace
Version  : 4.21
Release  : 31
URL      : https://sourceforge.net/projects/strace/files/strace/4.21/strace-4.21.tar.xz
Source0  : https://sourceforge.net/projects/strace/files/strace/4.21/strace-4.21.tar.xz
Source99 : https://sourceforge.net/projects/strace/files/strace/4.21/strace-4.21.tar.xz.asc
Summary  : Tracks and displays system calls associated with a running process
Group    : Development/Tools
License  : BSD-3-Clause
Requires: strace-bin
Requires: strace-doc
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

%description bin
bin components for the strace package.


%package doc
Summary: doc components for the strace package.
Group: Documentation

%description doc
doc components for the strace package.


%prep
%setup -q -n strace-4.21
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518887326
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1518887326
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/strace
/usr/bin/strace-graph
/usr/bin/strace-log-merge

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
