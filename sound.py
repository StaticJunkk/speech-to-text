import sounddevice as sd
import os
from scipy.io.wavfile import write


def record(duration):
    fs = 44100  # Sample rate
    seconds = duration  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)


def delete():
    if os.path.exists('output.wav'):
        os.remove('output.wav')
