#!/bin/bash
# Setup GNR stage4
set -ex

emerge -q dev-util/git app-portage/layman
echo 'source /usr/local/portage/layman/make.conf' >> /etc/make.conf
layman -q -L &> /dev/null

layman -a gnome
layman -a gnr

# rebuild with +extras
emerge -q sys-fs/udev

emerge -q virtual/gentoo-netbook-remix
