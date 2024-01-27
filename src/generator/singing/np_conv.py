import numpy as np
import librosa

def plot(sound):
    plt.plot(sound)
    plt.show()

import matplotlib.pyplot as plt
# here's the problem. it has the time converted.

def findpeaks(ar1):
    from scipy.signal import find_peaks
    # distance is useful.
    peaks, _ = find_peaks(ar1, height = 0, distance=150)
    return peaks, ar1[peaks]
#    plt.plot(ar1)
#    plt.plot(peaks,ar1[peaks],"x")
#    plt.show()

target = "sample.wav"
sound = librosa.load(target)

total = 1000
center = 0.2
side = (1-center)/2
side0,center0 = int(side*total),int(total*center)
ar0 = np.array([0 for _ in range(side0)]+[1 for _ in range(center0)]+[0 for _ in range(side0)])
abs0 = np.absolute(sound[0])
ar1 = np.convolve(abs0,ar0,"valid")

location, peaks = findpeaks(sound[0])
peaks_diff = np.diff(peaks)
#plot(peaks_diff)
#plot(peaks)
from scipy.signal import find_peaks
npeaks = -1*peaks
pks0, _ =  find_peaks(npeaks)
pks1 =  npeaks[pks0]
plt.plot(npeaks)
plt.plot(pks0,pks1,"x")
plt.show()
# i can invert it.
# nearly the same.
#plot(ar1)
# do this several times?
#plot(abs0)
#plot(ar1)
# you can line up those peaks and do it again.
# how to get peak values?
