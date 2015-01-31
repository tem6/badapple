#!/usr/bin/env python
# encoding: utf-8
# Image to text converter
# Covert image files to text sequence.

import Image
import sys
import traceback
th = 127  # threshold


def convertImageToText(fname):
    try:
        # Load an image.
        im = Image.open(fname)
        # Get image size.
        (w, h) = im.size
        # Convert image mode to black and white.
        mim = im.convert("1")
        # Get all pixel data in list.
        data = list(mim.getdata())

        # Convert pixel data to character.
        counter = 0
        field = True
        for pixel in data:
            # Skip field if field variable is False.
            if field:
                if pixel > th:
                    sys.stdout.write("*")
                else:
                    sys.stdout.write(" ")

            # Increase coutner
            counter = counter + 1
            # Reset counter and print a break character if counter equals to
            # the image width.
            if counter >= w:
                counter = 0
                if field:
                    sys.stdout.write("\n")
                # Switch field on/off
                field = not field
    except IOError:
        (exc_type, exc_value, exc_traceback) = sys.exc_info()
        traceback.print_tb(exc_traceback)
        # print "I/O error occurs in convertImageToText: %s" % fname
    except:
        print "Unexpected error."
        raise

# Entry point of this application.
# Verify that list of files has been set as argument.
if len(sys.argv) < 2:
    print "No necessary argument."
    exit(0)

# Copy file name.
fn_list = sys.argv[1]
try:
    # Open the file.
    f = open(fn_list)

    # Convert all image files enumerated in the file to text sequence.
    for l in f:
        convertImageToText(l.rstrip())
        print "R"

    # Close the file.
    f.close()
except IOError:
    print "I/O error occurs: %s" % fn_list
except:
    print "Unexcepted error occurs."
    raise
