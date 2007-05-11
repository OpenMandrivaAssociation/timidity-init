Name:		timidity-init
Version:	0.3
Release:	%mkrel 2
Summary:	Init script for TiMidity++ ALSA sequencer
License:	GPL
Source0:	timidity.init
Source1:	timidity.sysconfig
URL:		http://timidity.sourceforge.net/
Group:		Sound
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	TiMidity++
PreReq:		rpm-helper

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
