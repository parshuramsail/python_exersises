#HEALTHY PROGRAMER
# 9AM TO 5AM
# WATER =WATER.MP3 (3.5 LITERS)- DRANK-LOG-EVERY 30 MINUTES
# EYES=EYES.MP3 -EVERY 30 MIN-EYE DONE-LOG-EVERY 30 MINUTES
# PHYSICAL ACTIVITY=PHYSICAL.MP3 EVERY- 45 MIN-EX DONE-LOG
#RULES
#PY GAME MODULE TO PLAY AUDIO

from pygame import mixer
from datetime import datetime
from time import time

def music_icon_loop(file,stoppe):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while true
