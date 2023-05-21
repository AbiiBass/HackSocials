from vosk import Model, KaldiRecognizer

import pyaudio

p = pyaudio.PyAudio()
CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
input_stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=1,
                frames_per_buffer=CHUNK)

output_stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                output_device_index=6,
                frames_per_buffer=CHUNK)

model = Model("vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, RATE)


while True:
    data = input_stream.read(CHUNK)

    #output_stream.write(data)

    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(text)

