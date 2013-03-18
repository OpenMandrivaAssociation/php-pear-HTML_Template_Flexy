%define		_class		HTML
%define		_subclass	Template
%define		upstream_name	%{_class}_%{_subclass}_Flexy

Name:		php-pear-%{upstream_name}
Version:	1.3.12
Release:	1
Summary:	A flexible caching template engine based on SimpleTemplate
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Template_Flexy/
Source0:	http://download.pear.php.net/package/HTML_Template_Flexy-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

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
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

cd %{upstream_name}-%{version}

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/TODO %{upstream_name}-%{version}/ChangeLog
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.11-2mdv2011.0
+ Revision: 667508
- mass rebuild

* Thu Feb 17 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.11-1
+ Revision: 638145
- 1.3.11

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.10-1mdv2011.0
+ Revision: 569611
- new version

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.9-2mdv2010.1
+ Revision: 477886
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.9-1mdv2010.0
+ Revision: 383553
- update to new version 1.3.9

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.7-1mdv2009.1
+ Revision: 357909
- update to new version 1.3.7

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-3mdv2009.1
+ Revision: 321864
- rebuild

* Sat Sep 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-2mdv2009.0
+ Revision: 281914
- rule out some more old cruft

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.4-1mdv2009.0
+ Revision: 278920
- update to new version 1.3.4

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2.5-3mdv2009.0
+ Revision: 224743
- rebuild

* Tue Feb 12 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.5-2mdv2008.1
+ Revision: 166138
- rpmlint fixes

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.5-1mdv2008.0
+ Revision: 15541
- 1.2.5


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-1mdv2007.0
+ Revision: 81107
- Import php-pear-HTML_Template_Flexy

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-1mdk
- 1.2.4
- new group (Development/PHP)

* Tue Nov 08 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-2mdk
- rule out the dep that brings in php-gtk

* Mon Nov 07 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-1mdk
- 1.2.3

* Thu Sep 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-1mdk
- 1.2.2

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-1mdk
- initial Mandriva package (PLD import)


