#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCFDF148828C642A7 (alanc@freedesktop.org)
#
Name     : xsetroot
Version  : 1.1.2
Release  : 1
URL      : https://www.x.org/releases/individual/app/xsetroot-1.1.2.tar.gz
Source0  : https://www.x.org/releases/individual/app/xsetroot-1.1.2.tar.gz
Source99 : https://www.x.org/releases/individual/app/xsetroot-1.1.2.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT-Opengroup
Requires: xsetroot-bin
Requires: xsetroot-license
Requires: xsetroot-man
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xbitmaps)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xmuu)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)

%description
xsetroot - root window parameter setting utility for X
All questions regarding this software should be directed at the
Xorg mailing list:

%package bin
Summary: bin components for the xsetroot package.
Group: Binaries
Requires: xsetroot-license
Requires: xsetroot-man

%description bin
bin components for the xsetroot package.


%package license
Summary: license components for the xsetroot package.
Group: Default

%description license
license components for the xsetroot package.


%package man
Summary: man components for the xsetroot package.
Group: Default

%description man
man components for the xsetroot package.


%prep
%setup -q -n xsetroot-1.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535772842
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1535772842
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/xsetroot
cp COPYING %{buildroot}/usr/share/doc/xsetroot/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xsetroot

%files license
%defattr(-,root,root,-)
/usr/share/doc/xsetroot/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/xsetroot.1
