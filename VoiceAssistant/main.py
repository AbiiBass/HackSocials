from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys

recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)
voice = speaker.getProperty('voices')
speaker.setProperty('voice', voice[1].id)



def greetings():
    global recognizer
    speaker.say("Hello there kiddo, whatsup")
    speaker.runAndWait()

def support():
    global recognizer
    speaker.say("Aww don't worry kiddo, I'm here for you")
    speaker.runAndWait()

def die():
    global recognizer
    speaker.say("Let's cry together boo... hoo... hoo... hoo")
    speaker.runAndWait()

def quit():
    speaker.say("Bye")
    speaker.runAndWait()
    sys.exit(0)

mappings = {
    "greetings": greetings,
     "support": support,
    "die": die,
    "exit": quit
}

assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()

        assistant.request(message)
    except:
        recognizer = speech_recognition.Recognizer()
