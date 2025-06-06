import numpy as np
from smstools.models import stft as STFT
from smstools.models import utilFunctions as UF
import matplotlib.pyplot as plt

(fs, x) = UF.wavread('../../../sounds/piano.wav')

plt.figure(1, figsize=(9.5, 6))

w = np.hamming(256)
N = 256
H = 128
mX1, pX1 = STFT.stftAnal(2*x, w, N, H)
plt.subplot(211)
numFrames = int(mX1[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
binFreq = np.arange(mX1[0,:].size)*float(fs)/N
plt.pcolormesh(frmTime, binFreq, np.transpose(mX1), shading='nearest', snap='true')
plt.title('mX (piano.wav), Hamming window, M=256, N=256, H=128')
plt.autoscale(tight=True)

w = np.hamming(1024)
N = 1024
H = 128
mX2, pX2 = STFT.stftAnal(2*x, w, N, H)

plt.subplot(212)
numFrames = int(mX2[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
binFreq = np.arange(mX2[0,:].size)*float(fs)/N
plt.pcolormesh(frmTime, binFreq, np.transpose(mX2), shading='nearest', snap='true')
plt.title('mX (piano.wav), Hamming window, M=1024, N=1024, H=128')
plt.autoscale(tight=True)

plt.tight_layout()
plt.savefig('time-freq-compromise.png')
plt.show()

