import librosa

import librosa.display

target = "sample.wav"

y, sr = librosa.load(target)

S = librosa.feature.melspectrogram(y=y, sr=sr)

import matplotlib.pyplot as plt

import numpy as np

fig, ax = plt.subplots()

S_dB = librosa.power_to_db(S, ref=np.max)

img = librosa.display.specshow(S_dB, x_axis='time',

                         y_axis='mel', sr=sr,

                         fmax=8000, ax=ax)

fig.colorbar(img, ax=ax, format='%+2.0f dB')

ax.set(title='Mel-frequency spectrogram')

plt.show()
