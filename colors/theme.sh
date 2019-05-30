#!/bin/bash -eu
if [[ $(echo "dln" | grep $1) ]] 
then
    parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
    cd "$parent_path"
    case $1 in
    "l")
        file="./themes/light"
        ;;
    "d")
        file="./themes/dark"
        ;;
    "n")
        file="./themes/new"
    esac

    xcolors=""
    kitty=""
    dunst=""
    
    # cp over template to dunstrc
    # edit it in-place there. yes?
    dunst_file="$HOME/.config/dunst/dunstrc"
    bls_file="$HOME/.config/betterlockscreenrc"
    $(cp -f "./templates/dunst_replace" $dunst_file)
    $(cp -f "./templates/betterlockscreenrc_replace" $bls_file)
    while read line;
    do
        # echo $line >> kitty
        if [[ $line != "" ]]; then
            kitty+=$line"\n"
            line_upper="${line^^}"
            a="#define "$line_upper"\n"
            xcolors+=$a
            # replace each line in file ooof rip dude xddd
            # need to split line on space
            line_split=($line_upper)
            # use sed here to replace with current color
            $(sed -i --follow-symlinks -e "s/!${line_split[0]}/${line_split[1]}/g" $dunst_file)
            # replace betterlockscreen
            $(sed -i --follow-symlinks -e "s/!${line_split[0]}/${line_split[1]}/g" $bls_file)
            
        fi
    done < $file
    # replace cursorColor to cursor in kitty
    kitty_rep="${kitty/cursorColor/cursor}"
    # echo -e $xcolors
    echo $bls_file
    echo -e $kitty_rep > "./templates/kitty"
    echo -e $xcolors > "./templates/xcolors"
    $(xrdb -merge $HOME/.Xresources)
    $(kitty @ set-colors --all ./templates/kitty)
    $(killall dunst)
    $(i3-msg restart)
    echo "Theme switched!"
else
    echo "Argument must be either d, l or n"
fi