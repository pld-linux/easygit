Summary:	Easy git - git for mere mortals
Summary(pl.UTF-8):	Easy git - git dla zwykłych śmiertelników
Name:		easygit
Version:	20080816
Release:	3
License:	GPL v2
Group:		Development/Version Control
# git clone http://www.gnome.org/~newren/eg/eg.git
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	ad8d71eb8a19d20fe04dd155c11b6c38
# 404
#URL:		http://www.gnome.org/~newren/eg/
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	git-core >= 1.5.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# misdetected from "use an" fragment in comments
%define		_noautoreq_perl	an

%description
In short, Easy GIT is a wrapper for git, designed to make git easy to
use.

%description -l pl.UTF-8
W skrócie, Easy GIT to wrappier dla git mający na celu ułatwienie
pracy z tym narzędziem.

%package -n bash-completion-easygit
Summary:	bash-completion for easygit
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla easygit
Group:		Applications/Shell
Requires:	bash-completion
Requires:	easygit

%description -n bash-completion-easygit
This package provides bash-completion for easygit.

%description -n bash-completion-easygit -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla easygit.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/bash_completion.d}

install eg $RPM_BUILD_ROOT%{_bindir}
install bash-completion-eg.sh $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/eg

%files -n bash-completion-easygit
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/bash-completion-eg.sh
