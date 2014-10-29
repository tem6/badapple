#!/bin/bash

#The bash script to play ascii with terminal and original video with
#mplayer synchronized. And automatically reduce the fontsize before
#playing (increase lines) and restore after playing video.

#Font size needed to increase lines number. Adjust this value to suit
#for your environment.
ch_size="6"

profile_dir="/org/gnome/terminal/legacy/profiles:/"

font_key="$profile_dir$(dconf list $profile_dir | grep ^: |sed 's/\///g')/font"

old_value=$(dconf read $font_key)
new_value=`echo $old_value | awk -v ch_size=$ch_size '{ gsub(".*",ch_size"'\''",$NF); print $0; }'`

#We should consider the action to exit video playing on the fly.
trap "echo exit!!!" SIGINT

#Resize font
dconf write $font_key "$new_value"

#Play
(mplayer $1 &>/dev/null &) & python ./player.py $2 $3

#Restore font size
dconf write $font_key "$old_value"

pkill -f $1
