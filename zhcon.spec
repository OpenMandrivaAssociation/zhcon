%define version 0.2.6
%define release %mkrel 5

Summary:	Fast CJK console system
Name:		zhcon
Version:	%{version}
Release:	%{release}
License:	GPLv2+
URL:		http://zhcon.sf.net/
Group:		System/Internationalization
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

Source0:	http://ftp.debian.org/debian/pool/main/z/zhcon/zhcon_0.2.6.orig.tar.gz
Source1:	zhcon.sh
Patch0:		http://ftp.debian.org/debian/pool/main/z/zhcon/zhcon_0.2.6-4.1.diff.gz

# Patch1,2,3,4,5,6 from Fedora
Patch1: zhcon-0.2.6-flags.patch
Patch2: zhcon-0.2.6-path-define.patch
Patch3: zhcon-0.2.6-gcc43.patch
Patch4: zhcon-0.2.6-locale.patch
Patch5: zhcon-0.2.6-keyswitch.patch
Patch6: zhcon-0.2.6-processor-flags.patch

BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
BuildRequires:	bison
BuildRequires:	gpm-devel

%description
Zhcon is a fast Linux Console which supports framebuffer device. It can
display Chinese, Japanese or Korean (CJK) double byte characters. Supported
language encodings include:
GB2312, GBK, BIG5, JIS and KSCM.
It can also use input methods (table based) from unicon.

%prep
%setup -q -n %name-%version
%patch0 -p1 -b .0.26
%patch1 -p1 -b .flags
%patch2 -p0 -b .path-define
%patch3 -p0 -b .gcc43
%patch4 -p0 -b .locale
%patch5 -p0 -b .keyswitch
%patch6 -p1 -b .processor-flags
iconv -f GB2312 -t UTF-8 ChangeLog -o ChangeLog.utf && mv -f ChangeLog.utf ChangeLog
( cd doc; tar -zxf html.tar.gz; chmod 755 manual)

%build
# exit if bootstrap fails
# missing config.rpath causes automake failure
sed -i -e 's|set -x|set -e -x|' bootstrap
touch config.rpath

./bootstrap
%configure2_5x
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std

install -m755 -D %SOURCE1 %buildroot/etc/profile.d/zhcon.sh

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README README.utf8 THANKS TODO doc/bpsf.txt doc/README.html
%{_sysconfdir}/profile.d/zhcon.sh
%lang(zh_CN) %doc doc/manual*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(4755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}/
