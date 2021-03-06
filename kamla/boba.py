import pyttsx3
import datetime

# Initialize pyttsx3
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak(f"{date}")
    speak(f"{month}")
    speak(f"{year}")


def greetings():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Hiramon, I think you are having a beautiful morning!")
    elif hour >= 12 and hour <= 18:
        speak("Hiramon, I think you are having a beautiful evening!")
    elif hour >= 18 and hour <= 24:
        speak("Hiramon, I think you are having beautiful night!")
    speak("The time is")
    time()
    speak("And date is")
    date()
    speak("Hiramon, i am at your service. So, tell me how can i help you?")


if __name__ == "__main__":
    greetings()