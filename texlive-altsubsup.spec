Name:		texlive-altsubsup
Version:	62738
Release:	2
Summary:	Subscripts and superscripts with square brackets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/altsubsup
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/altsubsup.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/altsubsup.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/altsubsup.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package to write alternative and customisable
subscripts and superscripts, with square brackets in the source
code.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/altsubsup
%{_texmfdistdir}/tex/latex/altsubsup
%doc %{_texmfdistdir}/doc/latex/altsubsup

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
