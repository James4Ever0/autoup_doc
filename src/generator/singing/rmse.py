import librosa
import librosa.feature

target = "sample.wav"

ld = librosa.load(target)

sample = librosa.feature.rms(ld[0])

#print(sample)

import matplotlib.pyplot as plt

plt.plot(sample.T)

plt.show()
