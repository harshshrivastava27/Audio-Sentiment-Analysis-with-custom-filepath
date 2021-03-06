# -*- coding: utf-8 -*-
"""audiosentiment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PkH-K1flUqci5UtMOw1L_I40fHry0RWA
"""

!pip install pydub
!pip install SpeechRecognition
!pip install ffmpeg
!pip install nltk
import nltk
nltk.download("punkt")
nltk.download("vader_lexicon")

!pip install flair

from pydub import AudioSegment
import speech_recognition as sr


def convert_to_wav(filename):


  """conversion to .wav"""
  # Import audio file
  audio = AudioSegment.from_file(filename)


  # Create new filename
  new_filename = filename.split(".")[0] + ".wav"


  # Export file as .wav
  audio.export(new_filename, format='wav')
  print(f"Converting {filename} to {new_filename}...")

def show_pydub_stats(filename):
  
  """Returns different audio attributes related to an audio file."""
  # Create AudioSegment instance
  audio_segment = AudioSegment.from_file(filename)


  # Print audio attributes and return AudioSegment instance
  print(f"Channels: {audio_segment.channels}")
  print(f"Sample width: {audio_segment.sample_width}")
  print(f"Frame rate (sample rate): {audio_segment.frame_rate}")
  print(f"Frame width: {audio_segment.frame_width}")
  print(f"Length (ms): {len(audio_segment)}")
  return audio_segment

def transcribe_audio(filename):

  """Takes a .wav format audio file and transcribes it to text."""
  # Setup a recognizer instance
  recognizer = sr.Recognizer()


  # Import the audio file and convert to audio data
  audio_file = sr.AudioFile(filename)
  with audio_file as source:
   audio_data = recognizer.record(source)


  # Return the transcribed text
  return recognizer.recognize_google(audio_data)

#from nltk.sentiment.vader import SentimentIntensityAnalyzer


#sid = SentimentIntensityAnalyzer()
import flair


filename = '/content/drive/MyDrive/audiosentiment/output10.mp3'
new_name = '/content/drive/MyDrive/audiosentiment/output10.wav'


convert_to_wav(filename)


trans_text = transcribe_audio(new_name)
print(trans_text)
flair_sentiment = flair.models.TextClassifier.load('en-sentiment')
s = flair.data.Sentence(trans_text)
flair_sentiment.predict(s)
total_sentiment = s.labels
total_sentiment
#print(sid.polarity_scores(trans_text))

import pickle

pickle.dump(flair_sentiment, open('model.pkl','wb'))

import sys
import os

user_input = input("Enter the path of your file: ")

assert os.path.exists(user_input), "Could not find the file at, "+str(user_input)
f = open(user_input,'rb')
print("File exists!")
filename=user_input
new_name = '/content/drive/MyDrive/audiosentiment/output10.wav'
convert_to_wav(filename)


trans_text = transcribe_audio(new_name)
print(trans_text)
flair_sentiment = flair.models.TextClassifier.load('en-sentiment')
s = flair.data.Sentence(trans_text)
flair_sentiment.predict(s)
total_sentiment = s.labels
total_sentiment





























