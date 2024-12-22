# -*- mode: makefile; coding: utf-8 -*-
# Copyright © 2003 Christopher L Cheney <ccheney@debian.org>
# Copyright © 2019 TDE Team
# Description: A class for TDE packages; sets TDE environment variables, etc
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# 02111-1307 USA.

ifndef _cdbs_bootstrap
_cdbs_scripts_path ?= /usr/lib/cdbs
_cdbs_rules_path ?= /usr/share/cdbs/1/rules
_cdbs_class_path ?= /usr/share/cdbs/1/class
endif

ifndef _cdbs_class_debian-qt-kde
_cdbs_class_debian-qt-kde := 1

# for dh_icons
CDBS_BUILD_DEPENDS   := $(CDBS_BUILD_DEPENDS), debhelper (>= 5.0.7ubuntu4)

# Note: This _must_ be included before autotools.mk, or it won't work.
common-configure-arch common-configure-indep:: debian/stamp-cvs-make
debian/stamp-cvs-make:
ifndef _cdbs_class_cmake
	cp -Rp /usr/share/aclocal/libtool.m4 admin/libtool.m4.in
ifneq "$(wildcard /usr/share/libtool/config/ltmain.sh)" ""
	cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
endif
ifneq "$(wildcard /usr/share/libtool/build-aux/ltmain.sh)" ""
	cp -Rp /usr/share/libtool/build-aux/ltmain.sh admin/ltmain.sh
endif
	$(MAKE) -C $(DEB_SRCDIR) -f admin/Makefile.common dist;
endif
	touch debian/stamp-cvs-make

include $(_cdbs_rules_path)/buildcore.mk$(_cdbs_makefile_suffix)

ifdef _cdbs_tarball_dir
DEB_BUILDDIR = $(_cdbs_tarball_dir)/obj-$(DEB_BUILD_GNU_TYPE)
else
DEB_BUILDDIR = obj-$(DEB_BUILD_GNU_TYPE)
endif

ifndef _cdbs_class_cmake
include $(_cdbs_class_path)/autotools.mk$(_cdbs_makefile_suffix)
endif

ifdef _cdbs_class_cmake
ifneq "$(wildcard /usr/bin/ninja)" ""
MAKE = ninja -v
DEB_MAKE_ENVVARS += DESTDIR=$(DEB_DESTDIR)
DEB_MAKE_INSTALL_TARGET = install
DEB_CMAKE_NORMAL_ARGS += -GNinja
endif
endif

ifndef _cdbs_rules_patchsys_quilt
DEB_PATCHDIRS := debian/patches/common debian/patches
endif

export kde_cgidir  = \$${libdir}/cgi-bin
export kde_confdir = \$${sysconfdir}/trinity
export kde_htmldir = \$${datadir}/doc/tde/HTML

DEB_KDE_ENABLE_FINAL := yes
DEB_INSTALL_DOCS_ALL :=

DEB_DH_MAKESHLIBS_ARGS_ALL := -V
DEB_SHLIBDEPS_INCLUDE = $(foreach p,$(PACKAGES_WITH_LIBS),debian/$(p)/usr/lib)

DEB_AC_AUX_DIR = $(DEB_SRCDIR)/admin
DEB_CONFIGURE_INCLUDEDIR = "\$${prefix}/include"
DEB_COMPRESS_EXCLUDE = .dcl .docbook -license .tag .sty .el

# The default gzip compressor has been changed in dpkg >= 1.17.0.
deb_default_compress = $(shell LANG=C dpkg-deb --version | head -n1 | \
                         sed -e "s|.*version ||" -e "s| .*||" | \
                         xargs -r dpkg --compare-versions 1.17.0 lt \
                         && echo xz || echo gzip)
ifeq ($(deb_default_compress),gzip)
DEB_DH_BUILDDEB_ARGS += -- -Z$(shell dpkg-deb --help | grep -q ":.* xz[,.]" \
                               && echo xz || echo bzip2)
endif

ifeq (,$(findstring noopt,$(DEB_BUILD_OPTIONS)))
    cdbs_treat_me_gently_arches := arm m68k alpha ppc64 armel armeb
    ifeq (,$(filter $(DEB_HOST_ARCH_CPU),$(cdbs_treat_me_gently_arches)))
        cdbs_kde_enable_final = $(if $(DEB_KDE_ENABLE_FINAL),--enable-final,)
    else
        cdbs_kde_enable_final =
    endif
endif

ifneq (,$(filter nostrip,$(DEB_BUILD_OPTIONS)))
	cdbs_kde_enable_final =
	cdbs_kde_enable_debug = --enable-debug=yes
else
	cdbs_kde_enable_debug = --disable-debug
endif

ifneq (,$(filter debug,$(DEB_BUILD_OPTIONS)))
	cdbs_kde_enable_debug = --enable-debug=full
endif

DEB_BUILD_PARALLEL ?= true

cdbs_configure_flags += \
    --with-qt-dir=/usr/share/qt3 \
    --disable-rpath \
    --with-xinerama \
    $(cdbs_kde_enable_final) \
    $(cdbs_kde_enable_debug)


# This is a convenience target for calling manually.
# It's not part of the build process.
buildprep: clean apply-patches
ifndef _cdbs_class_cmake
	$(MAKE) -f admin/Makefile.common dist
endif
	debian/rules clean

.tdepkginfo:
	echo "# TDE package information" >.tdepkginfo
	dpkg-parsechangelog | sed -n "s|^Source: |Name: |p" >>.tdepkginfo
	dpkg-parsechangelog | sed -n "s|^Version: |Version: |p" >>.tdepkginfo
	date +"DateTime: %m/%d/%Y %H:%M" -u -d "$$(dpkg-parsechangelog | sed -n 's|^Date: ||p')" >>.tdepkginfo

