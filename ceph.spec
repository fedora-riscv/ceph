#################################################################################
# common
#################################################################################
Name:		ceph
Version:	0.80.5
Release:	11%{?dist}
Epoch:		1
Summary:	Virtual package that allows clean ceph update path for all epel users
License:	GPLv2
Group:		System Environment/Base
URL:		http://ceph.com/
Obsoletes:	ceph-common < 1:0.80.5-10
Obsoletes:	ceph-devel < 1:0.80.5-10
Obsoletes:	ceph-fuse < 1:0.80.5-10
Obsoletes:	ceph-libs-compat < 1:0.80.5-10
Obsoletes:	ceph-radosgw < 1:0.80.5-10
Obsoletes:	ceph-test < 1:0.80.5-10
Obsoletes:	cephfs-java < 1:0.80.5-10
Obsoletes:	libcephfs1 < 1:0.80.5-10
Obsoletes:	libcephfs_jni1 < 1:0.80.5-10
Obsoletes:	librados2 < 1:0.80.5-10
Obsoletes:	librbd1 < 1:0.80.5-10
Obsoletes:	python-ceph < 1:0.80.5-10
Obsoletes:	rbd-fuse < 1:0.80.5-10
Obsoletes:	rest-bench < 1:0.80.5-10
Obsoletes:	ceph-debuginfo < 1:0.80.5-10
Obsoletes:	ceph-libcephfs < 1:0.80.5-10
Obsoletes:	ceph-libs < 1:0.80.5-10

%description
This is an empty virtual package. The sole purpose of this package
is to allow clean update of Ceph distributed object store.

%prep

%build

%install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


#################################################################################
# files
#################################################################################
%files

%changelog
* Mon Jan 19 2015 Boris Ranto <branto@redhat.com> - 1:0.80.5-11
- Fix a typo libcephfs1_jni1 -> libcephfs_jni1
- Obsolete ceph-libs and ceph-libcephfs

* Fri Jan 16 2015 Boris Ranto <branto@redhat.com> - 1:0.80.5-10
- Deprecate the package -- the client part of the package will be provided

* Wed Jan 14 2015 Boris Ranto <branto@redhat.com> - 1:0.80.7-3
- Fix rhbz#1155335 -- /usr/bin/ceph hangs indefinitely

* Mon Dec 8 2014 Boris Ranto <branto@redhat.com> - 1:0.80.7-2
- Fix rhbz#1144794

* Thu Oct 16 2014 Boris Ranto <branto@redhat.com> - 1:0.80.7-1
- Rebase to latest upstream version

* Sat Oct 11 2014 Boris Ranto <branto@redhat.com> - 1:0.80.6-3
- Fix a typo in librados-devel vs librados2-devel dependency

* Fri Oct 10 2014 Boris Ranto <branto@redhat.com> - 1:0.80.6-2
- Provide empty file list for python-ceph-compat and ceph-devel-compat

* Fri Oct 10 2014 Boris Ranto <branto@redhat.com> - 1:0.80.6-1
- Rebase to 0.80.6
- Split ceph-devel and python-ceph packages

* Tue Sep 9 2014 Dan Horák <dan[at]danny.cz> - 1:0.80.5-10
- update Requires for s390(x)

* Wed Sep 3 2014 Boris Ranto <branto@redhat.com> - 1:0.80.5-9
- Symlink librd.so.1 to /usr/lib64/qemu only on rhel6+ x86_64 (1136811)

