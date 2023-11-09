from playsound import playsound
import time
from pydub import AudioSegment

beep_dat = AudioSegment.from_wav("Beep.wav")
beeep_dat = AudioSegment.from_wav("_Beep.wav")
pause = AudioSegment.from_wav("Pause.wav")
pause_ = AudioSegment.from_wav("Pause_.wav")

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': '|'
}

to_enc = input("Enter the message here: ")

to_enc = " ".join(morse_code_dict[i] for i in to_enc.upper()) #This joins the individual alphabets with spaces in between and joins the words with | hence allowing us to easily write the morse code with it

print("The morse code looks like this: ",to_enc)

encoded_audio = pause
  
for i in to_enc:
    if i == '.':
        encoded_audio += beep_dat
        encoded_audio += pause
    elif i == '-':
        encoded_audio += beeep_dat
        encoded_audio += pause
    elif i == ' ' or i == '|':
        encoded_audio += pause_
    else:
        print("Invalid character in the code") #Shouldn't work as every element will be checked with the dict first itself


encoded_audio.export("EncodedMorse.wav", format="wav")
playsound("EncodedMorse.wav")
