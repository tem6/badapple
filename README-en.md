badapple
========

Play Bad Apple!! PV on Terminal.
The script was used to generate and play the following video on Niconico:

【Apple】ターミナルで Bad Apple!! PV 影絵【Mac】
http://www.nicovideo.jp/watch/sm24162325

## Table of Contents
1 Files structure  
2 Running environment
3 Reproduce the video
4 Details of the scripts

## Files structure
All the files composed with two Python scripts, one text file for
ascii frame, and one bash script used to play the video synchronized. 
* image2text.py
* player.py
* badgnome.sh
* bad_apple_wb.txt.zip (Unzip needed)

## Running environment
For python2.x , it is confirmed that version 2.7.5 is working.
Curses module is required to run player.py
The PIL module is required to run image2text.py

## Reproduce the video
Run following commands in terminal if you want to reproduce the video.
You have to set the line number of your terminal to at least 161x61
before execution the script.

`$python player.py bad_apple_wb.txt 30`

## Details of the scripts
Each file will be described in following.

### image2text.py:

This script convert multiple images to a contiguous sequence of string
(ASCII Art)
You need to specify the files list of the images that you want to convert
in the first argument. Use relative or absolute path.
 
eg. `$python image2text.py list.txt`
  
The string will be displayed with standard output.
There is a special string "R\n" inserted between every images as a divider.
player.py is used to reset the cursor position.
  
Because the width:height of one character in terminal is 1:2, so one character should repersent two lines of pixels. When generating the ASCII images, one of two lines will simply be skipped.

### player.py:

This script will play the string output from image2text.py sequentially as a movie in the terminal.
The first argument is the output file name generated with image2text.py.
The second argument is the number of frames to be drawn per second you specified.
  
eg. `$python player.py bad_apple_wb.txt 30`
  
The script reads one line from the specified file each time. When the line contained character "R" has been found, the cursor will be reset to the upper left corner. And then it will going on to repeat the action.

### bad_apple_wb.txt:

Resize the original video with QuickTime 7 Pro to a sequence of images. Then use image2text.py convert them and output to the text strings.

It's all. 思ってたよりも単純なプログラムでしたか？

### badgnome.sh

It's a bash script to use player.py for playing badapple in GNOME terminal, and play original video with mplayer synchronized for compare.
