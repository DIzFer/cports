#!/bin/sh

rm /usr/lib/qt6/plugins/discover/fwupd-backend.so
rm /usr/lib/qt6/plugins/discover/kns-backend.so
echo "Removed kns and fwupd backends from discover's search path"
