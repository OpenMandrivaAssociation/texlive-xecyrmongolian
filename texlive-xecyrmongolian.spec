Name:		texlive-xecyrmongolian
Version:	53160
Release:	1
Summary:	Basic support for the typesetting of Cyrillic Mongolian documents using (Xe|Lua)LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xecyrmongolian
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xecyrmongolian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xecyrmongolian.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xecyrmongolian.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The 'xecyrmongolian' package can be used to produce documents
in Cyrillic Mongolian using either XeLaTeX or LuaLaTeX. The
command \setlanguage can be used to load alternative
hyphenation patterns so to be able to create multilingual
documents.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/xecyrmongolian
%{_texmfdistdir}/tex/latex/xecyrmongolian
%doc %{_texmfdistdir}/doc/latex/xecyrmongolian

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
