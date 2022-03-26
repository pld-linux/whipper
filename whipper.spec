Summary:	Python CD-DA ripper preferring accuracy over speed
Name:		whipper
Version:	0.10.0
Release:	3
License:	GPL v3+
Group:		Applications
Source0:	https://github.com/whipper-team/whipper/archive/v%{version}.tar.gz
# Source0-md5:	ad9e6cb208fdb799ba21ded976e868b4
URL:		https://github.com/whipper-team/whipper
BuildRequires:	libsndfile-devel
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	cdrdao
Requires:	flac
Requires:	libcdio-paranoia-utils
Requires:	python3-discid
Requires:	python3-modules
Requires:	python3-musicbrainzngs
Requires:	python3-mutagen
Requires:	python3-pycdio > 0.20
Requires:	python3-pygobject3
Requires:	python3-requests
Requires:	python3-ruamel.yaml
Requires:	python3-setuptools
Requires:	sox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Whipper is a Python 2.7 CD-DA ripper, fork of the morituri project
(CDDA ripper for *nix systems aiming for accuracy over speed). It
improves morituri which development seems to have halted merging old
ignored pull requests, improving it with bugfixes and new features.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md HACKING README.md TODO
%attr(755,root,root) %{_bindir}/accuraterip-checksum
%attr(755,root,root) %{_bindir}/whipper
%{_datadir}/metainfo/com.github.whipper_team.Whipper.metainfo.xml
%{py3_sitedir}/whipper
%{py3_sitedir}/whipper-%{version}-py*.egg-info
%attr(755,root,root)  %{py3_sitedir}/accuraterip.cpython-*.so
