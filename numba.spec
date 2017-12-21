#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : numba
Version  : 0.36.2
Release  : 4
URL      : http://pypi.debian.net/numba/numba-0.36.2.tar.gz
Source0  : http://pypi.debian.net/numba/numba-0.36.2.tar.gz
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
        
        A compiler for Python array and numerical functions
        ###################################################
        
        Numba is an Open Source NumPy-aware optimizing compiler for Python
        sponsored by Anaconda, Inc.  It uses the
        remarkable LLVM compiler infrastructure to compile Python syntax to
        machine code.
        
        It is aware of NumPy arrays as typed memory regions and so can speed-up
        code using NumPy arrays.  Other, less well-typed code will be translated
        to Python C-API calls effectively removing the "interpreter" but not removing
        the dynamic indirection.
        
        Numba is also not a tracing JIT.  It *compiles* your code before it gets
        run either using run-time type information or type information you provide
        in the decorator.
        
        Numba is a mechanism for producing machine code from Python syntax and typed
        data structures such as those that exist in NumPy.
        
        
        Dependencies
        ============
        
        * llvmlite
        * numpy (version 1.9 or higher)
        * funcsigs (for Python 2)
        
        
        Installing
        ==========
        
        The easiest way to install numba and get updates is by using the Anaconda

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
%setup -q -n numba-0.36.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513826752
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
