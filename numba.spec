#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : numba
Version  : 0.38.1
Release  : 15
URL      : http://pypi.debian.net/numba/numba-0.38.1.tar.gz
Source0  : http://pypi.debian.net/numba/numba-0.38.1.tar.gz
Summary  : compiling Python code using LLVM
Group    : Development/Tools
License  : BSD-2-Clause
Requires: numba-bin
Requires: numba-python3
Requires: numba-license
Requires: numba-python
Requires: llvmlite
Requires: numpy
BuildRequires : llvmlite
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Numba
        *****

%package bin
Summary: bin components for the numba package.
Group: Binaries
Requires: numba-license

%description bin
bin components for the numba package.


%package license
Summary: license components for the numba package.
Group: Default

%description license
license components for the numba package.


%package python
Summary: python components for the numba package.
Group: Default
Requires: numba-python3

%description python
python components for the numba package.


%package python3
Summary: python3 components for the numba package.
Group: Default
Requires: python3-core

%description python3
python3 components for the numba package.


%prep
%setup -q -n numba-0.38.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530280603
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/numba
cp LICENSE %{buildroot}/usr/share/doc/numba/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/numba
/usr/bin/pycc

%files license
%defattr(-,root,root,-)
/usr/share/doc/numba/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
