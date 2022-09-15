#!/usr/bin/env bash
set -e
sed -i 's/^%define version.*/%define version _VERSION_/' VirtualBox-Extension-Pack.spec
VERSION="$(curl -s http://download.virtualbox.org/virtualbox/LATEST.TXT)"
test -f Oracle_VM_VirtualBox_Extension_Pack-"$VERSION".vbox-extpack || wget https://download.virtualbox.org/virtualbox/"$VERSION"/Oracle_VM_VirtualBox_Extension_Pack-"$VERSION".vbox-extpack -O Oracle_VM_VirtualBox_Extension_Pack-"$VERSION".vbox-extpack
sed -i "s/_VERSION_/$VERSION/" VirtualBox-Extension-Pack.spec
fedpkg --release f36 local
rpm-ostree install x86_64/VirtualBox-Extension-Pack-"$VERSION"-1.x86_64.rpm
