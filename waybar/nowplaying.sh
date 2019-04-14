#!/usr/bin/env bash

set -euo pipefail

title=$(playerctl metadata title)
artist=$(playerctl metadata artist)
player_status=$(playerctl status)

if [ "$player_status" = "Playing" ]; then
    printf "%s by %s" "$title" "$artist" 2>/dev/null
else
    printf "$player_status"
fi
