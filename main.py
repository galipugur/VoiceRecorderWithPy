import sounddevice

from scipy.io.wavfile import write

fre = 44100

second = int(input("Enter time duration in seconds: "))

recordVoice = sounddevice.rec(int(second * fre), samplerate= fre, channels= 2)

sounddevice.wait()

write("record.wav", fre, recordVoice)