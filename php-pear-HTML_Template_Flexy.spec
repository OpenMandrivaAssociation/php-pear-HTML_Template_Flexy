%define _class		HTML
%define _subclass	Template
%define modname	%{_class}_%{_subclass}_Flexy
 
Summary:	A flexible caching template engine based on SimpleTemplate
Name:		php-pear-%{modname}
Version:	1.3.13
Release:	5
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/HTML_Template_Flexy/
Source0:	http://download.pear.php.net/package/HTML_Template_Flexy-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

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

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

cd %{modname}-%{version}

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/TODO %{modname}-%{version}/ChangeLog
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml
%{_datadir}/pear/doc/HTML_Template_Flexy/*
%{_datadir}/pear/test/HTML_Template_Flexy/tests/*
