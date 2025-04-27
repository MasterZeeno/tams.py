#!/bin/bash

<<<<<<< HEAD
=======
# check_install() {
  # local cmd pkg="$1"
  # [[ "$pkg" == *"-"* ]] && cmd="${pkg#*-}" || cmd="$pkg"
  # if ! command -v "$cmd" >/dev/null 2>&1; then
      # apt install -y "$pkg" >/dev/null 2>&1
  # fi
# }

# OUTDIR="${OUTDIR:-/sdcard/Projects}"
# ss="screenshot.png"

#apt update #>/dev/null 2>&1
#apt upgrade -y
#apt install python3 python3-pip python3-selenium chromium-driver -y
  
# for pkg in python3 python3-pip python3-selenium chromium-driver; do
    # check_install "$pkg"
# done

>>>>>>> 0b1d9649ed70afa3cebd620ce7814ae482fbfda1
echo -e "\n- Starting to scrape...\n"
while IFS=" " read -r url user pass; do
  [[ -z "$url" ]] && continue
  url="https://www.${url}-tams.com.ph"
  python3 main.py "$url" "$user" "$pass"
done < USERS
