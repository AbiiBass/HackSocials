import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noises...Please wait')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything...')
        recordedaudio=recognizer.listen(source)

    try:
        command=recognizer.recognize_google(recordedaudio,language="en_US")
        command=command.lower()
        print("Your message:", format(command))

    except Exception as ex:
        print(ex)

    if 'chrome' in command:
        a = 'Opening chrome..'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    if 'play' in command:
        a = 'opening youtube..'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(command)
    if 'youtube' in command:
        b = 'opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')

while True:
    cmd()
