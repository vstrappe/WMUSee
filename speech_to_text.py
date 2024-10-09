import speech_recognition as sr
import pyttsx3
from speech_recognition import google

recognizer = sr.Recognizer()

def record():
    while True:
        try:
            with sr.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, 0.1)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                newText = text.capitalize()
                newText += ". \n"
                return newText
                
        except sr.RequestError as e:
            print("Could not request results: " + e)

        except sr.UnknownValueError as e:
            print("Unknown value error")

def fileOutput(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

def listen():
    while True:
        text = record()
        return text
