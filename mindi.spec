#
# $Id: mindi.spec 1866 2008-01-16 15:29:04Z bruno $
#
Summary:	Mindi creates emergency boot disks/CDs using your kernel, tools and modules
Name:		mindi
Version:	2.1.1
Release:	%mkrel 1
License:	GPL
Group:		Archiving/Backup
Url:		http://www.mondorescue.org
Source:		ftp://ftp.mondorescue.org/src/%{name}-%{version}.tar.gz
# Not yet possible as busybox is a binary that should go alongside
# BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
Requires:	bzip2 >= 0.9, mkisofs, ncurses, binutils, gawk, dosfstools, mindi-busybox >= 1.7.3, parted, perl, mtools, which, grep >= 2.5
ExcludeArch:	ppc
 
# Not on all systems
#Conflicts:	bonnie++

%description
Mindi takes your kernel, modules, tools and libraries, and puts them on N
bootable disks (or 1 bootable CD image). You may then boot from the disks/CD
and do system maintenance - e.g. format partitions, backup/restore data,
verify packages, etc.

%prep
%setup -q

%build

%install
rm  -rf $RPM_BUILD_ROOT
export DONT_RELINK=1

export HEAD=${RPM_BUILD_ROOT}
export PREFIX=%{_exec_prefix}
export CONFDIR=%{_sysconfdir}
export MANDIR=%{_mandir}
#export DOCDIR=%{_docdir}
export LIBDIR=%{_libdir}
export CACHEDIR=%{_var}/cache/%{name}
export PKGBUILDMINDI="true"

