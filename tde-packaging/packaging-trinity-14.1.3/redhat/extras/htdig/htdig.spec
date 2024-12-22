%define _disable_ld_as_needed 1
%define _disable_ld_no_undefined 1

%if 0%{?mdkver} >= 5000000
%global __cc /usr/bin/gcc
%global __cxx /usr/bin/g++
%global prefer_gcc 1
%endif

%define contentdir /var/www

Summary:	A web indexing and searching system for a small domain or intranet
Name:		htdig
Version:	3.2.0b6_19
Release:	1%{?dist}
License:	GPL
Group:		Networking/WWW
URL:		http://www.htdig.org/

Source0:	htdig_3.2.0b6.orig.tar.gz

Patch1:		patches/htdig_3.2.0b6-13.diff
Patch2:		patches/kfreebsd
Patch3:		patches/gcc-6
Patch4:		patches/sourceforge_logo
Patch5:		patches/drop-bogus-assignment
Patch6:		patches/gcc-11.patch
Patch7:		patches/fix-ftbfs-gcc14

BuildRequires:	flex >= 2.5.4a-13
BuildRequires:	libtool
BuildRequires:	gcc-c++
BuildRequires:	zlib-devel

BuildRoot:	%{_tmppath}/%{name}-buildroot

Provides: group(htdig)
Provides: user(htdig)

%description
The ht://Dig system is a complete world wide web indexing and searching system 
for a small domain or intranet. This system is not meant to replace the need 
for powerful internet-wide search systems like Lycos, Infoseek, Webcrawler and 
AltaVista. Instead it is meant to cover the search needs for a single company, 
campus, or even a particular sub section of a web site.

As opposed to some WAIS-based or web-server based search engines, ht://Dig can 
span several web servers at a site. The type of these different web servers 
doesn't matter as long as they understand the HTTP 1.0 protocol.

ht://Dig was developed at San Diego State University as a way to search the
various web servers on the campus network.

%files
%defattr(-,root,root,0755)
%dir %{_sysconfdir}/htdig
%config(noreplace) %{_sysconfdir}/htdig/cookies.txt
%config(noreplace) %{_sysconfdir}/htdig/htdig.conf
%config(noreplace) %{_sysconfdir}/htdig/HtFileType-magic.mime
%config(noreplace) %{_sysconfdir}/htdig/mime.types
%{_bindir}/*
%dir %{_libdir}/htdig
%dir %{_libdir}/htdig_db
%{_libdir}/htdig/*3.2.0.so
%{_libdir}/htdig_db/*3.2.0.so
%dir %attr(-,htdig,htdig) /var/lib/htdig
%dir %attr(-,htdig,root) %{_datadir}/htdig
%{_datadir}/htdig/*
%{_mandir}/man1/*
%{_mandir}/man8/*

%pre
egrep "^htdig:" /etc/group >/dev/null
if [ $? = 1 ]; then
		echo "adding htdig group"
		groupadd -r htdig
fi
egrep "^htdig:" /etc/passwd >/dev/null
if [ $? = 1 ]; then
		echo "adding htdig user"
		useradd -r -g htdig -s "" -d /var/lib/htdig htdig 
fi
egrep "^htdig:.*/var/lib/htdig:" /etc/passwd   >/dev/null
if [ $? = 1 ]; then
		echo "updating htdig homedir"
		perl -pi -e "s,^(htdig:.*:)[^:]+(:[^:]*)$,\1/var/lib/htdig\2," /etc/passwd
fi

%preun
# we're uninstalling
if [ $1 = 0 ]; then
		egrep "^htdig:" /etc/passwd >/dev/null
		if [ $? = 0 ]; then
			echo "removing htdig user"
			userdel htdig # userdel seems to nuke the group too..
		fi

		egrep "^htdig:" /etc/group >/dev/null
		if [ $? = 0 ]; then
			echo "removing htdig group"
			groupdel htdig
		fi
fi

##########

%package	devel
Summary:	Libraries needed to develop for htdig
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description	devel
Libraries needed to develop for htdig.

