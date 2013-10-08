%define		pkgname	libphutil
%include	/usr/lib/rpm/macros.php
Summary:	Collection of utility classes and functions for PHP
Name:		php-%{pkgname}
Version:	0.0.1
Release:	0.1
License:	Apache v2.0
Group:		Applications/WWW
Source0:	https://github.com/facebook/libphutil/archive/master/libphutil.tar.gz
# Source0-md5:	276ec0faafabc48ca08ecab54e504b19
URL:		http://www.phabricator.com/docs/libphutil/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libphutil (pronounced as "lib-futile", like the English word futile)
is a collection of PHP utility classes and functions which provide
powerful extensions to the standard library.

This code was originally developed at Facebook and parts of it appear
in the core libraries for <http://www.facebook.com/>.

libphutil is principally the shared library for Arcanist and
Phabricator (see http://www.phabricator.org/), but is suitable for
inclusion in other projects. In particular, some of the classes
provided in this library vastly improve the state of common operations
in PHP, like executing system commands.

%prep
%setup -qc -n %{pkgname}-%{version}
mv libphutil-*/{.??*,*} .

grep -rlE '/usr/local/bin|bin/env' . | xargs sed -i -e ' 1 {
	s,/usr/local/bin/php,/usr/bin/php,
	s,/usr/bin/env .*php,/usr/bin/php,
}'

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/%{pkgname}
cp -a resources scripts src support $RPM_BUILD_ROOT%{php_data_dir}/%{pkgname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NOTICE
%{php_data_dir}/libphutil
