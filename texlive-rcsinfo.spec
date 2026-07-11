%global tl_name rcsinfo
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.11
Release:	%{tl_revision}.1
Summary:	Support for the revision control system
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rcsinfo
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rcsinfo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rcsinfo.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rcsinfo.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package to extract RCS (Revision Control System) information and use
it in a LaTeX document. For users of LaTeX2HTML rcsinfo.perl is
included.

