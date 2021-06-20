import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


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
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'how are you' in command:
        talk('I am fine.Take precautions for corona.')
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'made' in command:
        talk('Sharvari is my creator')
    elif 'do you like me' in command:
        talk('Yes you are good soul')
    elif'thank you' in command:
        talk('Welcome dear.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'father day' in command:
        talk('Fathers day is on Twenty June')
    elif 'gift idea' in command:
        talk('You can give a hug to your father and just say i love you')
    elif 'bye' in command:
        talk('Ok, bye see you again.')
    else:
        talk('Please repeat the command again. ')

while True:
    run_alexa()


