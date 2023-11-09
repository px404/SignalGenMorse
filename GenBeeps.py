import math
from IPython.display import Audio
import numpy as np
from playsound import playsound
import time


bitrate = 44100 #number of frames per second/frameset.      
freq = 440

for i in range(0,4):
    if i == 0:
        LENGTH = 0.35 #seconds to play sound
        bitrate = max(bitrate, freq)

        sound = Audio(np.sin(2 * np.pi * freq * np.linspace(0, LENGTH, int(LENGTH * bitrate), endpoint=False)), rate=bitrate)
        dat_sound = sound.data #extract the binary in the sound

        with open("_Beep.wav",'wb') as f:
            f.write(dat_sound)

        print("Here's the long beep")        
        playsound('_Beep.wav') #Playsound was on outs with mp3 therefore had to write and store it as wav to show how it sounds (No I don't want to use mp3 players)

    if i == 1:
        time.sleep(1)
        LENGTH = 0.22 #seconds to play sound
        bitrate = max(bitrate, freq)

        sound = Audio(np.sin(2 * np.pi * freq * np.linspace(0, LENGTH, int(LENGTH * bitrate), endpoint=False)), rate=bitrate)
        dat_sound = sound.data #extract the binary in the sound

        with open("Beep.wav",'wb') as f:
            f.write(dat_sound)

        print("Here's the beep")
        playsound('Beep.wav')

    if i == 2:
        LENGTH = 0.15
        bitrate = 44100 #number of frames per second/frameset.
        freq = 1

        sound = Audio(np.sin(2 * np.pi * freq * np.linspace(0, LENGTH, int(LENGTH * bitrate), endpoint=False)), rate=bitrate)
        dat_sound = sound.data #extract the binary in the sound

        with open("Pause.wav",'wb') as f:
            f.write(dat_sound)

    if i == 2:
        LENGTH = 0.25
        bitrate = 44100 #number of frames per second/frameset.
        freq = 1 #This is to make t#set it to one, it won't accept 0 as bitrate or freq, this shouldn't be bad unless there's a precise signal detecting device that can detect frequency of 1, or this could be wrong as well idk here

        sound = Audio(np.sin(2 * np.pi * freq * np.linspace(0, LENGTH, int(LENGTH * bitrate), endpoint=False)), rate=bitrate)
        dat_sound = sound.data #extract the binary in the sound

        with open("Pause_.wav",'wb') as f:
            f.write(dat_sound)
