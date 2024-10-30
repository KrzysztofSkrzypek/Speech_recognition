import speech_recognition as  sr
import pyaudio
import wave
import keyboard

#parametry nagrywania
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 7
OUTPUT_FILENAME = "password.wav"
main_pass = "abrakadabra"

#Nagrywanie
def record_audio():
    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                        input=True, frames_per_buffer=CHUNK)
    print("Nagrywanie.. Nacisnij 's', aby zatrzymać.")
    frames=[]
    while True:
        data = stream.read(CHUNK)
        frames.append(data)
        if keyboard.is_pressed('s'):
            print("Nagrywanie zakończone.")
            break
    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
print('Nacisniej 'r', aby rozpoczac nagrywanie...')
keyboard.wait('r')
record_audio()


recognizer = sr.Recognizer()

with sr.AudioFile("password.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language="pl-PL")
    if main_pass in text:
        print(text)
        print("HASLO PRAWIDLOWE")
    else:
        print("HASLO NIEPRAWIDLOWE")
except sr.UnknownValueError:
    print("nie rozpoznano dzwieku.")
except sr.RequestError as  e:
    print(f"blad w  komunikacji z API: {e}")
