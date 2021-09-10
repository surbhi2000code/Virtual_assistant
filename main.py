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


def talk():
    engine.say('T am your alexa')
    engine.say('What can I do for you')
    engine.runAndWait()
talk()

def talk_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Alexa' in command:
                command = command.replace('Alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = talk_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M ')
        print(time)
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what is' in command:
        thing = command.replace('what is', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('Sorry! I have headache')

    elif 'are you single' in command:
        talk('Sorry!I am already committed')

    elif 'jokes' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    else:
        talk('Sorry! Not able to recognize your command')

while True:
    run_alexa()