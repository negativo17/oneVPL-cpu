Name:           oneVPL-cpu
Version:        2022.1.0
Release:        2%{?dist}
Summary:        oneAPI Video Processing Library CPU Implementation
License:        MIT
URL:            https://www.intel.com/content/www/us/en/developer/tools/oneapi/onevpl.html

Source0:        https://github.com/oneapi-src/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-shared-libs.patch
Patch1:         %{name}-cxxflags.patch

Requires:       oneVPL%{?_isa}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libavcodec-devel
BuildRequires:  libavfilter-devel
BuildRequires:  libavutil-devel
BuildRequires:  libdav1d-devel
BuildRequires:  libswscale-devel
BuildRequires:  oneVPL-devel
BuildRequires:  svt-av1-devel
BuildRequires:  svt-hevc-devel
BuildRequires:  x264-devel

%description
The oneAPI Video Processing Library (oneVPL) provides a single video processing
API for encode, decode, and video processing that works across a wide range of
accelerators.

This repository contains a CPU implementation of the specification.

%prep
%autosetup -p1

%build
export VPL_BUILD_DEPENDENCIES="%{_prefix}"
%cmake \
    -DBUILD_GPL_X264:BOOL="ON" \
    -DBUILD_TESTS:BOOL="OFF" \
    -DCMAKE_BUILD_TYPE:STRING="Fedora"
%cmake_build

%install
%cmake_install

# Let RPM pick up documents in the files section
rm -fr %{buildroot}%{_docdir}

%{?ldconfig_scriptlets}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md third-party-programs.txt
%{_libdir}/libvplswref64.so.1

%changelog
* Wed Apr 06 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.0-2
- Rebuild for updated dependencies.

* Sat Mar 19 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.0-1
- Update to 2022.1.0.

* Sun Mar 13 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.6-1
- Update to 2022.0.6.

* Wed Mar 02 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.5-1
- Update to 2022.0.5.

* Tue Feb 08 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.4-1
- First build.
