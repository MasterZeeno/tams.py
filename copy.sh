#!/usr/bin/env bash

check_and_do() {
  local file="$1"
  shift
  [[ -s "$file" ]] && "$@" || \
  echo "- Does not exists: [$file]"
}

clear
OUTDIR="${1:-/sdcard/Projects}"
mkOUTDIR -p "$OUTDIR"

for f in $(find "$OUTDIR" -mindepth 1 -maxdepth 1); do
  f2="$(basename "$f")"
  if [[ -e "$f" ]]; then
    cp -f "$f" "$f2" && echo -e "\n- Copied: [$f2]"
    [[ "$f2" =~ .*\.(sh|py)$ ]] && check_and_do "$f2" \
      chmod +x "$f2" && echo "- Execute permission granted"
  fi
done

c="copy.sh"
check_and_do "_$c" mv -f "_$c" "$c" && echo "- Updated: [$c]"

s="start.sh"
check_and_do "$s" echo -e "\n- Running [$s]...\n"; sleep 2; . "$s"
