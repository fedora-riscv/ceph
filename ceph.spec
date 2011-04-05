Name:          ceph
Version:       0.26
Release:       1%{?dist}
Summary:       User space components of the Ceph file system
License:       LGPLv2
Group:         System Environment/Base
URL:           http://ceph.newdream.net/

Source:        http://ceph.newdream.net/download/%{name}-%{version}.tar.gz
Patch0:        ceph-init-fix.patch
Patch1:        ceph-fix-compile-error.patch
BuildRequires: fuse-devel, libtool, libtool-ltdl-devel, boost-devel, 
BuildRequires: libedit-devel, fuse-devel, git, perl, gdbm,
BuildRequires: cryptopp-devel, libatomic_ops-devel, google-perftools-devel
BuildRequires: pkgconfig, libcurl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires(post): chkconfig, binutils, libedit, google-perftools
Requires(preun): chkconfig
Requires(preun): initscripts

%description
Ceph is a distributed network file system designed to provide excellent
performance, reliability, and scalability.

%package       fuse
Summary:       Ceph fuse-based client
Group:         System Environment/Base
Requires:      %{name} = %{version}-%{release}
BuildRequires: fuse-devel
%description   fuse
FUSE based client for Ceph distributed network file system

%package     devel
Summary:     Ceph headers
Group:       Development/Libraries
License:     LGPLv2
Requires:    %{name} = %{version}-%{release}
%description devel
This package contains the headers needed to develop programs that use Ceph.

%package radosgw
Summary:        rados REST gateway
Group:          Development/Libraries
Requires:       mod_fcgid
BuildRequires:  fcgi-devel
BuildRequires:  expat-devel

%description radosgw
radosgw is an S3 HTTP REST gateway for the RADOS object store. It is
implemented as a FastCGI module using libfcgi, and can be used in
conjunction with any FastCGI capable web server.

%package gcephtool
Summary:        Ceph graphical monitoring tool
Group:          System Environment/Base
License:        LGPLv2
Requires:       gtk2 gtkmm24
BuildRequires:  gtk2-devel gtkmm24-devel

%description gcephtool
gcephtool is a graphical monitor for the clusters running the Ceph distributed
file system.

%prep
%setup -q
%patch0 -p1 -b .init
%patch1 -p1 -b .compile

%build
./autogen.sh
%{configure} --prefix=/usr --sbindir=/sbin \
--localstatedir=/var --sysconfdir=/etc \
--without-hadoop --with-radosgw --with-gtk2 
make CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'
install -D src/init-ceph $RPM_BUILD_ROOT%{_initrddir}/ceph
chmod 0644 $RPM_BUILD_ROOT%{_docdir}/ceph/sample.ceph.conf
install -m 0644 -D src/logrotate.conf $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/ceph
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/ceph/tmp/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/ceph/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/ceph/stat

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/chkconfig --add ceph

%preun
if [ $1 = 0 ] ; then
    /sbin/service ceph stop >/dev/null 2>&1
    /sbin/chkconfig --del ceph
fi

%postun
/sbin/ldconfig
if [ "$1" -ge "1" ] ; then
    /sbin/service ceph condrestart >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_bindir}/ceph
%{_bindir}/cephfs
%{_bindir}/cconf
%{_bindir}/cclass
%{_bindir}/cclsinfo
%{_bindir}/crushtool
%{_bindir}/monmaptool
%{_bindir}/osdmaptool
%{_bindir}/cauthtool
%{_bindir}/csyn
%{_bindir}/crun
%{_bindir}/cmon
%{_bindir}/cmds
%{_bindir}/cosd
%{_bindir}/crbdnamer
%{_bindir}/librados-config
%{_bindir}/rados
%{_bindir}/rbd
%{_bindir}/cdebugpack
%{_initrddir}/ceph
%{_libdir}/libceph.so.*
%{_libdir}/libcrush.so.*
%{_libdir}/librados.so.*
%{_libdir}/librbd.so.*
%{_libdir}/rados-classes/libcls_rbd.so.*
/sbin/mkcephfs
/sbin/mount.ceph
%{_libdir}/ceph
%{_docdir}/ceph/sample.ceph.conf
%{_docdir}/ceph/sample.fetch_config
%config(noreplace) %{_sysconfdir}/logrotate.d/ceph
%{_mandir}/man8/cmon.8*
%{_mandir}/man8/cmds.8*
%{_mandir}/man8/cosd.8*
%{_mandir}/man8/mkcephfs.8*
%{_mandir}/man8/crun.8*
%{_mandir}/man8/csyn.8*
%{_mandir}/man8/crushtool.8*
%{_mandir}/man8/osdmaptool.8*
%{_mandir}/man8/monmaptool.8*
%{_mandir}/man8/cconf.8*
%{_mandir}/man8/ceph.8*
%{_mandir}/man8/cephfs.8*
%{_mandir}/man8/mount.ceph.8*
%{_mandir}/man8/radosgw.8*
%{_mandir}/man8/radosgw_admin.8*
%{_mandir}/man8/rados.8*
%{_mandir}/man8/rbd.8*
%{_mandir}/man8/cauthtool.8*
%{_mandir}/man8/cdebugpack.8*
%{_mandir}/man8/cclass.8.gz
%{_mandir}/man8/cclsinfo.8.gz
%{python_sitelib}/rados.py
%{python_sitelib}/rados.pyc
%{python_sitelib}/rados.pyo
%dir %{_localstatedir}/lib/ceph/
%dir %{_localstatedir}/lib/ceph/tmp/
%dir %{_localstatedir}/log/ceph/

