#! /usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import json
import time
import sys
import os

ORIGIN_MOOD_FILE_PATH = "/Users/shanhaoqi/MyLove/niklaus520.github.com/source/life_origin/life.json"
HEXO_COMMAND_PATH = "/Users/shanhaoqi/MyLove/niklaus520.github.com"

def WriteDownYourLove(mood):
    global ORIGIN_MOOD_FILE_PATH
    with open(ORIGIN_MOOD_FILE_PATH) as data:
        moods = json.load(data)
    current_time = time.strftime("%a, %d %b %Y, %H:%M:%S %Z", time.localtime())
    current_mood = {'created_at': current_time, 'content': mood}
    moods['life'].insert(0, current_mood)
    with open(ORIGIN_MOOD_FILE_PATH, 'w') as outfile:
        json.dump(moods, outfile)

if __name__ == '__main__':
    #WriteDownYourLove("我就是试一下")
    #WriteDownYourLove("我想试试Emoji 😄")
    #WriteDownYourLove()
    if len(sys.argv) == 2:
        WriteDownYourLove(sys.argv[1])
        os.chdir(HEXO_COMMAND_PATH)
        #os.system("./saveme.py")
        #os.system('''hexo clean && hexo d && git add . && git commit -m "add mood" && git push origin source''')
        with open(os.devnull, 'wb') as devnull:
            subprocess.check_call(['./saveme.py'], stdout=devnull, stderr=subprocess.STDOUT)
            subprocess.check_call('''hexo clean && hexo d && git add . && git commit -m "add mood" && git push origin source''', shell=True, stdout=devnull, stderr=subprocess.STDOUT)
