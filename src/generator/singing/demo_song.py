import librosa

target = "sample.wav"

trumpet = librosa.ex('trumpet')

print(trumpet)

# along with sample rate.
sample = librosa.load(target)
print(sample)
array, sample_rate = sample
print(type(array), type(sample_rate))
# numpy array.
pitch_estimate = librosa.pitch.estimate_tuning(array,sr=sample_rate)
print(pitch_estimate)

shifted = librosa.effects.pitch_shift(sample[0],sample[1],2)

channels = len(shifted.shape)

# next is to crop the audio file?

import soundfile

with soundfile.SoundFile("shifted.wav","w",sample[1],channels,"PCM_24") as f:
    f.write(shifted)

import matplotlib.pyplot as plt
import librosa.display

plot = librosa.display.waveplot(sample[0], sample[1])

plt.show()


