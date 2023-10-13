import numpy as np
from notes import *
from wave_file import wave_write_16bit_mono
from musical_instruments import viola, acoustic_piano, violin, harp, acoustic_guitar, pipe_organ, harpsichord, electric_piano

# Beats per minute
BPM = 100
# Duration (in seconds) for a quarter note
qNote = 60/BPM
# Duration (in seconds) for a half, 1/8, 1/16 and 1/32 notes
hNote, eNote, sNote, tNote = (qNote*2, qNote/2, qNote/4, qNote/8)

masterVolume = 0.9
samplingFreq = 44100
initOnset = 0.5

# Track ID, Onset time, MIDI note nunmber, Velocity (0-127), Gate time (s)
score = np.array([[1, initOnset,
                      noteToNumber("F", 4), 100, qNote],
                 [1, initOnset+qNote,
                      noteToNumber("D", 4), 100, qNote],
                 [1, initOnset+qNote+qNote,
                      noteToNumber("B", 3), 100, eNote],
                 [1, initOnset+qNote+qNote+eNote,
                      noteToNumber("G", 3), 80, sNote],
                 [1, initOnset+qNote+qNote+eNote+sNote,
                      noteToNumber("C", 3), 100, sNote+eNote],
                 [1, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote,
                      noteToNumber("B", 2), 100, eNote],
                 [1, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote+eNote,
                      noteToNumber("D", 3), 100, eNote+qNote],
                 [1, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote+sNote+eNote+qNote,
                      noteToNumber("C", 5), 100, qNote+qNote]] )
noteCount = score.shape[0]
scoreDuration = score[ noteCount-1 ][1] + score[ noteCount-1 ][4]
masterDuration = scoreDuration + 1
print("Score duration: ", scoreDuration)
print("Master duration: ", masterDuration)

def synth(instrument):
    masterSamplesCount = int(samplingFreq * masterDuration)
    masterSamples = np.zeros(masterSamplesCount)

    for i in range(noteCount):
        print("Instrument:", instrument, " Note #", i)
        onset = score[i, 1]
#         print(onset)
        noteNumber = int(score[i, 2])
#         print(noteNumber)
        velocity = score[i, 3]
#         print(velocity)
        gate = score[i, 4]
#         print(gate)
        if instrument=="piano":
            samples = acoustic_piano(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="violin":
            samples = violin(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="harp":
            samples = harp(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="acoustic_guitar":
            samples = acoustic_guitar(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="pipe_organ":
            samples = pipe_organ(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="harpsichord":
            samples = harpsichord(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="electric_piano":
            samples = electric_piano(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="viola":
            samples = viola(samplingFreq, noteNumber, velocity, gate)
        
        offset = int(samplingFreq * onset)
        for n in range(len(samples)):
            masterSamples[offset -1 + n] += samples[n]

    for n in range(int(samplingFreq * 0.01)):
        masterSamples[n] = masterSamples[n] * n/(samplingFreq * 0.01)
        
    masterSamples = masterSamples/np.max(np.abs(masterSamples))
    masterSamples = masterSamples * masterVolume
    
    outputFileName = "wav/big-dipper-alto-cmajor-" + instrument +".wav"
    wave_write_16bit_mono(samplingFreq, masterSamples, outputFileName)
    print(outputFileName)

synth("viola")


