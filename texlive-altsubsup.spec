%global tl_name altsubsup
%global tl_revision 62738

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Subscripts and superscripts with square brackets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/altsubsup
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/altsubsup.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/altsubsup.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/altsubsup.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX package to write alternative and customisable subscripts and
superscripts, with square brackets in the source code.

