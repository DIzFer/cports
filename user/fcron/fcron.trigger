#!/bin/sh

fcrontab -z -u systab
echo "[fcron] Regenerated binary system crontab"
