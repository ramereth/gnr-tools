#!/bin/bash
# Setup GNR stage4

echo "Setup layman..."
USE=-perl emerge -q dev-util/git app-portage/layman
echo 'source /usr/portage/local/layman/layman.conf' >> /etc/make.conf
layman -q -L

echo "Adding gnome overlay.."
layman -a gnome
echo "Adding gnr overlay.."
layman -a gnr

echo "Installing GNR.."
emerge -q virtual/gentoo-netbook-remix

echo "Done!"
