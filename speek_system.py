import speech_recognition as sr
import pyttsx3 as ttx

# ======================================================================================================================
# CONSTRUCTEUR DE LA CLASSE [A COMPLETER PLUS TARD]
# ======================================================================================================================
class SpeekSystem:
    def __init__(self):
        self.listener = sr.Recognizer()
        self.engine = ttx.init()
        self.voice = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voice[1].id)

    # ======================================================================================================================
    # FONCTION ECOUTER [A COMPLETER PLUS TARD]
    # ======================================================================================================================
    def ecouter(self):
        try:
            with sr.Microphone() as source:
                print("Parler Maintenant")
                voix = self.listener.listen(source)
                command = self.listener.recognize_google(voix)
                print(command)

        except:
            pass

    # ======================================================================================================================
    # FONCTION PARLER [A COMPLETER PLUS TARD]
    # ======================================================================================================================
    def parler(self, text_to_say):
        try:
            self.engine.say(text_to_say)
            self.engine.runAndWait()

        except:
            pass
