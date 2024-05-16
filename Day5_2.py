# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 09:20:16 2021

@author: kelka
"""

import speech_recognition as sr


r = sr.Recognizer()



with sr.AudioFile('C:/Users/kelka/Documents/Internship_Python/Vedant_audio.wav.wav') as audio:
    audio_text = r.listen(audio)

    try:

        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)

    except:
        print('Sorry.. run again...')