subarch: i686
version_stamp: gnr-10.0
target: livecd-stage2
rel_type: default
profile: default/linux/x86/10.0/desktop
snapshot: 10.0
source_subpath: default/liveusb-stage1-i686-installer-10.0
portage_confdir: /data/gnr-tools/etc/portage
portage_overlay: /data/gnr-overlay

livecd/bootargs: dokeymap
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
#livecd/fsscript: /home/agaffney/release/10.0/scripts/livecd.sh
livecd/fstype: squashfs
livecd/gk_mainargs: --lvm --dmraid --evms --mdadm --makeopts=-j8
livecd/iso: /var/tmp/catalyst/builds/default/liveusb-i686-gnr-installer-10.0.iso
livecd/type: gentoo-gnr-liveusb
livecd/volid: Gentoo Linux (Gentoo Netbook Remix) 10.0 x86 LiveUSB
livecd/xdm: gdm
livecd/xsession: gnome

#livecd/root_overlay: /home/agaffney/release/10.0/overlays/common/root_overlay

boot/kernel: gentoo

boot/kernel/gentoo/sources: vanilla-sources
boot/kernel/gentoo/config: /data/catalyst/releases/weekly/kconfig/x86/installusb-2.6.32.1.config
boot/kernel/gentoo/use:
	atm
	fbcondecor
	mng
	png
	portaudio
	truetype
	usb
    consolekit
    policykit
    networkmanager
    vim-syntax
    pch
    nsplugin
    webkit
    lzma
    automount
    gnutls
    samba
    xattr
    bash-completion
    gphoto2
    ffmpeg
    zeroconf
    apm
    ssh
    faac
    network
    threads
    pulseaudio
    directfb
    xcb
    cleartype
    glitz
    dga
    sse
    mmx
    autoipd
    gnome-keyring
    avahi
    mmap
    applet
    exif
    pango
    nautilus
    laptop
    sse2
    sse3
    caps
    swat
    aspell
    -cdr
    -dvdr

boot/kernel/gentoo/packages:
    virtual/gentoo-netbook-remix 

livecd/empty:
	/var/tmp
	/var/empty
	/var/run
	/var/state
	/var/cache/edb/dep
	/tmp
	/usr/portage
	/usr/src
	/root/.ccache
	/usr/share/genkernel/pkg/x86/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/x86/*.bz2
