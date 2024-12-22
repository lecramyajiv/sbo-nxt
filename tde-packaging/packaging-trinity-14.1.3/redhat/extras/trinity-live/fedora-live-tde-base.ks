# Copied from 'fedora-live-kde-base.ks'

%include fedora-live-base.ks

# Local repository
repo --name="rpmbuild" --baseurl=file:///home/francois/rpmbuild/RPMS/RPMS.fc$releasever/$basearch
repo --name="rpmbuild-noarch" --baseurl=file:///home/francois/rpmbuild/RPMS/RPMS.fc$releasever/noarch

# Trinity repositories, main mirror.
repo --name=trinity --baseurl=http://trinity.mangafrance.com/f$releasever/trinity-3.5.13/RPMS/$basearch
repo --name=trinity-noarch --baseurl=http://trinity.mangafrance.com/f$releasever/trinity-3.5.13/RPMS/noarch

# RPM Fusion repository
repo --name="RPM Fusion for Fedora - Free" --baseurl=http://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/$basearch/os/
repo --name="RPM Fusion for Fedora - Free - Updates" --baseurl=http://download1.rpmfusion.org/free/fedora/updates/$releasever/$basearch/
repo --name="RPM Fusion for Fedora - Nonfree" --baseurl=http://download1.rpmfusion.org/nonfree/fedora/releases/$releasever/Everything/$basearch/os/
repo --name="RPM Fusion for Fedora - Nonfree - Updates" --baseurl="http://download1.rpmfusion.org/nonfree/fedora/updates/$releasever/$basearch/"

%packages

### The Trinity Desktop

# Main packages
#trinity-tdeaccessibility
#trinity-tdeaddons
#trinity-tdeadmin
#trinity-tdeartwork
trinity-tdebase
#trinity-tdebindings
#trinity-tdeedu
#trinity-tdegames
#trinity-tdegraphics
trinity-tdelibs
#trinity-tdemultimedia
#trinity-tdenetwork
#trinity-tdepim
#trinity-tdeutils
#trinity-tdetoys

# Subset of tdegraphics
trinity-kamera
trinity-kcoloredit
#trinity-tdegraphics-kfile-plugins
#trinity-kdvi
#trinity-kfax
#trinity-kfaxview
trinity-kgamma
#trinity-kghostview
#trinity-kiconedit
#trinity-kmrml
#trinity-kolourpaint
#trinity-kooka
trinity-kpdf
#trinity-kpovmodeler
#trinity-kruler
trinity-ksnapshot
#trinity-ksvg
#trinity-kview
trinity-kviewshell
#trinity-libkscan
trinity-tdegraphics-libpoppler-tqt

# Subset of tdeutils
trinity-ark
trinity-kcalc
#trinity-kcharselect
#trinity-kdelirc
#trinity-kdessh
#trinity-kdf
#trinity-kedit
#trinity-kfloppy
#trinity-kgpg
#trinity-khexedit
#trinity-kjots
#trinity-klaptopdaemon
#trinity-kmilo
#trinity-kmilo-legacy
trinity-kregexpeditor
trinity-ksim
#trinity-ktimer
trinity-kwalletmanager
#trinity-superkaramba


# Subset of tdeaddons
#trinity-atlantikdesigner
#trinity-kaddressbook-plugins
trinity-kate-plugins
#trinity-tdeaddons-kfile-plugins
trinity-kicker-applets
#trinity-knewsticker-scripts
trinity-konq-plugins
#trinity-ksig
#trinity-noatun-plugins


# TDE is missing a Network Applet, so we use Gnome...
/usr/bin/nm-applet

### fixes

# make sure alsaunmute is there
alsa-utils

# make sure gnome-packagekit doesn't end up the KDE live images
-gnome-packagekit*

# Remove printing support
-cups
-cups-filters
-cups-filesystem
-cups-pk-helper
-foomatic*
-gutenprint*
-paps
-system-config-printer*

# Remove bluetooth support
-bluez
-bluez-cups

%end


%post

# create /etc/sysconfig/desktop (needed for installation)
cat > /etc/sysconfig/desktop <<EOF
DESKTOP="TDE"
DISPLAYMANAGER="/opt/trinity/bin/kdm"
EOF

# Enable TDM service (systemd)
if [ -r /usr/lib/systemd/system/tdm.service ]; then
  ln -s '/usr/lib/systemd/system/tdm.service' '/etc/systemd/system/display-manager.service'
fi

