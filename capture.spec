%define cvsversion 20070329
Summary:	Command line tools to remote control Canon digital cameras
Name:		capture
Version:	1.0.4
Release:	%mkrel 1
License:	GPL
Group:		Graphics

Source:		http://heanet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}-cvs-%{cvsversion}.tar.bz2
Patch0:		capture-gcc4.patch
#Patch0:		ptp-utils.patch
#Patch1:		viewfinder.patch
Url:		http://capture.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libptp2-devel
BuildRequires:  libusb-devel
BuildRequires:  libreadline-devel
BuildRequires:  ncurses-devel

%description
Canon's digital cameras can all be remote-controlled by a PC via
USB. The camera comes only with Windows software for that. To
remote-capture with free software, you can use this utility. It is
based on libptp and does not only capture but also gives access to all
camera settings and it opens a live viewfinder window on the PC
screen.

The tool is command-line based, either for doing actions with shell
commands (out of scripts for example) or in an interactive command
mode (start "capture" without arguments and on the "capture>" prompt,
type "help" to know the commands and its arguments.

Should work with all compact digital cameras from Canon, most probably
does not work with all Canon EOS DSLRs. Tested with Canon PowerShot
A60, A70, S50, S60, S400 (Digital IXUS 400), they all work. Also
tested with the Canon EOS 300D (Digital Rebel) and 10D, these cameras
do not work (error on the "start" command). Note that you have to
switch your camera into PTP mode if it has an appropriate entry in its
"Setup" menu. If there is no such menu entry, the camera switches
automatically.

%prep
%setup -q -n %{name}-%{version}-cvs-%{cvsversion}
%patch0 -p1 -b .gcc4

%build
%make

%install
rm -rf %buildroot
install -m755 capture -D %buildroot%{_bindir}/capture
install -m755 job -D %buildroot%{_bindir}/capture-job
install -m755 example.sh -D %buildroot%{_bindir}/capture-example.sh

%find_lang %{name}

%clean
rm -rf %buildroot

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog
%{_bindir}/*
