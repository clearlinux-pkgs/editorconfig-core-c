#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
Name     : editorconfig-core-c
Version  : 0.12.6
Release  : 4
URL      : https://github.com/editorconfig/editorconfig-core-c/archive/v0.12.6/editorconfig-core-c-0.12.6.tar.gz
Source0  : https://github.com/editorconfig/editorconfig-core-c/archive/v0.12.6/editorconfig-core-c-0.12.6.tar.gz
Summary  : Library handling EditorConfig files, a file format defining coding styles in projects.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: editorconfig-core-c-bin = %{version}-%{release}
Requires: editorconfig-core-c-lib = %{version}-%{release}
Requires: editorconfig-core-c-license = %{version}-%{release}
Requires: editorconfig-core-c-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : pcre2-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[EditorConfig][]
================
[![GitHub release](https://img.shields.io/github/release/editorconfig/editorconfig-core-c.svg)](../../releases/latest)
[![Build Status](https://github.com/editorconfig/editorconfig-core-c/actions/workflows/CI_build.yml/badge.svg)](https://github.com/editorconfig/editorconfig-core-c/actions/workflows/CI_build.yml)
[![Build status](https://ci.appveyor.com/api/projects/status/u9t8m4uech5kejoi/branch/master?svg=true)](https://ci.appveyor.com/project/xuhdev/editorconfig-core-c/branch/master)

%package bin
Summary: bin components for the editorconfig-core-c package.
Group: Binaries
Requires: editorconfig-core-c-license = %{version}-%{release}

%description bin
bin components for the editorconfig-core-c package.


%package dev
Summary: dev components for the editorconfig-core-c package.
Group: Development
Requires: editorconfig-core-c-lib = %{version}-%{release}
Requires: editorconfig-core-c-bin = %{version}-%{release}
Provides: editorconfig-core-c-devel = %{version}-%{release}
Requires: editorconfig-core-c = %{version}-%{release}

%description dev
dev components for the editorconfig-core-c package.


%package lib
Summary: lib components for the editorconfig-core-c package.
Group: Libraries
Requires: editorconfig-core-c-license = %{version}-%{release}

%description lib
lib components for the editorconfig-core-c package.


%package license
Summary: license components for the editorconfig-core-c package.
Group: Default

%description license
license components for the editorconfig-core-c package.


%package man
Summary: man components for the editorconfig-core-c package.
Group: Default

%description man
man components for the editorconfig-core-c package.


%prep
%setup -q -n editorconfig-core-c-0.12.6
cd %{_builddir}/editorconfig-core-c-0.12.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701953268
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake .. -DCMAKE_INSTALL_LIBDIR=lib64
make
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1701953268
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/editorconfig-core-c
cp %{_builddir}/editorconfig-core-c-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/editorconfig-core-c/46e70de31a676e33f85c43719cdeff01a87fd63f || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/editorconfig
/usr/bin/editorconfig-0.12.6

%files dev
%defattr(-,root,root,-)
/usr/include/editorconfig/editorconfig.h
/usr/include/editorconfig/editorconfig_handle.h
/usr/lib64/cmake/EditorConfig/EditorConfigConfig.cmake
/usr/lib64/cmake/EditorConfig/EditorConfigConfigVersion.cmake
/usr/lib64/cmake/EditorConfig/EditorConfigTargets-relwithdebinfo.cmake
/usr/lib64/cmake/EditorConfig/EditorConfigTargets.cmake
/usr/lib64/libeditorconfig.so
/usr/lib64/pkgconfig/editorconfig.pc
/usr/share/man/man3/editorconfig.h.3
/usr/share/man/man3/editorconfig_handle.h.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libeditorconfig.so.0
/usr/lib64/libeditorconfig.so.0.12.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/editorconfig-core-c/46e70de31a676e33f85c43719cdeff01a87fd63f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/editorconfig.1
/usr/share/man/man5/editorconfig-format.5
