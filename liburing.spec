#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v10
# autospec commit: 5905be9
#
Name     : liburing
Version  : 2.6
Release  : 9
URL      : https://github.com/axboe/liburing/archive/liburing-2.6/liburing-2.6.tar.gz
Source0  : https://github.com/axboe/liburing/archive/liburing-2.6/liburing-2.6.tar.gz
Summary  : Linux-native io_uring I/O access library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 MIT
Requires: liburing-lib = %{version}-%{release}
Requires: liburing-license = %{version}-%{release}
Requires: liburing-man = %{version}-%{release}
BuildRequires : buildreq-configure
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Warn-for-unknown-configure-options.patch

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
%setup -q -n liburing-liburing-2.6
cd %{_builddir}/liburing-liburing-2.6
%patch -P 1 -p1
pushd ..
cp -a liburing-liburing-2.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1714517874
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --libdevdir=/usr/lib64
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --libdevdir=/usr/lib64
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1714517874
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/liburing
cp %{_builddir}/liburing-liburing-%{version}/COPYING %{buildroot}/usr/share/package-licenses/liburing/3704f4680301a60004b20f94e0b5b8c7ff1484a9 || :
cp %{_builddir}/liburing-liburing-%{version}/COPYING.GPL %{buildroot}/usr/share/package-licenses/liburing/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/liburing-liburing-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/liburing/7ec9728069d1205c985a64e2cf19496a45206bb1 || :
cp %{_builddir}/liburing-liburing-%{version}/debian/copyright %{buildroot}/usr/share/package-licenses/liburing/804982ee6d3905270c9dd405d4ee811ffc8ab902 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/liburing.h
/usr/include/liburing/barrier.h
/usr/include/liburing/compat.h
/usr/include/liburing/io_uring.h
/usr/include/liburing/io_uring_version.h
/usr/lib64/liburing-ffi.so
/usr/lib64/liburing.so
/usr/lib64/pkgconfig/liburing-ffi.pc
/usr/lib64/pkgconfig/liburing.pc
/usr/share/man/man2/io_uring_enter.2
/usr/share/man/man2/io_uring_enter2.2
/usr/share/man/man2/io_uring_register.2
/usr/share/man/man2/io_uring_setup.2
/usr/share/man/man3/IO_URING_CHECK_VERSION.3
/usr/share/man/man3/IO_URING_VERSION_MAJOR.3
/usr/share/man/man3/IO_URING_VERSION_MINOR.3
/usr/share/man/man3/__io_uring_buf_ring_cq_advance.3
/usr/share/man/man3/io_uring_buf_ring_add.3
/usr/share/man/man3/io_uring_buf_ring_advance.3
/usr/share/man/man3/io_uring_buf_ring_available.3
/usr/share/man/man3/io_uring_buf_ring_cq_advance.3
/usr/share/man/man3/io_uring_buf_ring_init.3
/usr/share/man/man3/io_uring_buf_ring_mask.3
/usr/share/man/man3/io_uring_check_version.3
/usr/share/man/man3/io_uring_close_ring_fd.3
/usr/share/man/man3/io_uring_cq_advance.3
/usr/share/man/man3/io_uring_cq_has_overflow.3
/usr/share/man/man3/io_uring_cq_ready.3
/usr/share/man/man3/io_uring_cqe_get_data.3
/usr/share/man/man3/io_uring_cqe_get_data64.3
/usr/share/man/man3/io_uring_cqe_seen.3
/usr/share/man/man3/io_uring_for_each_cqe.3
/usr/share/man/man3/io_uring_free_buf_ring.3
/usr/share/man/man3/io_uring_free_probe.3
/usr/share/man/man3/io_uring_get_events.3
/usr/share/man/man3/io_uring_get_probe.3
/usr/share/man/man3/io_uring_get_sqe.3
/usr/share/man/man3/io_uring_major_version.3
/usr/share/man/man3/io_uring_minor_version.3
/usr/share/man/man3/io_uring_opcode_supported.3
/usr/share/man/man3/io_uring_peek_cqe.3
/usr/share/man/man3/io_uring_prep_accept.3
/usr/share/man/man3/io_uring_prep_accept_direct.3
/usr/share/man/man3/io_uring_prep_cancel.3
/usr/share/man/man3/io_uring_prep_cancel64.3
/usr/share/man/man3/io_uring_prep_cancel_fd.3
/usr/share/man/man3/io_uring_prep_close.3
/usr/share/man/man3/io_uring_prep_close_direct.3
/usr/share/man/man3/io_uring_prep_cmd.3
/usr/share/man/man3/io_uring_prep_connect.3
/usr/share/man/man3/io_uring_prep_fadvise.3
/usr/share/man/man3/io_uring_prep_fallocate.3
/usr/share/man/man3/io_uring_prep_fgetxattr.3
/usr/share/man/man3/io_uring_prep_files_update.3
/usr/share/man/man3/io_uring_prep_fixed_fd_install.3
/usr/share/man/man3/io_uring_prep_fsetxattr.3
/usr/share/man/man3/io_uring_prep_fsync.3
/usr/share/man/man3/io_uring_prep_ftruncate.3
/usr/share/man/man3/io_uring_prep_futex_wait.3
/usr/share/man/man3/io_uring_prep_futex_waitv.3
/usr/share/man/man3/io_uring_prep_futex_wake.3
/usr/share/man/man3/io_uring_prep_getxattr.3
/usr/share/man/man3/io_uring_prep_link.3
/usr/share/man/man3/io_uring_prep_link_timeout.3
/usr/share/man/man3/io_uring_prep_linkat.3
/usr/share/man/man3/io_uring_prep_madvise.3
/usr/share/man/man3/io_uring_prep_mkdir.3
/usr/share/man/man3/io_uring_prep_mkdirat.3
/usr/share/man/man3/io_uring_prep_msg_ring.3
/usr/share/man/man3/io_uring_prep_msg_ring_cqe_flags.3
/usr/share/man/man3/io_uring_prep_msg_ring_fd.3
/usr/share/man/man3/io_uring_prep_msg_ring_fd_alloc.3
/usr/share/man/man3/io_uring_prep_multishot_accept.3
/usr/share/man/man3/io_uring_prep_multishot_accept_direct.3
/usr/share/man/man3/io_uring_prep_nop.3
/usr/share/man/man3/io_uring_prep_openat.3
/usr/share/man/man3/io_uring_prep_openat2.3
/usr/share/man/man3/io_uring_prep_openat2_direct.3
/usr/share/man/man3/io_uring_prep_openat_direct.3
/usr/share/man/man3/io_uring_prep_poll_add.3
/usr/share/man/man3/io_uring_prep_poll_multishot.3
/usr/share/man/man3/io_uring_prep_poll_remove.3
/usr/share/man/man3/io_uring_prep_poll_update.3
/usr/share/man/man3/io_uring_prep_provide_buffers.3
/usr/share/man/man3/io_uring_prep_read.3
/usr/share/man/man3/io_uring_prep_read_fixed.3
/usr/share/man/man3/io_uring_prep_read_multishot.3
/usr/share/man/man3/io_uring_prep_readv.3
/usr/share/man/man3/io_uring_prep_readv2.3
/usr/share/man/man3/io_uring_prep_recv.3
/usr/share/man/man3/io_uring_prep_recv_multishot.3
/usr/share/man/man3/io_uring_prep_recvmsg.3
/usr/share/man/man3/io_uring_prep_recvmsg_multishot.3
/usr/share/man/man3/io_uring_prep_remove_buffers.3
/usr/share/man/man3/io_uring_prep_rename.3
/usr/share/man/man3/io_uring_prep_renameat.3
/usr/share/man/man3/io_uring_prep_send.3
/usr/share/man/man3/io_uring_prep_send_set_addr.3
/usr/share/man/man3/io_uring_prep_send_zc.3
/usr/share/man/man3/io_uring_prep_send_zc_fixed.3
/usr/share/man/man3/io_uring_prep_sendmsg.3
/usr/share/man/man3/io_uring_prep_sendmsg_zc.3
/usr/share/man/man3/io_uring_prep_sendto.3
/usr/share/man/man3/io_uring_prep_setxattr.3
/usr/share/man/man3/io_uring_prep_shutdown.3
/usr/share/man/man3/io_uring_prep_socket.3
/usr/share/man/man3/io_uring_prep_socket_direct.3
/usr/share/man/man3/io_uring_prep_socket_direct_alloc.3
/usr/share/man/man3/io_uring_prep_splice.3
/usr/share/man/man3/io_uring_prep_statx.3
/usr/share/man/man3/io_uring_prep_symlink.3
/usr/share/man/man3/io_uring_prep_symlinkat.3
/usr/share/man/man3/io_uring_prep_sync_file_range.3
/usr/share/man/man3/io_uring_prep_tee.3
/usr/share/man/man3/io_uring_prep_timeout.3
/usr/share/man/man3/io_uring_prep_timeout_remove.3
/usr/share/man/man3/io_uring_prep_timeout_update.3
/usr/share/man/man3/io_uring_prep_unlink.3
/usr/share/man/man3/io_uring_prep_unlinkat.3
/usr/share/man/man3/io_uring_prep_waitid.3
/usr/share/man/man3/io_uring_prep_write.3
/usr/share/man/man3/io_uring_prep_write_fixed.3
/usr/share/man/man3/io_uring_prep_writev.3
/usr/share/man/man3/io_uring_prep_writev2.3
/usr/share/man/man3/io_uring_queue_exit.3
/usr/share/man/man3/io_uring_queue_init.3
/usr/share/man/man3/io_uring_queue_init_mem.3
/usr/share/man/man3/io_uring_queue_init_params.3
/usr/share/man/man3/io_uring_recvmsg_cmsg_firsthdr.3
/usr/share/man/man3/io_uring_recvmsg_cmsg_nexthdr.3
/usr/share/man/man3/io_uring_recvmsg_name.3
/usr/share/man/man3/io_uring_recvmsg_out.3
/usr/share/man/man3/io_uring_recvmsg_payload.3
/usr/share/man/man3/io_uring_recvmsg_payload_length.3
/usr/share/man/man3/io_uring_recvmsg_validate.3
/usr/share/man/man3/io_uring_register_buf_ring.3
/usr/share/man/man3/io_uring_register_buffers.3
/usr/share/man/man3/io_uring_register_buffers_sparse.3
/usr/share/man/man3/io_uring_register_buffers_tags.3
/usr/share/man/man3/io_uring_register_buffers_update_tag.3
/usr/share/man/man3/io_uring_register_eventfd.3
/usr/share/man/man3/io_uring_register_eventfd_async.3
/usr/share/man/man3/io_uring_register_file_alloc_range.3
/usr/share/man/man3/io_uring_register_files.3
/usr/share/man/man3/io_uring_register_files_sparse.3
/usr/share/man/man3/io_uring_register_files_tags.3
/usr/share/man/man3/io_uring_register_files_update.3
/usr/share/man/man3/io_uring_register_files_update_tag.3
/usr/share/man/man3/io_uring_register_iowq_aff.3
/usr/share/man/man3/io_uring_register_iowq_max_workers.3
/usr/share/man/man3/io_uring_register_napi.3
/usr/share/man/man3/io_uring_register_ring_fd.3
/usr/share/man/man3/io_uring_register_sync_cancel.3
/usr/share/man/man3/io_uring_setup_buf_ring.3
/usr/share/man/man3/io_uring_sq_ready.3
/usr/share/man/man3/io_uring_sq_space_left.3
/usr/share/man/man3/io_uring_sqe_set_data.3
/usr/share/man/man3/io_uring_sqe_set_data64.3
/usr/share/man/man3/io_uring_sqe_set_flags.3
/usr/share/man/man3/io_uring_sqring_wait.3
/usr/share/man/man3/io_uring_submit.3
/usr/share/man/man3/io_uring_submit_and_get_events.3
/usr/share/man/man3/io_uring_submit_and_wait.3
/usr/share/man/man3/io_uring_submit_and_wait_timeout.3
/usr/share/man/man3/io_uring_unregister_buf_ring.3
/usr/share/man/man3/io_uring_unregister_buffers.3
/usr/share/man/man3/io_uring_unregister_eventfd.3
/usr/share/man/man3/io_uring_unregister_files.3
/usr/share/man/man3/io_uring_unregister_iowq_aff.3
/usr/share/man/man3/io_uring_unregister_napi.3
/usr/share/man/man3/io_uring_unregister_ring_fd.3
/usr/share/man/man3/io_uring_wait_cqe.3
/usr/share/man/man3/io_uring_wait_cqe_nr.3
/usr/share/man/man3/io_uring_wait_cqe_timeout.3
/usr/share/man/man3/io_uring_wait_cqes.3

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/liburing-ffi.so.2.6
/V3/usr/lib64/liburing.so.2.6
/usr/lib64/liburing-ffi.so.2
/usr/lib64/liburing-ffi.so.2.6
/usr/lib64/liburing.so.2
/usr/lib64/liburing.so.2.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/liburing/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/liburing/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/liburing/7ec9728069d1205c985a64e2cf19496a45206bb1
/usr/share/package-licenses/liburing/804982ee6d3905270c9dd405d4ee811ffc8ab902

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man7/io_uring.7