./install.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}
%doc ChangeLog INSTALL COPYING README TODO README.* NEWS 
#svn.log
%{_mandir}/man8/*
%{_libdir}/%{name}
%{_sbindir}/*
%{_var}/cache/%{name}


%changelog
* Sun Feb 26 2012 Bruno Cornec <bcornec@mandriva.org> 2.1.1-1mdv2012.0
+ Revision: 780891
- Update to upstream 2.1.1

* Mon Mar 21 2011 Bruno Cornec <bcornec@mandriva.org> 2.0.7.6-1
+ Revision: 647364
- Update to upstream mindi 2.0.7.6

* Sat Feb 12 2011 Bruno Cornec <bcornec@mandriva.org> 2.0.7.5-1
+ Revision: 637407
-Update mindi to 2.0.7.5 upstream

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.7.3-2mdv2011.0
+ Revision: 612868
- the mass rebuild of 2010.1 packages

* Mon May 17 2010 Bruno Cornec <bcornec@mandriva.org> 2.0.7.3-1mdv2010.1
+ Revision: 544896
- Update mindi to upstream 2.0.7.3

* Fri Dec 04 2009 Bruno Cornec <bcornec@mandriva.org> 2.0.7.1-1mdv2010.1
+ Revision: 473303
- Update to upstream 2.0.7.1

* Wed Feb 18 2009 Bruno Cornec <bcornec@mandriva.org> 2.0.6-1mdv2009.1
+ Revision: 342523
- Updated to 2.0.6

* Mon Dec 08 2008 Bruno Cornec <bcornec@mandriva.org> 2.0.4-3mdv2009.1
+ Revision: 311742
- Updated to 2.0.4

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.24-3mdv2009.0
+ Revision: 252521
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.24-1mdv2008.1
+ Revision: 136579
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Bruno Cornec <bcornec@mandriva.org> 1.24-1mdv2008.0
+ Revision: 77280
- Fix better extra doc removal
- Remove extra doc files
- Updated to 1.2.4
- Support for swap with UUID on VMWare ESX 3 at least with dumpuuid (Bruno Cornec)
- Fix a problem in directory link handling in mindi seen on gentoo64 (Francesco Talamona/Bruno Cornec)
- Add README.proliant to document Virtual Media usage (Bruno Cornec)
- Add support for megaraid_sas (Daniel Hill/Bruno Cornec)
- No more acpi=off by default during restore (Bruno Cornec)
- /var/cache/mindi now useed by default for mindi images (Bruno Cornec)
- Add support for LSI SAS1064E (Brandon Poyner/Bruno Cornec)
- Fix a bug on the MODULE variable and grep -F usage with spaces. (Bruno Cornec)
- Fix Virtual media usage (Patrick Albert)
- Improve VMWare ESX support (Bruno Cornec)
- Fix a x86_64 bug (Bruno Cornec)
- MINDI_TMP now used in analyze-my-lvm (Bruno Cornec)
- Fx bugs for optimised libs (Debian, Centos/RHEL5) (Brandon Poyner/Andree Leidenfrost/Bruno Cornec)
- Remove a hack for x86_64 in spec file due to a RH bug (Bruno Cornec)
- Remove all support for mindi.conf for 2.2.x branch (Bruno Cornec)
- Gentoo support improvements (kernel, kbd, deps, ...) (Francesco Talamona/Bruno Cornec)
- parted is required by mindi (Francesco Talamona/Bruno Cornec)
- Add support for i2o (Fix #165) (Bruno Cornec)
- Now supports USB keyboard/mouse at restore time better (Bruno Cornec)
- Support for HP xw9300 NIC (forcedeth) added (Bruno Cornec)
- Improved log at restore time (Bruno Cornec)
- Add support for 3w-9xxx 3w_9xxx (Fix #163) (Bruno Cornec)
- Fix a bug where mondorestore.log was truncated (Bruno Cornec)
- Fix a Debian packaging bug for good (#142 and #126)
- Removes some now unnecessary commands concerning /root/images/mindi. (Andree Leidenfrost)
- Support of Debian optimised libraries in /lib/i686/cmov (Andree Leidenfrost)
- lsmod usage replaced by /proc/modules and a MODULES variable (Andree Leidenfrost/Bruno Cornec)
- Fix a fedora build bug for /etc/mindi (Bruno Cornec)

* Sat Apr 28 2007 Bruno Cornec <bcornec@mandriva.org> 1.23-1mdv2008.0
+ Revision: 19032
- Updated to 1.2.3
- FORCE_MODS variable to support additional modules at will (Bruno Cornec)
- Better log file content in mondoarchive.log from the copy of the mindi log (Bruno Cornec)
- Stricter POSIX compliance for mindi to allow usage with dash on Ubuntu (Fix for #154)

* Wed Apr 25 2007 Bruno Cornec <bcornec@mandriva.org> 1.22-1mdv2008.0
+ Revision: 18031
- Updated to 1.2.2
- Add support for new megaraid driver (HP NetServers with 2.6) (P.C.J.G.Brunier)
- Add support for adpahci (Proliant DL 140 G3 - SATA) (Abhijit Das/Bruno Cornec)
- Mindi log file is now added to mondoarchive log file to ease debug (Bruno Cornec)
- Suppress losetup usage in start-nfs (unreliable and doesn't work with QEMU (Bruno Cornec)
- Fix a bug where losetup is called with only one parameter (#140) (Bruno Cornec)
- Fix a bug on NFS in FC6 - fscache module needed (Bruno Cornec)
- Add build support for Mandriva 2007.1, RREL 5 and Debian 4.0 (Bruno Cornec)
- Fix a bug for FC6 where the boot disk size was again insufficient (Rene Ribaud/Bruno Cornec)
- On CentOS 4.4 mdrun isn't available anymore so init should use mdadm instead (Momtchil Momtchev/Bruno Cornec)
- Add support for raid456 driver (Mark Nienberg/Bruno Cornec)
- Add the DENY_MODS variable in mindi allowing to describes modules that you don't want to include as part of the restore boot environment (HP Open Call OCMP e.g; needs it) (Bruno Cornec)
- Add GetInitrdFilesystemToUse function to support initramfs type of initrd (SuSE 10.2/Debian 3.x/FC 6/...) (Andree Leidenfrost)
- Fix a bug for ia64 in kernel reference in elilo.conf (Andree Leidenfrost)
- Check that /boot/efi is mounted on ia64 (Andree Leidenfrost)
- Protect some rm -rf to avoid raw removals (Bruno Cornec)
- Better messages for analyze-my-lvm (Bruno Cornec)
- Add support for newer Qlogic drivers (qla2300 & 2400), mpt, dm and ohci (Josef Jetzinger/Bruno Cornec)
- Fix a bug in mindi for the FAILSAFE support (Scott Cummings)
- PATH fixed for init in restore (/usr/games added for petris) (Andree Leidenfrost)
- Fiw a bug where restore failing because no archive files are found when -G is used (Andree Leidenfrost)
- /media is now completely excluded as per StandardsCompliance (Bruno Cornec)


* Wed Aug 09 2006 bcornec
+ 08/09/06 22:29:59 (55214)
Version for the moment has to be changed to 1.09 for upgrade purposes.
Will be correct in 3.0.x. Dur to the history of stupid numbering

* Wed Aug 09 2006 bcornec
+ 08/09/06 11:29:13 (54687)
spec file adapted for %%{1}mdv2007.0

* Wed Aug 09 2006 bcornec
+ 08/09/06 09:34:46 (54660)
mindi now clean

* Wed Aug 09 2006 bcornec
+ 08/09/06 09:02:27 (54653)
import mindi-1.0.9-2.20060mdk

* Sat Aug 05 2006 Bruno Cornec <bcornec@mandriva.org> 1.0.9-2.20060mdk
- Updated to 1.0.9
- Fix for bug #22 RHEL4 + LVM + LABEL support (Bruno Cornec)
- Fix for bug #8 keyboard support incorrect (Bruno Cornec)
- New NFS/PXE support. start-nfs is now a fixed script. Allow more possibilities at restore time (Bruno Cornec)
- new global variables + Bug fixes for LVM (Bruno Cornec)
- SuSE RPMS now use bzip2 (Lars Rupp/Bruno Cornec)
- Fix a bug for filesystems with LABEL in fstab not mounted (Bruno Cornec)
- Qlogic 2300 and 2200 are now supported (Bruno Cornec)
- Use busybox 1.1.3 for net part (Bruno Cornec)
- Fix various screen corruption for 'Configure LVM' (Andree Leidenfrost)
- Fix Adaptec Zero-Channel RAID Cards support bug #6455 (Bruno Cornec)
- Fix a bug with redhat_label not initialized in the loop systematically
(Anthony P. Machon/Bruno Cornec)
- nfsmount option added to allow redeployment from another NFS server (Bruno Cornec)
- Replaced all occurrences of egrep with 'grep -E' and of fgrep with 'grep -F' (Andree Leidenfrost)
- Fix a bug in analyze-my-lvm for RHEL3 where vgdisplay prints an additional
field sometimes (#) (severine.lombardo_at_acoss.fr/Bruno Cornec)
- Deal properly with LVM tool lvmiopversion and with lvmcreate_initrd and pvdata - fixes Debian bug #351687 (Andree Leidenfrost)
- Handle the  /dev/mapper/<VG>-<LV> for LVM devices - fix for Debian bug #362926 (Andree Leidenfrost)

* Wed Jun 07 2006 Bruno Cornec <bcornec@mandriva.org> 1.0.8-3.20060mdk
- Updated to 1.0.8-3
- exec-shield removed for mindi (Bruno Cornec)
- Fix a bug for ia64 build in mindi where locallib was undefined (Bruno Cornec)
- Fix a bug for SuSE and Debian where $dfam was used in install.sh (Bruno Cornec)
- Make the init script mdadm-aware (Andree Leidenfrost)

* Fri Jun 02 2006 Bruno Cornec <bcornec@mandriva.org> 1.0.8-2.20060mdk
- Updated to 1.0.8-2
- Fix bugs in the swap+LABEL code found on rhel4 (Peter Naber/Bruno Cornec)
- PXE mode now supports change of NIC for redeployment (Bruno Cornec)

* Thu May 25 2006 Bruno Cornec <bcornec@mandriva.org> 1.0.8-1.20060mdk
- Updated to 1.0.8-1
- new build process (Bruno Cornec)
- Fix a bug when a disk less than 2.8 MB can be built, to include enough modules to support SCSI cds (Bruno Cornec)
- Fix a bug in .spec for RPM build (%%attr now unused) (Bruno Cornec)
- Add support for LABEL on swap partitions (Michel Loiseleur + Julien Pinon)
- Attempt to fix bug 6827 (addition of a script for busybox udhcpc to support pxe/dhcp restore) (Bruno Cornec)
- support of dm and LVM v2 (Andree Leidenfrost)
- analyze-my-lvm is under $MINDI_LIB (Andree Leidenfrost)
- Fix a bug introduced by trying to avoid an error message when modprobe.d doesn't exist (Johannes Franken)
- Fix for Bug #6975 (/net is now excluded from kernel search location) (Bruno Cornec)
- Allow 5670 MB fllopy disks for lilo as well (Bruno Cornec)
- Add missing net modules (Klaus Ade Johnstad)

* Fri Mar 10 2006 Bruno Cornec <bcornec@mandriva.org> 1.0.7-1.20060mdk
- Updated to 1.0.7
- Fix issue for 2.6 kernels with VIA chipsets (Andree Leidenfrost)
- stop creating further size of floppy disks if the smaller one succeeds (Bruno Cornec)
- init revamped (removed unnecessary second general module loading phase, start NFS appropriately depending on PXE or simple NFS) (Andree Leidenfrost)
- Changed module 'nfsacl' to 'nfs_acl' (Andree Leidenfrost)
- Mindi/DiskSize is gone (Bruno Cornec)
- useless cat, sort|uniq commands removed (Bruno Cornec/Sébastien Aperghis-Tramoni)
- Doc cleanup (Andree Leidenfrost)
- Bug fix for chown in install.sh (JeffS)
- CHANGES renamed also in install.sh now (Bruno Cornec)
- rpmlint cleanups
- Get mindi to look for analyze-my-lvm in it's library directory MINDI_LIB (See also Debian bug #351446.)
- mindi only deletes freshly created 1440kb images in case of error (See also Debian Bug #348966.) (Andree Leidenfrost)
- try standard grub-install in grub-MR restore script before trying anything fancy (Andree Leidenfrost)
- busybox mount should be called with -o ro for PXE (Make RHEL 3 works in PXE
with a 2.6 failsafe kernel now available) (Bruno Cornec)
- Fix mindi for 2.6 Failsafe support (Bruno Cornec)
- mindi now depends on grep >= 2.5 (for -m option) (Marco Puggelli/Bruno Cornec)
- Fix a bug in LVM context for RHEL4 in GetValueFromField (Rémi Bondoin/Bruno Cornec)
- New RPM Build environement (Bruno Cornec)
- mindi now supports x86_64 natively (Bruno Cornec)
- stop creating further size of floppy disks if the smaller one succeeds (Bruno Cornec)

* Fri Dec 23 2005 Bruno Cornec <bcornec@mandriva.org> 1.06-1.20060mdk
- Updated to 1.06
- mindi manpage added (Andree Leidenfrost)
- clean up remaining mount points, mindi.err at the end (Wolfgang Rosenauer)
- fix bugs for SuSE distro around tar, tr and find arguments order (Wolfgang Rosenauer)
- new busybox.net version used for better PXE support (Bruno Cornec)
- USB keyboard support (Bruno Cornec)
- -p should now work with ISO/PXE/NFS modes (Bruno Cornec)
- relocate what was under /usr/share to /usr/lib (FHS compliance) (Bruno Cornec/Andree Leidenfrost)
- manage non ambiguous delivery under /usr (packages) or /usr/local (tar ball) (Bruno Cornec)
- install script rewritten and used for RPM build, with new layout (Sébastien Aperghis-Tramoni/Bruno Cornec)
- use parted2fdisk everywhere (Bruno Cornec)
- use MONDO_LIB exported by mondoarchive instead of MONDO_HOME guessed (Bruno Cornec)
- RPM build for fedora core 4, sles9, redhat 7.3, rhel 3/4, mandriva 2006.0, mandrake 10.2/10.1 (Bruno Cornec/Gary Granger)
- VERSION/RELEASE Tag added (Bruno Cornec)
- VMPlayer support
- Code cleanup, small fixes, PXE/NFS code improvements (Wolfgang Rosenauer/Sébastien Aperghis-Tramoni/Bruno Cornec
- New switches for PXE mode (ping & ipconf, Cf README.pxe) (Sébastien Aperghis-Tramoni/Bruno Cornec)
- mindi-kernel added to SVN (Bruno Cornec)

* Sat Nov 19 2005 Bruno Cornec <bcornec@mandriva.org> 1.05-1.20060mdk
- Updated to 1.05
- Bug fix for ldd output incorrectly handled, leading to "grep not found" error (Andree Leidenfrost)
- NFS now works in interactive mode, and nolock problems are solve (Andree Leidenfrost)
- IA-64 support is now working for rhel 3 (Bruno Cornec)
- add MINDI_CONF to the mindi LOGFILE (Philippe De Muyter)
- Speed up fdisk'ing dev/ida raid devices (Philippe De Muyter)

* Tue May 03 2005 Bruno Cornec <bcornec@mandriva.org> 1.04-1.20060mdk
- Updated to 1.04
- support exec-shield
- added 'ide-generic' module to IDE modules in mindi to ensure that kernels with fully modularised IDE sub-system boot
- rewrote script 'wait-for-petris' to ensure that petris actually starts and can be restarted reliably
- fixed syntax error in mindi where a wrong delimiter is used in and sed call when processing file '/etc/issue.net'
- removed '#!/bin/bash' from file 'rootfs/etc/bashrc' (bashrc get sourced, not executed)
- removed executable flag from:
- 'rootfs/etc/ld.so.cache'
- 'rootfs/root/.profile'

* Wed Sep 29 2004 Bruno Cornec <bcornec@mandriva.org> 1.03-1.20060mdk
- Updated to 1.03
- better support of SLES 8

* Wed Jul 21 2004 Bruno Cornec <bcornec@mandriva.org> 1.02-1.20060mdk
- Updated to 1.02
- better kernel-level logging
- added ACL, xattr binaries to deplist.txt
- fixed obscure bug which occasionally stopped mindi from correctly finding and documenting all LVM2 LVM-on-RAID volumes 
1.01 (2004-06-21)
- added ide_tape and other modules to mindi's config detection
- unmount errant ramdisk ($mtpt) if fail to create boot floppy
- better support of ISO dirs at restore-time (Conor Daly)

* Fri Jun 18 2004 Bruno Cornec <bcornec@mandriva.org> 1.00-1.20060mdk
- Updated to 1.00
- first 1.0x release
- catch Ctrl-Alt-Del; trigger soft reset
- better support of SuSE 9.1
- added mdadm to deplist.txt
- better detection of multiple Mindis (Martin FÃ¼rstenau)
- don't complain if just a Mindi boot CD & not a platform for Mondo
- updated busybox to 1.0.0pre10
- removed uClibc
- add memtest support
- 2.6 kernel support
- removed Embleer files (Andree Leidenfrost)
- LVM v2 support for 2.6 (Takeru Komoriya)
- added kernel-only floppy support, to accommodate really big kernels
- updated+rebuilt busybox
- added star support
- mount /sys at boot-time
- better 64-bit and 2.6 kernel support
- better LVM, failsafe kernel support (Jim Richard)
- use LILO, not raw kernel, on 1.4MB boot floppy
- record names of unsaved modules for future reference
- enlarged ramdisk by 8MB

* Thu Mar 25 2004 Bruno Cornec <bcornec@mandriva.org> 0.95-1.20060mdk
- Updated to 0.95
- changed some '==' to '=' --- now more RH6-friendly
- allow absolute pathnames again in deplist
- disable multifunc cd thing
- better Gentoo support (Bill)
- better OnStream support
- better Slackware support (Laurenz)
- added partimagehack-static to deplist.txt
- recompiled Busybox - 10k smaller, better stack-handling
- fixed boot screen typo
- added support for 'auto' fs 
- better devfs support for Mandrake users
- better Debian+LVM support (Ralph Grewe)
- updated analyze-my-lvm to handle floating-point gigabyte -L values

* Wed Sep 24 2003 Bruno Cornec <bcornec@mandriva.org> 0.94-1.20060mdk
- Updated to 0.94
- altered rootfs's /dev entry to stop cvs from becoming confused
- tweaked MAX_COMPRESSED_SIZE
- added multi-function CD support to mindi and sbin/post-init
- re-mount root as rw just in case
- ask user to remove last data (floppy) disk if nec. (Tom Mortell)
- added support for 5th column in mountlist.txt for labels
- added symlinks.tgz
- suppress erroneous error messages re: failsafe kernel

