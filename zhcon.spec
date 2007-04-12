%define version 0.2.5
%define release %mkrel 3

Summary:	Zhcon is a fast CJK console system
Name:		zhcon
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		http://zhcon.sf.net/
Group:		System/Internationalization
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

# http://download.sourceforge.net/zhcon/
Source0:	%{name}-%{version}.tar.gz
# 0.2.3-1mdk (Abel) various config files tuned for each locale
Source1:	%{name}-0.2.3-config.tar.bz2
# 0.2.3-1mdk (Abel) small script to check for appropriate config file
Source2:	zhcon-config.sh
# 0.2.3-1mdk (Abel) http://www.okpos.com/wiki/pos/ZhconKoreanPatch
Patch0:		%{name}-0.2.2-korean-input-0.2.patch
# 0.2.3-2mdk (Abel) GCC 3.x fix
Patch1:		%{name}-0.2.3-gcc3.patch
# 0.2.3-1mdk (Abel) Fix debug flag in configure.in
Patch2:		%{name}-0.2.3-configure-fix.patch
# 0.2.3-1mdk (Abel) Allow non-root install
Patch3:		%{name}-0.2.3-nonroot.patch
# 0.2.3-1mdk (Abel) Avoid unicon dependency altogether
Patch4:		%{name}-0.2.3-no-unicon.patch
# 0.2.3-1mdk (Abel) Move config to /etc/zhcon/zhcon.conf
Patch5:		%{name}-0.2.3-config-location.patch
# 0.2.3-2mdk (Abel) Ugly hack for allowing big5 input methods
Patch6:		%{name}-0.2.3-big5.patch
Patch7:		zhcon-0.2.3-build-fix.patch

Patch8:		zhcon-fix-gcc-3.4.patch
Patch9:		zhcon-0.2.3-CAN-2005-0072.patch
Patch10:	zhcon-0.2.3-build.patch

# Patch11:	Official patch, used to patch source 0.2.5 to 0.2.6
Patch11:	zhcon-0.2.5-to-0.2.6.diff.gz
# Patch12:	(fw, from debian) fix installation-path
Patch12:	zhcon-0.2.6-fix-installation-dir.patch

BuildRequires:	automake1.8
BuildRequires:	gettext-devel
#BuildRequires:	libggi-devel
BuildRequires:	ncurses-devel
BuildRequires:	bison
Requires(pre):	bootsplash >= 1.3.4

%description
Zhcon is a fast Linux Console which supports framebuffer device. It can
display Chinese, Japanese or Korean (CJK) double byte characters. Supported
language encodings include:
GB2312, GBK, BIG5, JIS and KSCM.
It can also use input methods (table based) from unicon.

%prep
%setup -q
#%patch0 -p1 -b .korean
#%patch1 -p1 -b .gcc3
#%patch2 -p1 -b .debugflag
#%patch3 -p1 -b .nonroot
#%patch4 -p1 -b .no-unicon
#%patch5 -p1 -b .configfile
#%patch6 -p1 -b .big5
#%patch7 -p0 -b .build
#%patch8 -p1 -b .fix_gcc_3_4
#%patch9 -p1 -b .can-2005-0072
%patch10 -p1 -b .build
%patch11 -p1 -b .0-2-6
%patch12 -p1

# needed by patch0,3,5
%__aclocal
%__automake
# needed by patch2,4
%__autoconf

# cleanup backup from patch, otherwise they will be dist'ed
rm -f src/keyboard/*.korean

%build
%configure2_5x
%make
# Uncompress the Html format documentation.
tar zxf doc/html.tar.gz

%install
[ -z "%buildroot" -o "%buildroot" = "/" ] || rm -rf %buildroot

%makeinstall

# don't include duplicate locale files
#pushd %buildroot%{_datadir}/locale
#mv zh_CN.GB2312 zh_CN
#Mv zh_TW.Big5 zh_TW
#rm -rf ./zh_CN.GBK ./zh_CN.EUC
#popd

# custom config/scripts
#tar --bzip2 -xf %{SOURCE1} -C %{buildroot}%{_sysconfdir}/%{name}/
#install -m 0755 %{SOURCE2} %{buildroot}%{_libdir}/%{name}/zhcon-config.sh

#%{find_lang} %{name}

%clean
[ -z "%buildroot" -o "%buildroot" = "/" ] || rm -rf %buildroot

%post
# FIXME: Should have a clean way to do all these
#if [ $1 = 1 ]; then
#	%{_libdir}/%{name}/zhcon-config.sh
#fi

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL README THANKS TODO doc/bpsf.txt manual/
%config(noreplace) %{_sysconfdir}/zhcon.conf
%attr(4755, root, root) %{_bindir}/zhcon
%{_mandir}/man?/*
%{_libdir}/%{name}

