Summary:	Python CD-DA ripper preferring accuracy over speed
Name:		whipper
Version:	0.6.0
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	https://github.com/JoeLametta/whipper/archive/v%{version}.tar.gz
# Source0-md5:	fe0335e3636b995340c975787f74e022
URL:		https://github.com/JoeLametta/whipper
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	accuraterip-checksum
Requires:	cdrdao
Requires:	flac
Requires:	libcdio-paranoia-utils
Requires:	python-modules >= 1:2.7
Requires:	python-mutagen
Requires:	python-pycdio
Requires:	python-pygobject
Requires:	python-requests
Requires:	sox
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Whipper is a Python 2.7 CD-DA ripper, fork of the morituri project
(CDDA ripper for *nix systems aiming for accuracy over speed). It
improves morituri which development seems to have halted merging old
ignored pull requests, improving it with bugfixes and new features.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md HACKING README.md TODO
%attr(755,root,root) %{_bindir}/whipper
%{py_sitescriptdir}/whipper
%{py_sitescriptdir}/whipper-%{version}-py*.egg-info
