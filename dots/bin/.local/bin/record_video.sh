#!/bin/bash
slop=$(slop -f "%x %y %w %h %g %i") || exit 1
read -r X Y W H G ID < <(echo $slop)
ffmpeg -f x11grab -s "$W"x"$H" -i :0.0+$X,$Y \
  -framerate 24 \
  ~/videos/captures/"$(date +%y-%m-%d_%H:%M:%S)".mp4
