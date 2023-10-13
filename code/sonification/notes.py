NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
OCTAVES = list(range(10))
NOTES_IN_OCTAVE = len(NOTES)



def noteToNumber(noteName: str):
    return str

def noteToNumber(note: str, octave: int) -> int:
    assert note in NOTES, "Wrong note name."
    assert octave in OCTAVES, "Wrong octave number."
    return int( NOTES.index(note) + (NOTES_IN_OCTAVE * (octave+1)) )

# print( noteToNumber("A", 4) )

def noteNumberToFreq(noteNumber):
    return 440 * (2**((noteNumber-69)/12))
