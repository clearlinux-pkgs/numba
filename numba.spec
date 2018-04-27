#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : numba
Version  : 0.38.0
Release  : 8
URL      : http://pypi.debian.net/numba/numba-0.38.0.tar.gz
Source0  : http://pypi.debian.net/numba/numba-0.38.0.tar.gz
Summary  : compiling Python code using LLVM
Group    : Development/Tools
License  : BSD-2-Clause
Requires: numba-bin
Requires: numba-python3
Requires: numba-python
Requires: llvmlite
Requires: numpy
BuildRequires : llvmlite
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Numba
        *****

%package bin
Summary: bin components for the numba package.
Group: Binaries

%description bin
bin components for the numba package.


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
%setup -q -n numba-0.38.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524857547
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
