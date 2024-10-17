%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Mindi creates emergency boot disks/CDs using your kernel, tools and modules
Name:		mindi
Version:	3.0.2
Release:	1
License:	GPLv2+
Group:		Archiving/Backup
Url:		https://www.mondorescue.org
Source0:	ftp://ftp.mondorescue.org/src/%{name}-%{version}.tar.gz
Requires:	binutils
Requires:	dosfstools
Requires:	gawk
Requires:	grep
Requires:	mindi-busybox >= 1.18.5
Requires:	mkisofs
Requires:	mtools
Requires:	ncurses
Requires:	parted
Requires:	perl
Requires:	syslinux
Requires:	which
# Not yet possible as busybox is a binary that should go alongside
# BuildArch:	noarch

%description
Mindi takes your kernel, modules, tools and libraries, and puts them on N
bootable disks (or 1 bootable CD image). You may then boot from the disks/CD
and do system maintenance - e.g. format partitions, backup/restore data,
verify packages, etc.

It is part of the MondoRescue suite for which it creates boot media.
Homepage: http://www.mondorescue.org

%files
%config(noreplace) %{_sysconfdir}/%{name}
%doc ChangeLog INSTALL COPYING README TODO README.* NEWS 
%{_mandir}/man8/*
%{_libdir}/%{name}
%{_sbindir}/*
%{_var}/cache/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q

%build

%install
export DONT_RELINK=1

export HEAD=%{buildroot}
export PREFIX=%{_exec_prefix}
export CONFDIR=%{_sysconfdir}
export MANDIR=%{_mandir}
export LIBDIR=%{_libdir}
export CACHEDIR=%{_var}/cache/%{name}
export PKGBUILDMINDI="true"

./install.sh

