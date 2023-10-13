import numpy as np
from wave_file import wave_read_16bit_mono
from wave_file import wave_write_16bit_stereo

number_of_track = 5

# track1FileName = "wav/big-dipper-treble-cmajor-piano.wav"
# track2FileName = "wav/big-dipper-bass-cmajor-triad-piano.wav"
# track3FileName = "wav/big-dipper-bass-cmajor-qnote-accompaniment-cello.wav"
# track4FileName = "wav/big-dipper-treble-cmajor-violin.wav"
# track5FileName = "wav/big-dipper-alto-cmajor-viola.wav"
# outputFileName = "wav/big-dipper-mixed-cmajor-piano-piano-triad-violin-viola-cello-acc.wav"

track1FileName = "wav/orion-treble-bmajor-piano.wav"
track2FileName = "wav/orion-bass-bmajor-triad-piano.wav"
track3FileName = "wav/orion-bass-bmajor-qnote-accompaniment-cello.wav"
track4FileName = "wav/orion-treble-bmajor-violin.wav"
track5FileName = "wav/orion-alto-bmajor-viola.wav"
outputFileName = "wav/orion-mixed-bmajor-piano-piano-triad-violin-viola-cello-acc.wav"

fs = 44100
length_of_s_master = int(fs * 12)
# track = np.zeros((length_of_s_master, number_of_track))
# s_master = np.zeros((length_of_s_master, 1))

fs, s= wave_read_16bit_mono(track1FileName)
track = np.zeros((len(s), number_of_track))
s_master = np.zeros((len(s), number_of_track))
track[:, 0] = s
print("Track 1: sampleCount", len(s))

fs, s = wave_read_16bit_mono(track2FileName)
track[:, 1] = s
print("Track 2: sampleCount", len(s))

fs, s = wave_read_16bit_mono(track3FileName)
track[:, 2] = s
print("Track 3: sampleCount", len(s))

fs, s = wave_read_16bit_mono(track4FileName)
track[:, 3] = s
print("Track 4: sampleCount", len(s))

fs, s = wave_read_16bit_mono(track4FileName)
track[:, 4] = s
print("Track 5: sampleCount", len(s))


v = np.array([1, 1, 1, 1, 1])
p = np.array([0.25, 0.25, 1, 0, 0.75])

for i in range(number_of_track):
    s_master[:, 0] += track[:, i] * v[i] * np.cos(np.pi * p[i] / 2)
    s_master[:, 1] += track[:, i] * v[i] * np.sin(np.pi * p[i] / 2)
    

master_volume = 0.9
s_master /= np.max(np.abs(s_master))
s_master *= master_volume

# for n in range(int(len(s) * 0.01)):
#     s_master[n, 0] = s_master[n, 0] * n/(fs * 0.01)
#     s_master[n, 1] = s_master[n, 1] * n/(fs  * 0.01)


wave_write_16bit_stereo(fs, s_master, outputFileName)
print(outputFileName)