#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
import os
from gtts import gTTS
import os
 
# speech to text
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio))
    text = r.recognize_google(audio)
    os.system(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


# now text to speech

tts = gTTS(text=r.recognize_google(audio),lang="en")
# to save audio file in hello.mp3 at the same location as that of this file
tts.save("hello1.mp3")
# starting the audio file using mpg321 driver
os.system("mpg321 hello1.mp3")
