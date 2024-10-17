Name:		timidity-init
Version:	0.3
Release:	8
Summary:	Init script for TiMidity++ ALSA sequencer
License:	GPL
Source0:	timidity.service
Source1:	timidity.sysconfig
Source2:        timidity-wrapper.sh
URL:		https://timidity.sourceforge.net/
Group:		Sound
BuildArch:	noarch
Requires:	TiMidity++

%description
Contains init script to launch TiMidity++ as a service. This allows one to
hear music played by any application which outputs to a MIDI device
even if you do not own a MIDI synthesizer soundcard.

%install

install -d -m 755 %{buildroot}%{_unitdir}
install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -m0644 %{SOURCE0} %{buildroot}%{_unitdir}/%{name}.service
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -m0755 -D %{SOURCE2} %{buildroot}%{_bindir}/timidity-wrapper.sh

sed "s:sysconfig:%{_sysconfdir}/sysconfig:" -i %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{name}

%preun
%systemd_preun %{name}

%clean

%files
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(0644,root,root) %{_unitdir}/%{name}.service
%attr(0755,root,root) %{_bindir}/timidity-wrapper.sh

