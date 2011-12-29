# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/rcsinfo
# catalog-date 2007-01-06 10:07:33 +0100
# catalog-license lppl
# catalog-version 1.11
Name:		texlive-rcsinfo
Version:	1.11
Release:	1
Summary:	Support for the revision control system
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rcsinfo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rcsinfo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rcsinfo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rcsinfo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package to extract RCS (Revision Control System) information
and use it in a LaTeX document. For users of LaTeX2HTML
rcsinfo.perl is included.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rcsinfo/rcsinfo.cfg
%{_texmfdistdir}/tex/latex/rcsinfo/rcsinfo.sty
%doc %{_texmfdistdir}/doc/latex/rcsinfo/README
%doc %{_texmfdistdir}/doc/latex/rcsinfo/README-1.9
%doc %{_texmfdistdir}/doc/latex/rcsinfo/rcsinfo.init
%doc %{_texmfdistdir}/doc/latex/rcsinfo/rcsinfo.pdf
%doc %{_texmfdistdir}/doc/latex/rcsinfo/rcsinfo.perl
%doc %{_texmfdistdir}/doc/latex/rcsinfo/rcsinfo2html.tex
#- source
%doc %{_texmfdistdir}/source/latex/rcsinfo/Makefile
%doc %{_texmfdistdir}/source/latex/rcsinfo/rcsinfo.dtx
%doc %{_texmfdistdir}/source/latex/rcsinfo/rcsinfo.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