# make oxygen-gtk the default GTK+ theme for root (see #683855, #689070, #808062)
cat > /root/.gtkrc-2.0 << EOF
include "/usr/share/themes/oxygen-gtk/gtk-2.0/gtkrc"
include "/etc/gtk-2.0/gtkrc"
gtk-theme-name="oxygen-gtk"
EOF
mkdir -p /root/.config/gtk-3.0
cat > /root/.config/gtk-3.0/settings.ini << EOF
[Settings]
gtk-theme-name = oxygen-gtk
EOF

# add initscript
cat >> /etc/rc.d/init.d/livesys << EOF

if [ -e /usr/share/icons/hicolor/96x96/apps/fedora-logo-icon.png ] ; then
    # use image also for kdm
    mkdir -p /usr/share/apps/kdm/faces
    cp /usr/share/icons/hicolor/96x96/apps/fedora-logo-icon.png /usr/share/apps/kdm/faces/fedora.face.icon
fi

# make liveuser use TDE
echo "/opt/trinity/bin/startkde" > /home/liveuser/.xsession
chmod a+x /home/liveuser/.xsession
chown liveuser:liveuser /home/liveuser/.xsession

# set up autologin for user liveuser
sed -i 's/#AutoLoginEnable=true/AutoLoginEnable=true/' /opt/trinity/share/config/kdm/kdmrc
sed -i 's/#AutoLoginUser=fred/AutoLoginUser=liveuser/' /opt/trinity/share/config/kdm/kdmrc

# set up user liveuser as default user and preselected user
sed -i 's/#PreselectUser=Default/PreselectUser=Default/' /opt/trinity/share/config/kdm/kdmrc
sed -i 's/#DefaultUser=johndoe/DefaultUser=liveuser/' /opt/trinity/share/config/kdm/kdmrc

# add liveinst.desktop to favorites menu
mkdir -p /home/liveuser/.trinity/share/config/
cat > /home/liveuser/.trinity/share/config/kickoffrc << MENU_EOF
[Favorites]
FavoriteURLs=/usr/share/applications/kde4/konqbrowser.desktop,/usr/share/applications/kde4/dolphin.desktop,/usr/share/applications/kde4/systemsettings.desktop,/usr/share/applications/liveinst.desktop
MENU_EOF

# show liveinst.desktop on desktop and in menu
sed -i 's/NoDisplay=true/NoDisplay=false/' /usr/share/applications/liveinst.desktop

# chmod +x ~/Desktop/liveinst.desktop to disable KDE's security warning
chmod +x /usr/share/applications/liveinst.desktop

# copy over the icons for liveinst to hicolor
cp /usr/share/icons/gnome/16x16/apps/system-software-install.png /usr/share/icons/hicolor/16x16/apps/
cp /usr/share/icons/gnome/22x22/apps/system-software-install.png /usr/share/icons/hicolor/22x22/apps/
cp /usr/share/icons/gnome/24x24/apps/system-software-install.png /usr/share/icons/hicolor/24x24/apps/
cp /usr/share/icons/gnome/32x32/apps/system-software-install.png /usr/share/icons/hicolor/32x32/apps/
cp /usr/share/icons/gnome/48x48/apps/system-software-install.png /usr/share/icons/hicolor/48x48/apps/
cp /usr/share/icons/gnome/256x256/apps/system-software-install.png /usr/share/icons/hicolor/256x256/apps/
touch /usr/share/icons/hicolor/

# Create user Desktop directory
mkdir -p /home/liveuser/Desktop
mkdir -p /home/liveuser/Documents

# Kmix (from TDE) should be started automatically
#mkdir -p /home/liveuser/.trinity/Autostart
#ln -sf /opt/trinity/share/applications/kde/kmix.desktop /home/liveuser/.trinity/Autostart/kmix.desktop
cat <<KMIX_EOF >/home/liveuser/.trinity/share/config/kmixrc
Autostart=true
Visible=false
KMIX_EOF

# make sure to set the right permissions and selinux contexts
chown -R liveuser:liveuser /home/liveuser/
restorecon -R /home/liveuser/

# don't use prelink on a running KDE live image
sed -i 's/PRELINKING=yes/PRELINKING=no/' /etc/sysconfig/prelink

EOF

### TDE LIVECD specific features ###

# Sets 'nm-applet' to run automatically (system-wide)
ln -sf /usr/share/applications/nm-applet.desktop /opt/trinity/share/autostart/nm-applet.desktop

%end
