# $Id: mindi.spec 1866 2008-01-16 15:29:04Z bruno $
#
Summary:	Mindi creates emergency boot disks/CDs using your kernel, tools and modules
Name:		mindi
Version:	2.0.4
Packager:	Bruno Cornec <bcornec@mandriva.org>
Release:	%mkrel 3
License:	GPL
Group:		Archiving/Backup
Url:		http://www.mondorescue.org
Source:		ftp://ftp.mondorescue.org/src/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
Requires:	bzip2 >= 0.9, mkisofs, ncurses, binutils, gawk, dosfstools, mindi-busybox, parted, perl, mtools, which, grep >= 2.5
ExcludeArch: ppc

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
%ifarch ia64
%{__make} -f Makefile.parted2fdisk clean
%{__make} -f Makefile.parted2fdisk
%endif

%install
%{__rm}  -rf $RPM_BUILD_ROOT
export DONT_RELINK=1

export HEAD=${RPM_BUILD_ROOT}
export PREFIX=%{_exec_prefix}
export CONFDIR=%{_sysconfdir}
export MANDIR=%{_mandir}
export LIBDIR=%{_libdir}
export CACHEDIR=%{_var}/cache/%{name}
export PKGBUILDMINDI="true"

./install.sh

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}
%doc ChangeLog INSTALL COPYING README TODO README.* NEWS 
%{_mandir}/man8/*
%{_libdir}/%{name}
%{_sbindir}/*
%{_var}/cache/%{name}

%changelog
