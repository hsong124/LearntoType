from google.cloud import texttospeech
import os
import pygame
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/Heather/Desktop/LearnToType/LTTKey.json'





#set up speech to text api
client = texttospeech.TextToSpeechClient()
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

userInput = ("Key Z is directly under key A, so slide your left pinky down one key to press Z.")
'''("Hi. Welcome to learning to type. This application is meant to help you learn to type."
            "Find the j key with your right index finger."
            "It should have a little bump on most keyboards and is located in the third to bottom row"
            "and six from the right. The rest of your right hand fingers should rest on the following keys to the right."
            "Find the F key with your left index finger. It is on the same row as the j key and three keys to the left of the j key."
            "It should also have a bump and the following left hand fingers should rest as expected."
            "The enter key is on the same row as J and F all the way to the right. After typing a key, press enter to receive feedback."
            "Try pressing j with your right index finger and then enter with your right pinkie now.")
'''

synthesis_input = texttospeech.types.SynthesisInput(text=userInput)
response = client.synthesize_speech(synthesis_input, voice, audio_config)
with open("introZ" + '.mp3', 'wb') as out:
    out.write(response.audio_content)
