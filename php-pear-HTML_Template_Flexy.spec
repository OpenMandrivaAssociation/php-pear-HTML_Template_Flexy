%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Flexy

%define _requires_exceptions pear(Gtk/VarDump.php)

Summary:	A flexible caching template engine based on SimpleTemplate
Name:		php-pear-%{_pearname}
Version:	1.2.5
Release:	%mkrel 2
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Template_Flexy/
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
Patch0:		%{name}-case_fix.patch
Patch1:		%{name}-path_fix.patch
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
HTML_Template_Flexy started its life as a simplification of
HTML_Template_Xipe, however in version 0.2, it became one of the first
template engine to use a real Lexer, rather than regexes, making it
possible to do things like ASP.net or Cold Fusion tags. However, it
still has a very simple set of goals.
- Very Simple API,
	- easy to learn...
	- prevents to much logic going in templates
- Easy to write documentable code
	- By using object vars for a template rather than 'assign',
	  you can use PHPDoc comments to list what variable you use.
- Editable in WYSIWYG editors
	- you can create full featured templates, that don't get
	  broken every time you edit with Dreamweaver(tm) or Mozilla
	  editor
	- Uses namespaced attributes to add looping/conditionals
- Extremely Fast
	- runtime is at least 4 time smaller than most other template
	  engines (eg. Smarty)
	- uses compiled templates, as a result it is many times faster
	  on blocks and loops than than Regex templates (eg.
	  IT/phplib)
- Safer (for cross-site scripting attacks)
	- All variables default to be output as HTML escaped
	  (overridden with the :h modifier)
- Multilanguage support
	- Parses strings out of template, so you can build translation
	  tools
	- Compiles language specific templates (so translation is only
	  done once, not on every request)
- Full dynamic element support (like ASP.NET), so you can pick
	  elements to replace at runtime

The long term plan for Flexy is to be integrated as a backend for the
Future Template Package (A BC wrapper will be made available - as the
author needs to use it too).

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U
cd %{_pearname}-%{version}
%patch0 -p1
%patch1 -p1

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Flexy/{Compiler/{Flexy,Standard,Regex},Element,Plugin,Token}
	
install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Flexy/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Flexy
install %{_pearname}-%{version}/Flexy/Compiler/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Flexy/Compiler
install %{_pearname}-%{version}/Flexy/Compiler/Flexy/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Flexy/Compiler/Flexy
install %{_pearname}-%{version}/Flexy/Compiler/Standard/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Flexy/Compiler/Standard
install %{_pearname}-%{version}/Flexy/Compiler/Regex/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Flexy/Compiler/Regex
install %{_pearname}-%{version}/Flexy/Element/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Flexy/Element
install %{_pearname}-%{version}/Flexy/Plugin/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Flexy/Plugin
install %{_pearname}-%{version}/Flexy/Token/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Flexy/Token

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{Flexy/example.ini,tests}
%{_datadir}/pear/%{_class}/%{_subclass}/Flexy
%{_datadir}/pear/%{_class}/%{_subclass}/Flexy.php
%{_datadir}/pear/packages/%{_pearname}.xml
