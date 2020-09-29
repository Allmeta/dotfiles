#!/usr/bin/env sh

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -x polybar >/dev/null; do sleep 1; done

# wait for pulseaudio xd

until pgrep -x pulseaudio >/dev/null; do sleep 1; done

# Launch polybar
polybar -c ~/.config/polybar/config ${1:-i3} 2>~/polybar-log &
