#!/bin/bash
# Setup GNR stage4
set -ex

emerge_opts="--quiet --usepkg --buildpkg --newuse"

emerge ${emerge_opts} dev-util/git app-portage/layman
echo 'source /usr/local/portage/layman/make.conf' >> /etc/make.conf
layman -q -L &> /dev/null

layman -a gnome
layman -a gnr

# rebuild with +extras
emerge ${emerge_opts} sys-fs/udev

# copy kernel config so it builds
emerge -q sys-kernel/gentoo-sources
cp /root/kernel-config /usr/src/linux/.config

emerge ${emerge_opts} virtual/gentoo-netbook-remix

# remove kernel stuff
emerge -Cq sys-kernel/gentoo-sources
rm -rf /usr/src/linux/