* Thu Aug 21 2014 Boris Ranto <branto@redhat.com> - 1:0.80.5-8
- Revert the previous change
- Fix bz 1118504, second attempt (yasm appears to be the package that caused this

* Wed Aug 20 2014 Boris Ranto <branto@redhat.com> - 1:0.80.5-7
- Several more merges from file to try to fix the selinux issue (1118504)

* Sun Aug 17 2014 Kalev Lember <kalevlember@gmail.com> - 1:0.80.5-6
- Obsolete ceph-libcephfs

* Sat Aug 16 2014 Boris Ranto <branto@redhat.com> - 1:0.80.5-5
- Do not require xfsprogs/xfsprogs-devel for el6
- Require gperftools-devel for non-ppc*/s390* architectures only
- Do not require junit -- no need to build libcephfs-test.jar
- Build without libxfs for el6
- Build without tcmalloc for ppc*/s390* architectures
- Location of mkcephfs must depend on a rhel release
- Use epoch in the Requires fields [1130700]

* Sat Aug 16 2014 Boris Ranto <branto@redhat.com> - 1:0.80.5-4
- Use the proper version name in Obsoletes

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.80.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Boris Ranto <branto@redhat.com> - 1:0.80.5-2
- Add the arm pthread hack

* Fri Aug 15 2014 Boris Ranto <branto@redhat.com> - 1:0.80.5-1
- Bump the Epoch, we need to keep the latest stable, not development, ceph version in fedora
- Use the upstream spec file with the ceph-libs split
- Add libs-compat subpackage [1116546]
- use fedora in rhel 7 checks
- obsolete libcephfs [1116614]
- depend on redhat-lsb-core for the initscript [1108696]

* Wed Aug 13 2014 Kalev Lember <kalevlember@gmail.com> - 0.81.0-6
- Add obsoletes to keep the upgrade path working (#1118510)

* Mon Jul 7 2014 Kaleb S. KEITHLEY <kkeithle[at]redhat.com> - 0.81.0-5
- revert to old spec until after f21 branch

* Fri Jul 4 2014 Kaleb S. KEITHLEY <kkeithle[at]redhat.com>
- temporary exclude f21/armv7hl. N.B. it builds fine on f20/armv7hl.

* Fri Jul 4 2014 Kaleb S. KEITHLEY <kkeithle[at]redhat.com> - 0.81.0-4
- upstream ceph.spec file

* Tue Jul 1 2014 Kaleb S. KEITHLEY <kkeithle[at]redhat.com> - 0.81.0-3
- upstream ceph.spec file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.81.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 5 2014 Kaleb S. KEITHLEY <kkeithle[at]redhat.com>
- el6 ppc64 likewise for tcmalloc, merge from origin/el6

* Thu Jun 5 2014 Kaleb S. KEITHLEY <kkeithle[at]redhat.com>
- el6 ppc64 does not have gperftools, merge from origin/el6

* Thu Jun 5 2014 Kaleb S. KEITHLEY <kkeithle[at]redhat.com> - 0.81.0-1
- ceph-0.81.0

* Wed Jun  4 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.80.1-5
- gperftools now available on aarch64/ppc64

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.80.1-4
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.80.1-3
- rebuild for boost 1.55.0

* Wed May 14 2014 Kaleb S. KEITHLEY <kkeithle[at]redhat.com> - 0.80.1-2
- build epel-6
- exclude %%{_libdir}/ceph/erasure-code in base package

* Tue May 13 2014 Kaleb S. KEITHLEY <kkeithle[at]redhat.com> - 0.80.1-1
- Update to latest stable upstream release, BZ 1095201
- PIE, _hardened_build, BZ 955174

* Thu Feb 06 2014 Ken Dreyer <ken.dreyer@inktank.com> - 0.72.2-2
- Move plugins from -devel into -libs package (#891993). Thanks Michael
  Schwendt.

* Mon Jan 06 2014 Ken Dreyer <ken.dreyer@inktank.com> 0.72.2-1
- Update to latest stable upstream release
- Use HTTPS for URLs
- Submit Automake 1.12 patch upstream
- Move unversioned shared libs from ceph-libs into ceph-devel

* Wed Dec 18 2013 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> 0.67.3-4
- build without tcmalloc on aarch64 (no gperftools)

* Sat Nov 30 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.67.3-3
- gperftools not currently available on aarch64

* Mon Oct 07 2013 Dan Horák <dan[at]danny.cz> - 0.67.3-2
- fix build on non-x86_64 64-bit arches

* Wed Sep 11 2013 Josef Bacik <josef@toxicpanda.com> - 0.67.3-1
- update to 0.67.3

* Wed Sep 11 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.61.7-3
- let base package include all its documentation files via %%doc magic,
  so for Fedora 20 Unversioned Docdirs no files are included accidentally
- include the sample config files again (instead of just an empty docdir
  that has been added for #846735)
- don't include librbd.so.1 also in -devel package (#1003202)
- move one misplaced rados plugin from -devel into -libs package (#891993)
- include missing directories in -devel and -libs packages
- move librados-config into the -devel pkg where its manual page is, too
- add %%_isa to subpackage dependencies
- don't use %%defattr anymore
- add V=1 to make invocation for verbose build output

* Wed Jul 31 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.61.7-2
- re-enable tmalloc on arm now gperftools is fixed

* Mon Jul 29 2013 Josef Bacik <josef@toxicpanda.com> - 0.61.7-1
- Update to 0.61.7

* Sat Jul 27 2013 pmachata@redhat.com - 0.56.4-2
- Rebuild for boost 1.54.0

* Fri Mar 29 2013 Josef Bacik <josef@toxicpanda.com> - 0.56.4-1
- Update to 0.56.4
- Add upstream d02340d90c9d30d44c962bea7171db3fe3bfba8e to fix logrotate

* Wed Feb 20 2013 Josef Bacik <josef@toxicpanda.com> - 0.56.3-1
- Update to 0.56.3

* Mon Feb 11 2013 Richard W.M. Jones <rjones@redhat.com> - 0.53-2
- Rebuilt to try to fix boost dependency problem in Rawhide.

* Thu Nov  1 2012 Josef Bacik <josef@toxicpanda.com> - 0.53-1
- Update to 0.53

* Mon Sep 24 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.51-3
- Fix automake 1.12 error
- Rebuild after buildroot was messed up

* Tue Sep 18 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.51-2
- Use system leveldb

* Fri Sep 07 2012 David Nalley <david@gnsa.us> - 0.51-1
- Updating to 0.51
- Updated url and source url. 

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  9 2012 Josef Bacik <josef@toxicpanda.com> - 0.46-1
- updated to upstream 0.46
- broke out libcephfs (rhbz# 812975)

* Mon Apr 23 2012 Dan Horák <dan[at]danny.cz> - 0.45-2
- fix detection of C++11 atomic header

* Thu Apr 12 2012 Josef Bacik <josef@toxicpanda.com> - 0.45-1
- updating to upstream 0.45

* Wed Apr  4 2012 Niels de Vos <devos@fedoraproject.org> - 0.44-5
- Add LDFLAGS=-lpthread on any ARM architecture
- Add CFLAGS=-DAO_USE_PTHREAD_DEFS on ARMv5tel

* Mon Mar 26 2012 Dan Horák <dan[at]danny.cz> 0.44-4
- gperftools not available also on ppc

* Mon Mar 26 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.44-3
- Remove unneeded patch

* Sun Mar 25 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.44-2
- Update to 0.44
- Fix build problems

* Mon Mar  5 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.43-1
- Update to 0.43
- Remove upstreamed compile fixes patch
- Remove obsoleted dump_pop patch

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-2
- Rebuilt for c++ ABI breakage

* Thu Feb 16 2012 Tom Callaway <spot@fedoraproject.org> 0.41-1
- update to 0.41
- fix issues preventing build
- rebuild against gperftools

* Sat Dec 03 2011 David Nalley <david@gnsa.us> 0.38-1
- updating to upstream 0.39

* Sat Nov 05 2011 David Nalley <david@gnsa.us> 0.37-1
- create /etc/ceph - bug 745462
- upgrading to 0.37, fixing 745460, 691033
- fixing various logrotate bugs 748930, 747101

* Fri Aug 19 2011 Dan Horák <dan[at]danny.cz> 0.31-4
- google-perftools not available also on s390(x)

* Mon Jul 25 2011 Karsten Hopp <karsten@redhat.com> 0.31-3
- build without tcmalloc on ppc64, BR google-perftools is not available there

* Tue Jul 12 2011 Josef Bacik <josef@toxicpanda.com> 0.31-2
- Remove curl/types.h include since we don't use it anymore

* Tue Jul 12 2011 Josef Bacik <josef@toxicpanda.com> 0.31-1
- Update to 0.31

* Tue Apr  5 2011 Josef Bacik <josef@toxicpanda.com> 0.26-2
- Add the compile fix patch

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

* Fri Apr 30 2010 Josef Bacik <josef@toxicpanda.com> 0.19.1-4
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
