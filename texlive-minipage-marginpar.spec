Name:		texlive-minipage-marginpar
Version:	15878
Release:	2
Summary:	Minipages with marginal notes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/minipage-marginpar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minipage-marginpar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minipage-marginpar.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minipage-marginpar.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows \marginpar-commands inside of minipages and
other boxes. (It takes another approach than marginnote by
Markus Kohm: it saves all \marginpar-commands and typesets them
outside (i.e., after) the box.) The package defines an
environment minipagewithmarginpars (to be used like minipage)--
and the internal commands may be used by other packages to
define similar environments or commands.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/minipage-marginpar/minipage-marginpar.sty
%{_texmfdistdir}/tex/latex/minipage-marginpar/mpgmpar.sty
%doc %{_texmfdistdir}/doc/latex/minipage-marginpar/README
%doc %{_texmfdistdir}/doc/latex/minipage-marginpar/minipage-marginpar.pdf
#- source
%doc %{_texmfdistdir}/source/latex/minipage-marginpar/minipage-marginpar.dtx
%doc %{_texmfdistdir}/source/latex/minipage-marginpar/minipage-marginpar.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
