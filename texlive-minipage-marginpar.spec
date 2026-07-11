%global tl_name minipage-marginpar
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Minipages with marginal notes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/minipage-marginpar
License:	lppl1.3b
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minipage-marginpar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minipage-marginpar.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minipage-marginpar.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows \marginpar-commands inside of minipages and other
boxes. (It takes another approach than marginnote by Markus Kohm: it
saves all \marginpar-commands and typesets them outside (i.e., after)
the box.) The package defines an environment minipagewithmarginpars (to
be used like minipage)--and the internal commands may be used by other
packages to define similar environments or commands.