%files fuse
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/cfuse
%{_mandir}/man8/cfuse.8*

%files devel
%defattr(-,root,root,-)
%doc COPYING
%{_includedir}/ceph/libceph.h
%{_includedir}/crush/crush.h
%{_includedir}/crush/hash.h
%{_includedir}/crush/mapper.h
%{_includedir}/crush/types.h
%{_includedir}/rados/librados.h
%{_includedir}/rados/librados.hpp
%{_includedir}/rados/buffer.h
%{_includedir}/rados/atomic.h
%{_includedir}/rados/page.h
%{_includedir}/rados/crc32c.h
%{_includedir}/rados/Spinlock.h
%{_includedir}/rados/assert.h
%{_includedir}/rbd/librbd.h
%{_includedir}/rbd/librbd.hpp
%{_libdir}/libceph.so
%{_libdir}/libcrush.so
%{_libdir}/librados.so
%{_libdir}/librbd.so*
%{_libdir}/rados-classes/libcls_rbd.so

%files gcephtool
%defattr(-,root,root,-)
%{_bindir}/gceph
%{_datadir}/ceph_tool/gui_resources/*

%files radosgw
%defattr(-,root,root,-)
%{_bindir}/radosgw
%{_bindir}/radosgw_admin

%changelog
* Tue Apr  5 2011 Josef Bacik <josef@toxicpanda.com> 0.26
- Update to 0.26

* Tue Mar 22 2011 Josef Bacik <josef@toxicpanda.com> 0.25.1-1
- Update to 0.25.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 Steven Pritchard <steve@kspei.com> 0.21.3-1
- Update to 0.21.3.

* Mon Aug 30 2010 Steven Pritchard <steve@kspei.com> 0.21.2-1
- Update to 0.21.2.

* Thu Aug 26 2010 Steven Pritchard <steve@kspei.com> 0.21.1-1
- Update to 0.21.1.
- Sample configs moved to /usr/share/doc/ceph/.
- Added cclass, rbd, and cclsinfo.
- Dropped mkmonfs and rbdtool.
- mkcephfs moved to /sbin.
- Add libcls_rbd.so.

* Tue Jul  6 2010 Josef Bacik <josef@toxicpanda.com> 0.20.2-1
- update to 0.20.2

* Wed May  5 2010 Josef Bacik <josef@toxicpanda.com> 0.20-1
- update to 0.20
- disable hadoop building
- remove all the test binaries properly

* Fri Apr 30 2010 Sage Weil <sage@newdream.net> 0.19.1-5
- Remove java deps (no need to build hadoop by default)
- Include all required librados helpers
- Include fetch_config sample
- Include rbdtool
- Remove misc debugging, test binaries

* Thu Apr 30 2010 Josef Bacik <josef@toxicpanda.com> 0.19.1-4
- Add java-devel and java tricks to get hadoop to build

* Mon Apr 26 2010 Josef Bacik <josef@toxicpanda.com> 0.19.1-3
- Move the rados and cauthtool man pages into the base package

* Sun Apr 25 2010 Jonathan Dieter <jdieter@lesbg.com> 0.19.1-2
- Add missing libhadoopcephfs.so* to file list
- Add COPYING to all subpackages
- Fix ownership of /usr/lib[64]/ceph
- Enhance description of fuse client

* Tue Apr 20 2010 Josef Bacik <josef@toxicpanda.com> 0.19.1-1
- Update to 0.19.1

* Mon Feb  8 2010 Josef Bacik <josef@toxicpanda.com> 0.18-1
- Initial spec file creation, based on the template provided in the ceph src
