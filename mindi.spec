#
# $Id: mindi.spec 722 2006-07-28 23:53:46Z bruno $
#
%define rel     1
%define release %mkrel %{rel}
# Official version. We keep 2.09 for update purposes
# Will be solved with 3.0
%define ver		1.0.9

Summary:	Mindi creates emergency boot disks/CDs using your kernel, tools and modules
Name:		mindi
Version:	1.09
Release:	%{release}
License:	GPL
Group:		Archiving/Backup
Url:		http://www.mondorescue.org
Source:		ftp://ftp.mondorescue.org/src/%{name}-%{ver}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{ver}-%{release}-root-%(id -u -n)
Requires:	bzip2 >= 0.9, mkisofs, ncurses, binutils, gawk, dosfstools , which, grep >= 2.5

# Not on all systems
#Conflicts:	bonnie++

%description
Mindi takes your kernel, modules, tools and libraries, and puts them on N
bootable disks (or 1 bootable CD image). You may then boot from the disks/CD
and do system maintenance - e.g.  partitions, backup/restore data,
verify packages, etc.

%prep
%setup -n %name-%{ver}
echo %{version} > VERSION

%build
%ifarch ia64
%{__make} -f Makefile.parted2fdisk clean
%{__make} -f Makefile.parted2fdisk
%endif

%install
%{__rm}  -rf $RPM_BUILD_ROOT
export DONT_RELINK=1

export PREFIX=${RPM_BUILD_ROOT}%{_exec_prefix}
export CONFDIR=${RPM_BUILD_ROOT}%{_sysconfdir}
export RPMBUILDMINDI="true"

./install.sh

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post
if [ -f /usr/local/sbin/mindi ]; then
	echo "WARNING: /usr/local/sbin/mindi exists. You should probably remove your manual mindi installation !"
fi

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/mindi/deplist.txt 
%doc ChangeLog INSTALL COPYING README TODO README.ia64 README.pxe README.busybox svn.log
%{_mandir}/man8/*
%{_libdir}/mindi
%{_sbindir}/*

