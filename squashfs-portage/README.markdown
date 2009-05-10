Squashfs Portage tree
=====================

One of Gentoo's annoying draw backs is the nature of the portage tree on its
affects on disk usage. With a standard ext3 filesystem, it could use up to
700-800MB of space which is a lot for a netbook. Considering you probably will
rarely compile things directly on your netbook, you may not need the portage
tree that much but its still nice to have around.

The next best alternative is to use squashfs for the portage tree. Squashfs is
compressed read-only filesystem which is normally used for the livecds. A
squashfs compressed portage tree uses only 45MB of space!

create-sqfs-portage
-------------------

This will create a squashfs portage tree by pulling the latest Gentoo snapshot
tarball from your selected mirror and copy it to a directory for your webserver.

update-sqfs-portage
-------------------

This script is intended to be used on your netbook and will pull the latest
squashfs file from your designated host.

TODO
----

I plan to clean up the scripts and make them more configurable but input is
welcome of course!

vim: tw=80 ft=txt :
