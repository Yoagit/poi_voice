import pyttsx3
import b_parse
import locale
import speech_recognition as sr  

locale.setlocale(locale.LC_TIME,'')
engine = pyttsx3.init()
val = 'init'
r  = sr.Recognizer()

while b_parse.nostop(val):
    with sr.Microphone() as source:
        print("Dites quelque chose")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="fr-FR")
        print("Vous avez dit : " + text)
        val = b_parse.parse_sentect(text)
        engine.say(val)
        print(val)
        engine.runAndWait()
    except sr.UnknownValueError:
        engine.say("Je n'ai pas compris")
        engine.runAndWait()
    except sr.RequestError as e:
        engine.say("Le service Google Speech API ne fonctionne plus")
        print("Le service Google Speech API ne fonctionne plus" + format(e))
