import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening to your BAK BAK")
        recognizer.adjust_for_ambient_noise(source,duration=0.2)
        audio=recognizer.listen(source)
        try:
            print("Smajhne ki koshish")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("ARRE BHAI kuch to BOLO")

def speechtxt(x):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',200)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(x)
    engine.runAndWait()

if __name__=='__main__':

    #if sptext().lower()=="hey assitant":
    while True:
        data1=sptext().lower()

        if "time" in data1:
            time=datetime.datetime.now().strftime("%I%M%p")
            speechtxt(time)

        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")

        elif 'google' in data1:
            webbrowser.open("https://www.google.com/")

        elif "exit" in data1:
            speechtxt("byebyebyeybe")
            break
        
        