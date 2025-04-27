#!/usr/bin/env bash

OUTDIR="${OUTDIR:-/sdcard/Projects}"
ss="screenshot.png"

apt update
apt install -y \
  python3 python3-pip \
  python3-selenium chromium-driver

echo -e "\n- Starting to scrape...\n"
python3 main.py

if [[ -f "$ss" ]]; then
  cp -f "$ss" "$OUTDIR/$ss" && \
    echo -e "\n- Screenshot saved to: [$OUTDIR/$ss]\n"
fi
