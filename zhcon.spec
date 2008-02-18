%define version 0.2.6
%define release %mkrel 2

Summary:	Fast CJK console system
Name:		zhcon
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		http://zhcon.sf.net/
Group:		System/Internationalization
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

# http://download.sourceforge.net/zhcon/
Source0:	%{name}-0.2.5.tar.gz
Source1:	zhcon.sh
# Patch0:	Official patch, used to patch source 0.2.5 to 0.2.6
Patch0:		zhcon-0.2.5-to-0.2.6.diff.gz

# Patch1,2,3,4 from Fedora
Patch1:		zhcon-0.2.6-path.patch
Patch2:		zhcon-0.2.6-path-define.patch
Patch3:		zhcon-0.2.6-flags.patch
Patch4:		zhcon-0.2.6-64bit-fix.patch

BuildRequires:	automake1.8
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
%setup -q -n zhcon-0.2.5
%patch0 -p1 -b .0.26
%patch1 -p1 -b .instpath
%patch2 -p1 -b .path_define
%patch3 -p1 -b .flags
%patch4 -p1 -b .64bit_fix
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