post-patches:: .tdepkginfo

common-build-arch:: debian/stamp-man-pages
debian/stamp-man-pages:
	if ! test -d debian/man/out; then mkdir -p debian/man/out; fi
	for f in $$(find debian/man -name '*.sgml'); do \
		docbook-to-man $$f > debian/man/out/`basename $$f .sgml`.1; \
	done
	for f in $$(find debian/man -name '*.man'); do \
		soelim -I debian/man $$f \
		> debian/man/out/`basename $$f .man`.`head -n1 $$f | awk '{print $$NF}'`; \
	done
	touch debian/stamp-man-pages

common-binary-indep::
	( set -e; \
	tmpf=`mktemp debian/versions.XXXXXX`; \
	perl debian/cdbs/versions.pl >$$tmpf; \
	for p in $(DEB_INDEP_PACKAGES); do \
	    cat $$tmpf >>debian/$$p.substvars; \
	done; \
	rm -f $$tmpf )

common-binary-arch::
	( set -e; \
	tmpf=`mktemp debian/versions.XXXXXX`; \
	perl debian/cdbs/versions.pl >$$tmpf; \
	for p in $(DEB_ARCH_PACKAGES); do \
	    cat $$tmpf >>debian/$$p.substvars; \
	done; \
	rm -f $$tmpf )
	# update multi-arch path in install files
	ls -d debian/* | \
	grep -E "(install|links)$$" | \
	while read a; do \
	    [ -d $$a ] || [ -f $$a.arch ] || \
	    ! grep -q "\$$(DEB_HOST_MULTIARCH)" $$a || \
	    sed -i.arch "s|\$$(DEB_HOST_MULTIARCH)|$(DEB_HOST_MULTIARCH)|g" $$a; \
	done

clean::
	rm -rf debian/man/out
	-rmdir debian/man
	rm -f debian/stamp-man-pages
	rm -rf debian/shlibs-check
	# revert multi-arch path in install files
	ls -d debian/* | \
	grep -E "(install|links)$$" | \
	while read a; do \
	    [ ! -f $$a.arch ] || \
	    mv $$a.arch $$a; \
	done

$(patsubst %,binary-install/%,$(DEB_PACKAGES)) :: binary-install/%:
	if test -x /usr/bin/dh_icons; then dh_icons -p$(cdbs_curpkg) $(DEB_DH_ICONCACHE_ARGS); fi
	if test -x /usr/bin/dh_desktop; then dh_desktop -p$(cdbs_curpkg) $(DEB_DH_DESKTOP_ARGS); fi
	if test -e debian/$(cdbs_curpkg).lintian; then \
		install -p -D -m644 debian/$(cdbs_curpkg).lintian \
			debian/$(cdbs_curpkg)/usr/share/lintian/overrides/$(cdbs_curpkg); \
	fi
	if test -e debian/$(cdbs_curpkg).presubj; then \
		install -p -D -m644 debian/$(cdbs_curpkg).presubj \
			debian/$(cdbs_curpkg)/usr/share/bug/$(cdbs_curpkg)/presubj; \
	fi

binary-install/$(DEB_SOURCE_PACKAGE)-doc-html::
	set -e; \
	for doc in `cd $(DEB_DESTDIR)/opt/trinity/share/doc/tde/HTML/en; find . -name index.docbook`; do \
		pkg=$${doc%/index.docbook}; pkg=$${pkg#./}; \
		echo Building $$pkg HTML docs...; \
		mkdir -p $(CURDIR)/debian/$(DEB_SOURCE_PACKAGE)-doc-html/opt/trinity/share/doc/tde/HTML/en/$$pkg; \
		cd $(CURDIR)/debian/$(DEB_SOURCE_PACKAGE)-doc-html/opt/trinity/share/doc/tde/HTML/en/$$pkg; \
		/opt/trinity/bin/meinproc $(DEB_DESTDIR)/opt/trinity/share/doc/tde/HTML/en/$$pkg/index.docbook; \
	done
	for pkg in $(DOC_HTML_PRUNE) ; do \
	  rm -rf debian/$(DEB_SOURCE_PACKAGE)-doc-html/opt/trinity/share/doc/tde/HTML/en/$$pkg; \
	done

common-build-indep:: debian/stamp-kde-apidox
debian/stamp-kde-apidox:
	$(if $(DEB_KDE_APIDOX),+$(DEB_MAKE_INVOKE) apidox)
	touch $@

common-install-indep:: common-install-kde-apidox
common-install-kde-apidox::
	$(if $(DEB_KDE_APIDOX),+DESTDIR=$(DEB_DESTDIR) $(DEB_MAKE_INVOKE) install-apidox)

cleanbuilddir::
	-$(if $(call cdbs_streq,$(DEB_BUILDDIR),$(DEB_SRCDIR)),,rm -rf $(DEB_BUILDDIR))

clean::
ifndef _cdbs_class_cmake
	if test -n "$(DEB_KDE_CVS_MAKE)" && test -d $(DEB_SRCDIR); then \
		cd $(DEB_SRCDIR); \
		find . -name Makefile.in -print | \
			xargs --no-run-if-empty rm -f; \
		rm -f Makefile.am acinclude.m4 aclocal.m4 config.h.in \
			configure configure.files configure.in stamp-h.in \
			subdirs; \
	fi
endif
	rm -f .tdepkginfo
	rm -f debian/stamp-kde-apidox
	rm -f debian/stamp-cvs-make

endif
