import numpy as np
import librosa

def plot(sound):
    plt.plot(sound)
    plt.show()

import matplotlib.pyplot as plt
# here's the problem. it has the time converted.
target = "sample.wav"
sound = librosa.load(target)

ar0 = np.array([1 for _ in range(10000)])
ar1 = np.convolve(sound[0],ar0,"valid")
print(ar1.shape,sound[0].shape)
# nearly the same.
#plot(ar1)
abs0 = np.absolute(sound[0])
from scipy.signal import argrelextrema
max_ind = argrelextrema(abs0,np.greater)
print(max_ind)
# do this several times?
#plot(abs0)

