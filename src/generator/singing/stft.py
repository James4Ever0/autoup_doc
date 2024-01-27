import librosa

target = "sample.wav"

y, sr = librosa.load(target)

#sft = librosa.stft(y)

pitch = librosa.cqt(y=y,sr=sr,hop_length=1024,n_bins = 84)
#print(pitch)

import librosa.display

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

img = librosa.display.specshow(librosa.amplitude_to_db(pitch,ref=np.max), x_axis="time", y_axis="cqt_note", sr=sr, fmax=8000,ax=ax)

fig.colorbar(img, ax=ax, format='%+2.0f dB')

ax.set(title='Mel-frequency spectrogram')

plt.show()

