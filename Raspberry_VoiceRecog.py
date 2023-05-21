import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import subprocess
from vosk import Model, KaldiRecognizer
from multiprocessing import Process
import pyaudio
import time
import json
from TTS.api import TTS
import numpy as np

## servo motor is connected to GPIO 22 which is pin 15
### Phrases to test
## I feel lonely
## I feel pain
## hello
## How are you doing




def voice_assist():



    listener = sr.Recognizer()
    #engine = pyttsx3.init(driverName="espeak")
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[1].id)
    ##
    #rate = engine.getProperty('rate')
    #engine.setProperty('rate', 125)
    #engine.runAndWait()

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
                           rate=22050,
                           output=True,
                           output_device_index=0,
                           frames_per_buffer=CHUNK)

    model = Model("vosk-model-small-en-us-0.15")
    recognizer = KaldiRecognizer(model, RATE)

    tts = TTS(model_name="tts_models/en/ljspeech/glow-tts")

    def talk(text):
        # engine.say(text)
        # engine.runAndWait()
        raw_list = tts.tts(text=text)
        np_array = np.array(raw_list)
        output_np_array = np_array.astype(np.float32)
        output_byte = output_np_array.tobytes()
        output_stream.write(output_byte)


    def run_alexa():
        import time
        ###======================###
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        ## Motor Hand ##
        servo = 22
        ## Motor Hand ##
        ## Motor Hand ##
        GPIO.setup(servo, GPIO.OUT)
        servo_pwm = GPIO.PWM(servo, 50)
        servo_pwm.start(0)

        data = input_stream.read(CHUNK, exception_on_overflow=False)
        # output_stream.write(data)

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            command = json.loads(str(text))["text"]
            print(text)
            print(command)

            if 'play' in command:
                song = command.replace('play', '')
                talk('playing' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('The current time is ' + time)
                print(time)
            elif 'who is' in command:
                person = command.replace('who is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            elif 'chrome' in command:
                a = 'Opening chrome..'
                #engine.say(a)
                #engine.runAndWait()
                programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                subprocess.Popen([programName])
            elif 'youtube' in command:
                b = 'opening youtube'
                #engine.say(b)
                #engine.runAndWait()
                webbrowser.open('www.youtube.com')
            elif 'joke' in command:
                talk(pyjokes.get_joke())

            elif 'hello' in command:
                servo_pwm.start(3)
                time.sleep(1)
                servo_pwm.start(12)
                talk('Hi there kiddo!')
                time.sleep(1)
                servo_pwm.start(6)

            elif 'how are you doing' in command:
                servo_pwm.start(3)
                talk('I am doing good!')
                servo_pwm.start(12)
                talk(' Thanks for asking!')
                servo_pwm.start(6)
                talk('today is')
                servo_pwm.start(3)
                talk('a great day')
                servo_pwm.start(12)

            elif 'lonely' in command:
                servo_pwm.start(3)
                talk('Aww... dont worry kiddo,')
                servo_pwm.start(12)
                talk('I am here for you.')
                servo_pwm.start(6)
                talk('Everything is going to be alright ')
                servo_pwm.start(3)

            elif 'pain' in command:
                servo_pwm.start(3)
                talk('Ouch...')
                servo_pwm.start(12)
                talk('press on my arms kiddo.')
                servo_pwm.start(6)
                talk('The nurse will come in shortly')
                servo_pwm.start(3)

            elif 'smartest' in command:
                talk(
                    "The smartest person in SP is Tileron Levi Jan Lacang. This bokana is too smart, he is dangerouse to be kept alive")
            elif 'tallest' in command:
                talk(
                    "Technically Naveen Gopalkrishnan comes first runner up in being the tallest. Hoewever Asha Mathyalakan is the first to tallest")
            elif 'bye' in command:
                quit
            else:
                print('START')
                state = 0

    while True:
        run_alexa()
        # try:
        #    run_alexa()
        # except:
        #    "error try again"


if __name__ == '__main__':
    p0 = Process(target=voice_assist)
      #p1 = Process(target=hand_move)
    p0.start()
    time.sleep(2)

    inp = input("Type 'q' and Enter to QUIT:")
    if inp == str('q'):
        p0.terminate()


