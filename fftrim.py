#!/usr/bin/env python3

import sys
import os
import datetime

def timecode2seconds(timecode):
    t = datetime.datetime.strptime(timecode, "%H:%M:%S")
    minutes = 60 * t.hour + t.minute
    seconds = minutes * 60 + t.second
    return seconds

src = sys.argv[1]
timecode_file = sys.argv[2]

with open(timecode_file, 'r') as timecode_file_lol:
    timecodes_lol = timecode_file_lol.readlines()
    timecodes = [0]
    for timecode in timecodes_lol:
        if len(timecode) <= 1:
            continue
        timecode = timecode2seconds(timecode[:-1])
        timecodes.append(timecode)
    timecode_file_lol.close()

counter = -1

while True:
    counter += 1
    try:
        begin = timecodes[counter]
    except IndexError:
        print("All done!")
        exit(0)
    try:
        duration = timecodes[counter + 1] - timecodes[counter]
        print("Beginning at second: " + str(begin) + " with a length of: " + str(duration) + " seconds")
        os.system("ffmpeg -v quiet -stats -i " + src + " -ss " + str(begin) + " -t " + str(duration)  + " " + os.getcwd() + "/out" + str(counter) + ".mkv")
    except IndexError:
        print("Beginning at second: " + str(begin))
        os.system("ffmpeg -v quiet -stats -i " + src + " -ss " + str(begin) + " " + os.getcwd() + "/out" + str(counter) + ".mkv")
