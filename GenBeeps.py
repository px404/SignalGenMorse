import math
from IPython.display import Audio
import numpy as np
from playsound import playsound
import time


bitrate = 44100 #number of frames per second/frameset.      
freq = 440

for i in range(0,2):
    if i == 0:
        LENGTH = 0.5 #seconds to play sound
        bitrate = max(bitrate, freq)

        sound = Audio(np.sin(2 * np.pi * freq * np.linspace(0, LENGTH, int(LENGTH * bitrate), endpoint=False)), rate=bitrate)
        dat_sound = sound.data #extract the binary in the sound

        with open("_Beep.wav",'wb') as f:
            f.write(dat_sound)

        print("Here's the long beep")        
        playsound('_Beep.wav') #Playsound was on outs with mp3 therefore had to write and store it as wav to show how it sounds (No I don't want to use mp3 players)

    if i == 1:
        time.sleep(1)
        LENGTH = 0.3 #seconds to play sound
        bitrate = max(bitrate, freq)

        sound = Audio(np.sin(2 * np.pi * freq * np.linspace(0, LENGTH, int(LENGTH * bitrate), endpoint=False)), rate=bitrate)
        dat_sound = sound.data #extract the binary in the sound

        with open("Beep.wav",'wb') as f:
            f.write(dat_sound)

        print("Here's the beep")
        playsound('Beep.wav')
