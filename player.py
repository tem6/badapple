# encoding: utf-8
# Text sequence player

import curses
import sys
import time

# Wait timing to show next frame.
def waitFrame(start, fps, next_frame):
    while True:
        # Get current time.
        now = time.clock()
        # Calcurate elapsed time from start of playing.
        delta = now - start
        # Exit this function delta reaches time to display a next frame.
        if float(next_frame) / fps <= delta:
            return

def play(window, fname, adj):

    # Define a frame-hop interval to drop frame regularly,
    # so that it can keep synchroize with the original video.
    # Adjust this value to fit the specific environment.
    frame_hop = 256

    # Initialize start_time
    start_time = time.clock()
    #curses.delay_output(0)

    try:
        f = open(fname)
        # Initialize counter of played out frames.
        framecount = 0
        # Initialize counter of real frames to be played.
        file_framecount = 0
        # Display all lines in order.
        for l in f:
            if file_framecount % frame_hop != 0:
                # Reset cursor position after complete to show a frame.
                if l[0] == 'R':
                    window.move(0,0)
                    #curses.delay_output(0)
                    # Wait next frame
                    waitFrame(start_time, adj, framecount)
                    # Increase frame counter.
                    framecount = framecount + 1
                    file_framecount = file_framecount + 1
                else:
                    # Output current line to stdout.
                    window.addstr(l)
                    #curses.delay_output(0)
                    # Refresh window.
                    window.refresh()
                #time.sleep()
            else:
                if l[0] == 'R':
                    file_framecount = file_framecount + 1
                continue
                
    except curses.error:
        window.addstr(0,0,"Windows size is too small.X(")
        window.addstr(1,0,"Expand window size and try again.")
        window.addstr(2,0,"Press any key to exit...")
        window.refresh()
        window.getch()
    except:
        raise

# Entry point of this application.
# Terminate the application if no argument set.
if len(sys.argv) < 3:
    print "No argument."
    exit(0)

fn_list = sys.argv[1]
adj = int(sys.argv[2])

curses.wrapper(play, fn_list, adj)
