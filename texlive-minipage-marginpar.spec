# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/minipage-marginpar
# catalog-date 2008-04-09 16:44:20 +0200
# catalog-license lppl
# catalog-version v0.2
Name:		texlive-minipage-marginpar
Version:	v0.2
Release:	7
Summary:	Minipages with marginal notes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/minipage-marginpar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minipage-marginpar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minipage-marginpar.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minipage-marginpar.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.2-2
+ Revision: 754011
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v0.2-1
+ Revision: 719036
- texlive-minipage-marginpar
- texlive-minipage-marginpar
- texlive-minipage-marginpar
- texlive-minipage-marginpar

