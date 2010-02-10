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

emerge ${emerge_opts} virtual/gentoo-netbook-remix
