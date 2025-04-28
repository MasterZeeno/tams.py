#!/usr/bin/env bash

DIR="USER DATA"

echo -e "\n- Starting to scrape...\n"
while IFS=" " read -r url user pass; do
  [[ -z "$url" ]] && continue
  url="https://${url}-tams.com.ph/"
  mkdir -p "$DIR/$user"
  echo "- Preparing [$user] data..."
  # python3 main.py "$url" "$user" "$pass"
done < USERS
