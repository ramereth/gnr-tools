subarch: i686
target: stage4
rel_type: gnr-10.0
profile: gnr/linux/x86/10.0/desktop
portage_confdir: /etc/catalyst/autobuilder/portage/10.0/standard
pkgcache_path: /data/catalyst/autobuilder/packages/stage4-i686-10.0-gnr
cflags: -march=pentium4 -O2 -fomit-frame-pointer -pipe
cxxflags: -mtune=i686 -O2 -fomit-frame-pointer -pipe

stage4/use: consolekit policykit networkmanager vim-syntax pch nsplugin webkit lzma automount gnutls samba xattr bash-completion gphoto2 ffmpeg zeroconf apm ssh faac network threads pulseaudio directfb xcb cleartype glitz dga sse mmx autoipd gnome-keyring avahi mmap applet exif pango nautilus laptop sse2 sse3 caps swat aspell -cdr -dvdr
stage4/packages: virtual/gentoo-netbook-remix
#stage4/fsscript: /etc/catalyst/autobuilder/scripts/stage4-cfengine.sh
#stage4/root_overlay: /etc/catalyst/autobuilder/stage4-root-overlay
#stage4/rm: /var/cfengine/ppkeys/localhost.priv /var/cfengine/ppkeys/localhost.pub /etc/portage/package.keywords/stage /etc/portage/package.mask/stage /etc/portage/profile
