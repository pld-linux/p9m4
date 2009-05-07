Summary:	GUI for Prover9 and Mace4
Summary(pl.UTF-8):	Środowisko graficzne dla Prover9 i Mace4
Name:		p9m4
Version:	0.5
Release:	0.1
License:	GPL v2
Group:		Applications/Science
Source0:	http://www.cs.unm.edu/%7Emccune/prover9/gui/%{name}-v%(echo %{version} | tr -d .).tar.gz
# Source0-md5:	fe031fbc49953c580f54c11864f31a36
Patch0:		%{name}-64bit.patch
Patch1:		%{name}-python2.6.patch
Patch2:		%{name}-use-inst-paths.patch
URL:		http://www.cs.unm.edu/~mccune/prover9/gui/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-libs
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q -n %{name}-v%(echo %{version} | tr -d .)
%patch0 -p1
%patch1 -p1
%patch2 -p1

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/lib}

cp -a Images $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a Samples $RPM_BUILD_ROOT%{_datadir}/%{name}

install prover9-mace4.py $RPM_BUILD_ROOT%{_bindir}

install utilities.py wx_utilities.py files.py options.py \
	partition_input.py my_setup.py control.py platforms.py \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/lib

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
