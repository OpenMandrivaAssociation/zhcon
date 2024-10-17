%define version 0.2.6
%define release 19

Summary:	Fast CJK console system
Name:		zhcon
Version:	%{version}
Release:	%{release}
License:	GPLv2+
URL:		https://zhcon.sf.net/
Group:		System/Internationalization

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

Patch7: zhcon-automake-1.13.patch

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
%patch7 -p1 -b .am113~
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


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.6-8mdv2011.0
+ Revision: 671957
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.6-7mdv2011.0
+ Revision: 608285
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.6-6mdv2010.1
+ Revision: 524488
- rebuilt for 2010.1

* Thu Aug 07 2008 Funda Wang <fwang@mandriva.org> 0.2.6-5mdv2009.0
+ Revision: 266343
- Sync with fedora packages

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Fri May 30 2008 Funda Wang <fwang@mandriva.org> 0.2.6-4mdv2009.0
+ Revision: 213317
- add fedora patch to make it build against gcc4.3

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.2.6-3mdv2008.1
+ Revision: 171195
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 06 2007 Funda Wang <fwang@mandriva.org> 0.2.6-2mdv2008.1
+ Revision: 115933
- make it more smart to detect utf8 environment

* Thu Jun 14 2007 Funda Wang <fwang@mandriva.org> 0.2.6-1mdv2008.0
+ Revision: 39535
- Merge fedora patches
- Clean patches


* Tue Sep 19 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.2.5-3mdv2007.0
- Rebuild

* Mon Jul 31 2006 Funda Wang <fundawang@gmail.com> 0.2.5-2mdv2007.0
- Fix build on x86-64 (re-enabled patches)

* Sun Jul 16 2006 Funda Wang <fundawang@gmail.com> 0.2.5-1mdv2007.0
- New release 0.2.6 (0.2.5 + diff)

* Thu Mar 16 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.2.3-9mdk
- patch 10: fix build

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.2.3-8mdk
- Rebuild
- %%mkrel

* Tue Jan 25 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 0.2.3-7mdk
- rebuild the security fix update from 10.1

* Thu Jan 20 2005 Vincent Danen <vdanen@mandrakesoft.com> 0.2.3-6.2.101mdk
- updated patch for CAN-2005-0072

* Mon Jan 17 2005 Vincent Danen <vdanen@mandrakesoft.com> 0.2.3-6.1.101mdk
- security fix for CAN-2005-0072

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.2.3-6mdk
- Rebuild

* Sun Feb 08 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.3-5mdk
- rebuild for libnewt-0.51
- patch 7: fix build

* Sat Oct 25 2003 Stefan van der Eijk <stefan@eijk.nu> 0.2.3-4mdk
- BuildRequires

