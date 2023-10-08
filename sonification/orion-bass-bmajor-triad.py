import numpy as np
from notes import *
from wave_file import wave_write_16bit_mono
from musical_instruments import acoustic_piano, acoustic_guitar, pipe_organ, cello, contrabass, trombone

# Beats per minute
BPM = 100
# Duration (in seconds) for a quarter note
qNote = 60/BPM
# Duration (in seconds) for a half, 1/8, 1/16 and 1/32 notes
wNote, hNote, eNote, sNote, tNote = (qNote*4, qNote*2, qNote/2, qNote/4, qNote/8)

masterVolume = 0.9
samplingFreq = 44100
initOnset = 0.5

# Track ID, Onset time, MIDI note nunmber, Velocity (0-127), Gate time (s)
score1 = np.array([[1, initOnset,
                      noteToNumber("D#", 4), 120, qNote],
                 [1, initOnset+qNote,
                      noteToNumber("B", 1), 100, qNote],
                 [1, initOnset+qNote+qNote,
                      noteToNumber("A#", 2), 100, qNote],
                 [1, initOnset+qNote+qNote+qNote,
                      noteToNumber("C#", 3), 100, eNote],
                 [1, initOnset+qNote+qNote+qNote+eNote,
                      noteToNumber("D#", 3), 100, eNote],
                 [1, initOnset+qNote+qNote+qNote+eNote+eNote,
                      noteToNumber("C#", 4), 100, qNote+eNote],
                 [1, initOnset+qNote+qNote+qNote+eNote+eNote+qNote+eNote+eNote,
                      noteToNumber("C#", 2), 120, qNote+qNote]] )
score2 = np.array([[1, initOnset,
                      noteToNumber("D#", 4)+2, 120, qNote],
                 [1, initOnset+qNote,
                      noteToNumber("B", 1)+2, 100, qNote],
                 [1, initOnset+qNote+qNote,
                      noteToNumber("A#", 2)+2, 100, qNote],
                 [1, initOnset+qNote+qNote+qNote,
                      noteToNumber("C#", 3)+2, 100, eNote],
                 [1, initOnset+qNote+qNote+qNote+eNote,
                      noteToNumber("D#", 3)+2, 100, eNote],
                 [1, initOnset+qNote+qNote+qNote+eNote+eNote,
                      noteToNumber("C#", 4)+2, 100, qNote+eNote],
                 [1, initOnset+qNote+qNote+qNote+eNote+eNote+qNote+eNote+eNote,
                      noteToNumber("C#", 2)+2, 120, qNote+qNote]] )
score3 = np.array([[1, initOnset,
                      noteToNumber("D#", 4)+2, 120, qNote],
                 [1, initOnset+qNote,
                      noteToNumber("B", 1)+2, 100, qNote],
                 [1, initOnset+qNote+qNote,
                      noteToNumber("A#", 2)+2, 100, qNote],
                 [1, initOnset+qNote+qNote+qNote,
                      noteToNumber("C#", 3)+2, 100, eNote],
                 [1, initOnset+qNote+qNote+qNote+eNote,
                      noteToNumber("D#", 3)+2, 100, eNote],
                 [1, initOnset+qNote+qNote+qNote+eNote+eNote,
                      noteToNumber("C#", 4)+2, 100, qNote+eNote],
                 [1, initOnset+qNote+qNote+qNote+eNote+eNote+qNote+eNote+eNote,
                      noteToNumber("C#", 2)+2, 120, qNote+qNote]] )

trackCount = 3
noteCount = score1.shape[0]

score = np.append(score1, score2, axis=0)
score = np.append(score, score3, axis=0)
scoreDuration = score[ noteCount-1 ][1] + score[ noteCount-1 ][4]
masterDuration = scoreDuration + 1

print("Score duration: ", scoreDuration)
print("Master duration: ", masterDuration)

def synth(instrument):
    masterSamplesCount = int(samplingFreq * masterDuration)
    masterSamples = np.zeros(masterSamplesCount)
    
    for i in range(score.shape[0]):
        print("Track #", int(score[i, 0]), " Note #", i%noteCount)
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
        elif instrument=="cello":
            samples = cello(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="contrabass":
            samples = contrabass(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="trombone":            
            samples = trombone(samplingFreq, noteNumber, velocity, gate)
    
        offset = int(samplingFreq * onset)
        for n in range(len(samples)):
            masterSamples[offset -1 + n] += samples[n]

    for n in range(int(samplingFreq * 0.01)):
        masterSamples[n] = masterSamples[n] * n/(samplingFreq * 0.01)
        
    masterSamples = masterSamples/np.max(np.abs(masterSamples))
    masterSamples = masterSamples * masterVolume
    
    outputFileName = "wav/orion-bass-bmajor-triad-" + instrument +".wav"
    wave_write_16bit_mono(samplingFreq, masterSamples, outputFileName)
    print(outputFileName)
 
synth("piano")
#synth("pipe_organ")
# synth("cello")
# synth("contrabass")