%files devel
%defattr(-,root,root)
%doc ChangeLog
%doc htdoc/*
%if 0%{?mdkver} < 5000000
%{_libdir}/htdig/*.a
%endif
%{_libdir}/htdig/*.la
%{_libdir}/htdig/*[a-z].so
%if 0%{?mdkver} < 5000000
%{_libdir}/htdig_db/*.a
%endif
%{_libdir}/htdig_db/*.la
%{_libdir}/htdig_db/*[a-z].so
%{_includedir}/*

##########

%package	web
Summary:	Scripts and HTML code needed for using ht://Dig as a web search engine
Group:		Networking/WWW
Requires:	%{name} = %{version}-%{release}
Requires:	webserver

%description	web
The ht://Dig system is a complete world wide web indexing and searching
system for a small domain or intranet. This system is not meant to replace
the need for powerful internet-wide search systems like Lycos, Infoseek,
Webcrawler and AltaVista. Instead it is meant to cover the search needs for
a single company, campus, or even a particular sub section of a web site. As
opposed to some WAIS-based or web-server based search engines, ht://Dig can
span several web servers at a site. The type of these different web servers
doesn't matter as long as they understand the HTTP 1.0 protocol.

The %{name}-web package includes CGI scripts and HTML code needed to use
ht://Dig on a website.

ht://Dig was developed at San Diego State University as a way to search the
various web servers on the campus network.

%files web
%defattr(-,root,root)
%{contentdir}/html/htdig
%{contentdir}/cgi-bin/*

%post web
# Only run this if installing for the first time
if [ "$1" = 1 ]; then
	if [ -f /etc/httpd/conf/httpd.conf ];then
	SERVERNAME="`grep '^ServerName' /etc/httpd/conf/httpd.conf | awk 'NR == 1 {print $2}'`"
	fi
	[ -z "$SERVERNAME" ] && SERVERNAME="`hostname -f`"
	[ -z "$SERVERNAME" ] && SERVERNAME="localhost"
	sed 's/^start_url:.*/#&\
# (See end of file for this parameter.)/' /etc/htdig/htdig.conf > /tmp/ht.$$
	cat /tmp/ht.$$ > /etc/htdig/htdig.conf
	rm /tmp/ht.$$
	cat >> /etc/htdig/htdig.conf <<!

# Automatically set up by htdig RPM, from your current Apache httpd.conf...
# Verify and configure these, and set maintainer above, before running
# /usr/bin/rundig.
# See /usr/doc/htdig*/attrs.html for descriptions of attributes.

# The URL(s) where htdig will start.  See also limit_urls_to above.
start_url:	http://$SERVERNAME/

# This makes sure that we don't spider the web
local_urls_only: true

# These attributes allow indexing server via local filesystem rather than HTTP.
local_urls:	http://$SERVERNAME/=/var/www/html/
local_user_urls:	http://$SERVERNAME/=/home/,/public_html/
!

fi

##########

%prep
%setup -q -n htdig-3.2.0b6
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
autoreconf -fiv


%build
%configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --enable-shared \
    --with-config-dir=%{_sysconfdir}/htdig \
    --with-common-dir=%{contentdir}/html/htdig \
    --with-database-dir=/var/lib/htdig \
    --localstatedir=/var/lib/htdig \
    --with-cgi-bin-dir=%{contentdir}/cgi-bin \
    --with-image-dir=%{contentdir}/html/htdig \
    --with-search-dir=%{contentdir}/html/htdig \
    --with-default-config-file=/etc/htdig/htdig.conf \
    --with-apache=/usr/sbin/httpd \
    --with-zlib=%{_prefix}

%if 0%{?fedora} == 40
echo "#define HAVE_SHMGET 1" >>"db/db_config.h"
%endif

%__make %{?_smp_mflags}
mv htdoc/ChangeLog .


%install
rm -rf %{buildroot}

%__make install DESTDIR=%{?buildroot}

cp %{buildroot}%{contentdir}/cgi-bin/htsearch %{buildroot}%{_bindir}

chmod 644 %{buildroot}%{contentdir}/html/htdig/*

# pb with current rpm and symlinks (4.0.3-0.8mdk)
ln -sf ./search.html %{buildroot}%{contentdir}/html/htdig/index.html

# now get rid of the %{buildroot} paths in the conf files
for i in /etc/htdig.conf /usr/bin/rundig ; do
  perl -pi -e "s|%{buildroot}||g" %{buildroot}/$i
done

%__install -d %{buildroot}%{_datadir}
mv %{buildroot}%{contentdir}/html/htdig %{buildroot}%{_datadir}
ln -sf ../../../usr/share/htdig %{buildroot}%{contentdir}/html/htdig


%clean
rm -rf %{buildroot}


%changelog
