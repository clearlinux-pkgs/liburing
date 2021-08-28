#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : liburing
Version  : 2.0
Release  : 2
URL      : https://github.com/axboe/liburing/archive/liburing-2.0/liburing-2.0.tar.gz
Source0  : https://github.com/axboe/liburing/archive/liburing-2.0/liburing-2.0.tar.gz
Summary  : Linux-native io_uring I/O access library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 MIT
Requires: liburing-lib = %{version}-%{release}
Requires: liburing-license = %{version}-%{release}
Requires: liburing-man = %{version}-%{release}
Patch1: 0001-Warn-for-unknown-configure-options.patch
Patch2: 0002-examples-ucontext-cp.c-cope-with-variable-SIGSTKSZ.patch

%description
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%package dev
Summary: dev components for the liburing package.
Group: Development
Requires: liburing-lib = %{version}-%{release}
Provides: liburing-devel = %{version}-%{release}
Requires: liburing = %{version}-%{release}

%description dev
dev components for the liburing package.


%package lib
Summary: lib components for the liburing package.
Group: Libraries
Requires: liburing-license = %{version}-%{release}

%description lib
lib components for the liburing package.


%package license
Summary: license components for the liburing package.
Group: Default

%description license
license components for the liburing package.


%package man
Summary: man components for the liburing package.
Group: Default

%description man
man components for the liburing package.


%prep
%setup -q -n liburing-liburing-2.0
cd %{_builddir}/liburing-liburing-2.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630112657
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --libdevdir=/usr/lib64
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1630112657
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/liburing
cp %{_builddir}/liburing-liburing-2.0/COPYING %{buildroot}/usr/share/package-licenses/liburing/3704f4680301a60004b20f94e0b5b8c7ff1484a9
cp %{_builddir}/liburing-liburing-2.0/COPYING.GPL %{buildroot}/usr/share/package-licenses/liburing/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/liburing-liburing-2.0/LICENSE %{buildroot}/usr/share/package-licenses/liburing/36710809dd93101a87fab97bd7e5e34d7bd3615e
cp %{_builddir}/liburing-liburing-2.0/debian/copyright %{buildroot}/usr/share/package-licenses/liburing/804982ee6d3905270c9dd405d4ee811ffc8ab902
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/liburing.h
/usr/include/liburing/barrier.h
/usr/include/liburing/compat.h
/usr/include/liburing/io_uring.h
/usr/lib64/liburing.so
/usr/lib64/pkgconfig/liburing.pc
/usr/share/man/man2/io_uring_enter.2
/usr/share/man/man2/io_uring_register.2
/usr/share/man/man2/io_uring_setup.2
/usr/share/man/man3/io_uring_get_sqe.3
/usr/share/man/man3/io_uring_queue_exit.3
/usr/share/man/man3/io_uring_queue_init.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/liburing.so.2
/usr/lib64/liburing.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/liburing/36710809dd93101a87fab97bd7e5e34d7bd3615e
/usr/share/package-licenses/liburing/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/liburing/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/liburing/804982ee6d3905270c9dd405d4ee811ffc8ab902

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man7/io_uring.7
