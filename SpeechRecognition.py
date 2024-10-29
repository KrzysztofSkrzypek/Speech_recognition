import speech_recognition as  sr

recognizer = sr.Recognizer()

with sr.AudioFile("test_menz.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language="pl-PL")
    print("rozpoznawany tekst: ", text)
except sr.UnknownValueError:
    print("nie rozpoznano dzwieku.")
except sr.RequestError as  e:
    print(f"blad w  komunikacji z API: {e}")
