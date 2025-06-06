import numpy as np
import matplotlib.pyplot as plt
from smstools.models import stft as STFT
from smstools.models import sineModel as SM
from smstools.models import utilFunctions as UF

(fs, x) = UF.wavread('../../../sounds/bendir.wav')
w = np.hamming(2001)
N = 2048
H = 200
t = -80
minSineDur = .02
maxnSines = 150
freqDevOffset = 10
freqDevSlope = 0.001
mX, pX = STFT.stftAnal(x, w, N, H)
tfreq, tmag, tphase = SM.sineModelAnal(x, fs, w, N, H, t, maxnSines, minSineDur, freqDevOffset, freqDevSlope)

plt.figure(1, figsize=(9.5, 7))
maxplotfreq = 800.0
maxplotbin = int(np.ceil(N*maxplotfreq/fs))
numFrames = int(mX[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
binFreq = np.arange(maxplotbin)*float(fs)/N
plt.pcolormesh(frmTime, binFreq, np.transpose(np.diff(pX[:,:maxplotbin+1],axis=1)))
plt.autoscale(tight=True)

tracks = tfreq*np.less(tfreq, maxplotfreq)
tracks[tracks<=0] = np.nan
plt.plot(frmTime, tracks, color='k', lw=1.5)
plt.autoscale(tight=True)
plt.title('pX + sinusoidal tracks (bendir.wav)')

plt.tight_layout()
plt.savefig('sineModelAnal-bendir-phase.png')
plt.show()
