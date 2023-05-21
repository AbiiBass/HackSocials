import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import subprocess

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sammy' in command:
                command = command.replace('sammy', '')
                print(command)
                return command
            else:
                command = ""
                return command

    except:
        pass
    # return command


def run_alexa():
    command = take_command()
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
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
    elif 'youtube' in command:
        b = 'opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'hello' in command:
        talk('Hi!')
    elif 'how are you doing' in command:
        talk('I am doing good! Thanks for asking!')
    elif 'i feel lonely' in command:
        talk('Aww... dont worry kiddo, I am here for you. Everything is going to be alright ')
    elif 'pain' in command:
        talk('Ouch...press on my arms kiddo. The nurse will come in shortly')
    elif 'smartest person in sp' in command:
        talk("The smartest person in SP is Tileron Levi Jan Lacang. This bokana is too smart, he is dangerouse to be kept alive")
    elif 'tallest person in sp' in command:
        talk("Technically Naveen Gopalkrishnan comes first runner up in being the tallest. Hoewever Asha Mathyalakan is the first to tallest")
    elif 'bye' in command:
        quit
    else:
        talk('Please say the command again.')


while True:
    try:
        run_alexa()
    except:
        "error try again"