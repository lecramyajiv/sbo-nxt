# fedora-livecd-tde.ks
#
# Description:
# - Fedora Livecd Spin with the Trinity Desktop Environment (TDE)
# - Based on 'fedora-livecd-kde.ks' provided by Fedora 15
#
# Maintainer(s):
# - Francois Andriot <francois.andriot@free.fr>

%include fedora-live-tde-base.ks
%include fedora-live-minimization.ks


%packages
# Additional packages that are not default in trinity-desktop but useful
trinity-live-openbox

# Some TDE applications
trinity-amarok
#trinity-amarok-konqueror
#trinity-digikam
#trinity-dolphin
trinity-gtk-qt-engine
trinity-gwenview
trinity-k3b
#trinity-k3b-plugin-ffmpeg
#trinity-k3b-plugin-lame
#trinity-k3b-plugin-mad
trinity-kaffeine
#trinity-kbookreader
#trinity-kdiff3
#trinity-kgtk-qt3
#trinity-knetworkmanager
#trinity-konversation
trinity-kpowersave
#trinity-krusader
#trinity-kstreamripper
#trinity-smb4k
#trinity-tde-style-lipstik
#trinity-tdeio-umountwrapper
#trinity-tdmtheme
#trinity-twin-style-crystal
#trinity-yakuake

# Some TDE translations
#trinity-tde-i18n-French
#trinity-tde-i18n-German
#trinity-tde-i18n-Spanish
#trinity-tde-i18n-Chinese-Big5

# Fedora stuff
fuse
liveusb-creator
#yumex

# use yum-presto by default
yum-presto

### space issues

# fonts (we make no bones about admitting we're english-only)
wqy-microhei-fonts	# a compact CJK font, to replace:
-nhn-nanum-gothic-fonts	# Korean
-un-core-dotum-fonts	# Korean
-vlgothic-fonts		# Japanese
-wqy-zenhei-fonts	# simplified Chinese
-cjkuni-uming-fonts	# traditional Chinese

-paratype-pt-sans-fonts	# Cyrillic (already supported by DejaVu), huge
#-stix-fonts		# mathematical symbols

# remove input methods to free space
-@input-methods
-scim*
-m17n*
-ibus*
-iok

# save some space (from @base)
-make
-nss_db

# save space (it pulls in gdisk/udisks2/libicu)
-gnome-disk-utility

## avoid serious bugs by omitting broken stuff

%end

%post
%end
