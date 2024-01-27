import librosa

y, sr = librosa.load(librosa.ex('nutcracker'))

# Set the hop length; at 22050 Hz, 512 samples ~= 23ms
#hop_length = 512

channels = len(y.shape)
# Separate harmonics and percussives into two waveforms
y_harmonic, y_percussive = librosa.effects.hpss(y)

#print(y_harmonic.shape,y_percussive.shape)
#check shape first.
import soundfile

with soundfile.SoundFile("nuts_harm.wav","w",sr,channels,"PCM_24") as f:
    f.write(y_harmonic)
with soundfile.SoundFile("nuts_perc.wav","w",sr,channels,"PCM_24") as f:
    f.write(y_percussive)
