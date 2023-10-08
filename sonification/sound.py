# Library to use PyAudio for audio output
# Feb 10, 2023 v0.14
# IoT for Kids: https://jxsboston.github.io/IoT-Kids/
#
# PyAudio's web page: https://people.csail.mit.edu/hubert/pyaudio/

import pyaudio, wave, numpy as np
from typing import Optional

audio = pyaudio.PyAudio()

# Default sampling rate: 44,100 (CD quality)
# Default # of channels: 1
# Default sound format: paInt16
# Default sample width/depth in bytes: 2 (== FORMAT/8)
# Default FPG (frames per buffer): 1024
SAMPLING_RATE = 44100
FORMAT = pyaudio.paInt16
SAMPLE_WIDTH = audio.get_sample_size(FORMAT)
CHANNELS = 1
FRAMES_PER_BUFFER = 1024

# Function to initizalize PyAudio with pre-fixed default settings
# and open a new audio stream
#   Returns a new audio stream (pyaudio.Stream). 
#
def init(*, samplingRate = SAMPLING_RATE) -> pyaudio.Stream:
    global SAMPLING_RATE
    SAMPLING_RATE = samplingRate
    stream = audio.open(rate=SAMPLING_RATE,
                        format=FORMAT,
                        channels=CHANNELS,
                        frames_per_buffer=FRAMES_PER_BUFFER,                        
                        output=True)
    return stream

# Close an open stream and terminate the current PyAudio instance
#   stream (pyaudio.Stream): a stream to be closed
#
def close(stream):
    stream.close()
    audio.terminate()

# Function to generate a sine curve and make samples on the curve
#   frequency (float):
#   duration (float):
#   gain (float): Optional. Sound volume: [0, 1.0]. Default: 1.0.
#
#   Returns a set of sound wave samples (sine curve samples) as a numpy.ndarray.
#     Each sample is a float value that is normalized in [0, 1.0]. 
#
def makeSinCurveSamples(*, frequency: float, duration: float, gain: float = 1.0) ->np.ndarray:
    sampleSize = int(duration * SAMPLING_RATE)
    factor = float(frequency) * np.pi * 2 / SAMPLING_RATE
    return np.sin(np.arange(sampleSize) * factor) * float(gain)

# Function to play a musical tone
#   stream (pyaudio.Stream): a stream to be used for playing a tone
#   frequency (float):
#   duration (float):
#   gain (float): Optional. Sound volume: [0, 1.0]. Default: 1.0.
#   
#   Returns a set of sound wave samples (sine curve samples) as a numpy.ndarray.
#     Each sample is a float value that is normalized in [0, 1.0]. 
#
def playTone(stream: pyaudio.Stream, frequency: float, duration: float, gain: float = 1.0) -> np.ndarray:
    if type(frequency) is list:
        print("A float value should have been passed as a frequency, but a list is passed.")
        return None
    if frequency >= 20000: frequency = 20000
    if frequency < 20: frequency = 20
    samples = makeSinCurveSamples(frequency=frequency, duration=duration, gain=gain)
    # Scale normalized samples to [0, 2**(SAMPLE_WIDTH*8-1].
    # If sound format is paInt16 (signed 16bits), the range is [0, 2^15].
    samplesScaled = samples * 2**(SAMPLE_WIDTH*8-1)
    stream.write(samplesScaled.astype(np.int16).tobytes())
    return samples

# Function to play multiple musical tones at the same time
#   stream (pyaudio.Stream): a stream to be used for playing tones
#   frequencyList (list): List of frequency (float) values
#   duration (float):
#   gain (float): Optional. Sound volume: [0, 1.0]. Default: 1.0.
#
#   Returns a set of sound wave samples (sine curve samples) as a numpy.ndarray.
#     Each sample is a float value that is normalized in [0, 1.0]. 
#
def playTones(stream, frequencyList, duration, gain = 1.0):
    if type(frequencyList) is not list:
        print("A list of frequency values should have been passed.")
        return None
    sampleSize = int(duration * SAMPLING_RATE)
    samples = [0] * sampleSize
    freqCount = len(frequencyList)
    for freq in frequencyList:
        if freq >= 20000: freq = 20000
        if freq < 20: freq = 20
        samples += makeSinCurveSamples(frequency=freq, duration=duration, gain=(gain/freqCount))
    # Scale normalized samples to [0, 2**(SAMPLE_WIDTH*8-1].
    # If sound format is paInt16 (signed 16bits), the range is [0, 2^15].
    samplesScaled = samples * 2**(SAMPLE_WIDTH*8-1)
    stream.write(samplesScaled.astype(np.int16).tobytes())
    return samples

# Function to beep
#   stream (pyaudio.Stream): A stream to be used to beep
#   duration (float): Duration of a beep
#   frequency (float): Optional. Default frequency is 523.251 Hz (C5 tone).
#
def beep(stream: pyaudio.Stream, duration: float, frequency: float = 523.251) ->np.ndarray:
    return playTone(stream, frequency, duration)

# Function to concatenate 2 sound wave samples
#   samples1 (numpy.ndarray): A list of sound wave samples
#   samples2 (numpy.ndarray): A list of sound wave samples
#
#   Returns a concatenated list as a numpy.ndarray.
#
def concatenateSamples(samples1, samples2):
    if type(samples1) is np.ndarray and type(samples2) is np.ndarray:
        return np.concatenate((samples1, samples2), axis=None)
    else:
        print("Provided sound wave samples are not in numpy.ndarray.")
        return None


# Function to save sound wave samples as a WAV file.
#   samples (numpy.ndarray): A list of sound wave samples, which is normalized in [0.0, 1.0].
#   outputFileName (string): Name of the output WAV file
#
def saveSamplesAsWav(samples, outputFileName):
    if type(samples) is not np.ndarray:
        print("Provided sound wave samples are not in numpy.ndarray.")
    else:
        # Scale normalized samples to [0, 2**(SAMPLE_WIDTH*8-1].
        # If sound format is paInt16 (signed 16bits), the range is [0, 2^15].
        samples = samples * 2**(SAMPLE_WIDTH*8-1)
        bData = b""
        bSamples = samples.astype(np.int16).tobytes()
        bData += bSamples
        w = wave.Wave_write(outputFileName)
        params = (CHANNELS, SAMPLE_WIDTH, SAMPLING_RATE, len(bData), "NONE", "not compressed")
        w.setparams(params)
        w.writeframes(bData)
        w.close()
