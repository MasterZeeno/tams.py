#!/usr/bin/env bash

echo -e "\n- Starting to scrape...\n"
while IFS=" " read -r url user pass; do
  [[ -z "$url" ]] && continue
  url="https://www.${url}-tams.com.ph"
  python3 main.py "$url" "$user" "$pass"
done < USERS
