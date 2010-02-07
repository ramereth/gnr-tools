subarch: i686
target: stage4
version_stamp: gnr-10.0
rel_type: default
profile: default/linux/x86/10.0/desktop
snapshot: 10.0
portage_confdir: /data/gnr-tools/etc/portage
source_subpath: default/system-i686-gnr-10.0

stage4/use:
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

stage4/packages:
    virtual/gentoo-netbook-remix

stage4/overlay: /data/gnr-overlay
