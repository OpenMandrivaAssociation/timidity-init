Name:		timidity-init
Version:	0.3
Release:	%mkrel 5
Summary:	Init script for TiMidity++ ALSA sequencer
License:	GPL
Source0:	timidity.init
Source1:	timidity.sysconfig
URL:		http://timidity.sourceforge.net/
Group:		Sound
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	TiMidity++
Requires(post,preun):	rpm-helper

%description
Contains init script to launch TiMidity++ as a service. This allows one to
hear music played by any application which outputs to a MIDI device
even if you do not own a MIDI synthesizer soundcard.

%install
rm -rf %buildroot

install -d -m 755 %buildroot%_initrddir
install -d -m 755 %buildroot%_sysconfdir/sysconfig
install -m 755 %SOURCE0 %buildroot%_initrddir/timidity
install -m 644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/timidity

%post
%_post_service timidity

%preun
%_preun_service timidity

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%config(noreplace) %_sysconfdir/sysconfig/timidity
%config(noreplace) %_initrddir/timidity


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.3-5mdv2010.0
+ Revision: 434386
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-4mdv2009.0
+ Revision: 242859
- rebuild
- fix prereq on rpm-helper
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri May 11 2007 David Walluck <walluck@mandriva.org> 0.3-2mdv2008.0
+ Revision: 26289
- LSB initscript
- bunzip2 sources
- fix install
- use %%mkrel
- Import timidity-init



* Sun Feb 20 2005 Abel Cheung <deaddog@mandrake.org> 0.3-1mdk
- 0.3, submitted by Miguel Barrio Orsikowsky <megamik@zarb.org>:
  o made a total rewrite of script and sysconfig file
  o modified description
- Add more parameters to allow extra tuning

* Tue Nov 16 2004 Miguel Barrio Orsikowsky <megamik@zarb.org> 0.2-2mdk
- fixed a bug in the way of launching the program
- lower quality by default (less CPU consumption)

* Tue Nov 16 2004 Miguel Barrio Orsikowsky <megamik@zarb.org> 0.2-1mdk
- modified init script to launch timidity in true daemon mode

* Tue Nov 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1-2mdk
- actually bunzip2 source
- use spaces in stead of tabs at the top of init file, using tabs breaks it
- cosmetics

* Sun Aug 29 2004 Austin Acton <austin@mandrake.org> 0.1-1mdk
- from Miguel Barrio Orsikowsky
  - first version
