import sound, time
from notes import *

# Musical notes and their frequencies
C2,Cs2,D2,Ds2,E2,F2,Fs2,G2,Gs2,A2,As2,B2 =(
    65.40639, 69.29566, 73.41619, 77.78175,
    82.40689, 87.30706, 92.49861, 97.99886,
    103.8262, 110.0000, 116.5409, 123.4708)
C3,Cs3,D3,Ds3,E3,F3,Fs3,G3,Gs3,A3,As3,B3 =(
    130.8128, 138.5913, 146.8324, 155.5635,
    164.8138, 174.6141, 174.6141, 195.9977,
    207.6523, 220.0000, 233.0819, 246.9417)
C4,Cs4,D4,Ds4,E4,F4,Fs4,G4,Gs4,A4,As4,B4 = (
    261.6256, 277.1826, 293.6648, 311.1270,
    329.6276, 349.2282, 369.9944, 391.9954,
    415.3047, 440.0000, 466.1638, 493.8833)
C5,Cs5,D5,Ds5,E5,F5,Fs5,G5,Gs5,A5,As5,B5 = (
    523.2511, 554.3653, 587.3295, 622.2540,
    659.2551, 698.4565, 739.9888, 783.9909,
    830.6094, 880.0000, 932.3275, 987.7666)
C6,Cs6,D6,Ds6,E6,F6,Fs6,G6,Gs6,A6,As6,B6 = (
    1046.502, 1108.731, 1174.659, 1244.508,
    1318.510, 1396.913, 1479.978, 1567.982,
    1661.219, 1760.000, 1864.655, 1975.533)
C7,Cs7,D7,Ds7,E7,F7,Fs7,G7,Gs7,A7,As7,B7 = (
    2093.005, 2217.461, 2349.318, 2489.016,
    2637.020, 2793.826, 2959.955, 3135.963,
    3322.438, 3322.438, 3729.310, 3951.066)
C8,Cs8,D8,Ds8,E8,F8,Fs8,G8,Gs8,A8,As8,B8 = (
    4186.009, 4434.922, 4698.636, 4978.032,
    5274.041, 5587.652, 5919.911, 6271.927,
    6644.875, 7040.000, 7458.620, 7902.133)

cMajorChordScale = {
    C3: [C3,E3,G3], D3: [D3,F3,A3], E3: [E3,G3,B3], F3: [F3,A3,C4], G3: [G3,B3,D4],
    A3: [A3,C4,E4], B3: [B3,D4,F4],
    C4: [C4,E4,G4], D4: [D4,F4,A4], E4: [E4,G4,B4], F4: [F4,A4,C5], G4: [G4,B4,D5],
    A4: [A4,C5,E5], B4: [B4,D5,F5], C5: [C5,E5,G5], D5: [D5,F5,A5], E5: [E5,G5,B5],
    F5: [F5,A5,C6], G5: [G5,B5,D6], A5: [A5,C6,E6], B5: [B5,D6,F6], C6: [C6,E6,G6],
    D6: [D6,F6,A6], E6: [E6,G6,B6], F6: [F6,A6,C7], G6: [G6,B6,D7], A6: [A6,C7,E7],
    B6: [B6,D7,F7], C7: [C7,E7,G7], D7: [D7,F7,A7], E7: [E7,G7,B7], F7: [F7,A7,C8],
    G7: [G7,B7,D8], A7: [A7,C8,E8], 7:[B7,D8,F8] }

# Beats per minute
BPM = 100
# Duration (in seconds) for a quarter note
qNote = 60/BPM
# Duration (in seconds) for a half, 1/8, 1/16 and 1/32 notes
hNote, eNote, sNote, tNote = (qNote*2, qNote/2, qNote/4, qNote/8)

stream = sound.init()

# sound.playTone(stream, E5, qNote)
# sound.playTone(stream, C5, qNote)
# sound.playTone(stream, A4, eNote)
# sound.playTone(stream, F4, sNote)
# sound.playTone(stream, B3, sNote)
# time.sleep(qNote)
# sound.playTone(stream, A3, eNote)
# sound.playTone(stream, C4, eNote)
# time.sleep(qNote)
# time.sleep(qNote)
# sound.playTone(stream, B5, qNote)
# 
# time.sleep(2)
# sound.playTone(stream, E5, qNote)
# sound.playTone(stream, C5, qNote)
# sound.playTone(stream, A4, eNote)
# sound.playTone(stream, F4, sNote)
# sound.playTone(stream, B3, sNote+eNote)
# sound.playTone(stream, A3, eNote+eNote)
# sound.playTone(stream, C4, eNote+qNote)
# sound.playTone(stream, B5, eNote+qNote)

time.sleep(2)
sound.playTone(stream, E5, qNote)
sound.playTone(stream, C5, qNote)
sound.playTone(stream, A4, eNote)
sound.playTone(stream, F4, sNote, 0.5)
sound.playTone(stream, B3, sNote+eNote)
time.sleep(eNote)
sound.playTone(stream, A3, eNote)
sound.playTone(stream, C4, eNote+qNote)
sound.playTone(stream, B5, eNote+qNote)

time.sleep(2)
sound.playTones(stream, cMajorChordScale[E5], qNote)
sound.playTones(stream, cMajorChordScale[C5], qNote)
sound.playTones(stream, cMajorChordScale[A4], eNote)
sound.playTones(stream, cMajorChordScale[F4], sNote, 0.5)
sound.playTones(stream, cMajorChordScale[B3], sNote+eNote)
time.sleep(eNote)
sound.playTones(stream, cMajorChordScale[A3], eNote)
sound.playTones(stream, cMajorChordScale[C4], eNote+qNote)
sound.playTones(stream, cMajorChordScale[B5], eNote+qNote)

time.sleep(2)
sound.playTones(stream, [E5, G3], qNote)
sound.playTones(stream, [C5, E3], qNote)
sound.playTones(stream, [A4, C3], eNote)
sound.playTones(stream, [F4, A2], sNote, 0.5)
sound.playTones(stream, [B3, D2], sNote+eNote)
time.sleep(eNote)
sound.playTones(stream, [A3, C2], eNote)
sound.playTones(stream, [C4, E2], eNote+qNote)
sound.playTones(stream, [B5, D4], eNote+qNote)

sound.close(stream)
