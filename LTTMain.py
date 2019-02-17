"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
import os
import pygame
import time
from random import randint

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/Heather/Desktop/LearnToType/LTTKey.json'

words = ("apples babies balls beds bears boys bells birds brothers boats giants"
        " dinosaurs cakes cars cats children corn chairs chickens cows dogs wind"
        " dolls frogs ducks eggs eyes snails waves lizards feet clouds fish trains"
        " flowers pets books girls snakes grass pies hands pizzas oranges bikes "
        "horses houses kittens legs letters ants men tomatoes money teeth mice "
        "friends spiders pigs rabbits rain rings clocks fairies planes songs sheep"
        " shoes sisters trees plants trucks sticks sun toys things creep crawl walk run jump "
        "skip hop slither climb dig squirm fly sit stalk stomp tiptoe gallop blow dance glide "
        "swim wash play throw drink eat chew sing shout growl bark buzz laugh smile cry "
        "go moo quack talk yell scream screech squawk squeal glow listen paint look read knit "
        "sleep draw shine watch kick dive find build work explore shop clean catch shake ").split()





def learnLetter(letter, originalReq):
    learning = True
    count = 0
    while learning:
        if count % 5 == 4:
            pygame.mixer.music.load(originalReq)
            pygame.mixer.music.play()
            time.sleep(8)
        userInput = input()
        if userInput == "quit":
            return "quit"
        elif userInput == "free":
            return "free"
        elif userInput == "skip":
            return "skip"
        speechOutput = "you pressed " + userInput
        for char in userInput:
            pygame.mixer.music.load("letterAudio/" + char + ".mp3")
            pygame.mixer.music.play()
            time.sleep(1)
        if userInput == letter:
            learning = False
        else:
            pygame.mixer.music.load("sorry.mp3")
            pygame.mixer.music.play()
            time.sleep(1.5)
        count += 1
    pygame.mixer.music.load("gj.mp3")
    pygame.mixer.music.play()
    time.sleep(1)
    return letter

'''synthesis_input = texttospeech.types.SynthesisInput(text=userInput)
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    with open("userInput" + '.mp3', 'wb') as out:
        out.write(response.audio_content)'''
def skip():
    learning = True
    count = 0
    while learning:
        index = randint(0,139)
        desired = words[index]
        study = True
        synthesis_input = texttospeech.types.SynthesisInput(text="Please type the word " + desired)
        response = client.synthesize_speech(synthesis_input, voice, audio_config)
        with open("desired" + '.mp3', 'wb') as out:
            out.write(response.audio_content)
        pygame.mixer.music.load("desired.mp3")
        pygame.mixer.music.play()
        time.sleep(2)
        while study:
            userInput = input()
            if userInput == "quit":
                study = False
                learning = False
                return "quit"
            elif userInput == "free":
                study = False
                learning = False
                return "free"
            elif userInput == "alpha":
                study = False
                learning = False
                return "alpha"
            else:
                speech = "You typed " + userInput
                synthesis_input = texttospeech.types.SynthesisInput(text=speech)
                response = client.synthesize_speech(synthesis_input, voice, audio_config)
                with open("speech" + '.mp3', 'wb') as out:
                    out.write(response.audio_content)
                pygame.mixer.music.load("speech.mp3")
                pygame.mixer.music.play()
                timeLength = 1.5 + .5 *len(userInput.split())
                time.sleep(timeLength)
                if userInput == desired:
                    pygame.mixer.music.load("gj.mp3")
                    pygame.mixer.music.play()
                    time.sleep(1)
                    study = False
                else:
                    pygame.mixer.music.load("sorry.mp3")
                    pygame.mixer.music.play()
                    time.sleep(1.8)
                if count % 5 == 4:
                    pygame.mixer.music.load("desired.mp3")
                    pygame.mixer.music.play()
                    time.sleep(3)
                count += 1

def free():
    study = True
    while study:
        userInput = input()
        if userInput == "quit":
            study = False
            return "quit"
        elif userInput == "alpha":
            study = False
            return "alpha"
        elif userInput == "skip":
            study = False
            return "skip"
        else:
            speech = "You typed " + userInput
            synthesis_input = texttospeech.types.SynthesisInput(text=speech)
            response = client.synthesize_speech(synthesis_input, voice, audio_config)
            timeLength = 1.5 + .5 *len(userInput.split())
            with open("speech" + '.mp3', 'wb') as out:
                out.write(response.audio_content)
            pygame.mixer.music.load("speech.mp3")
            pygame.mixer.music.play()
            time.sleep(timeLength)
            pygame.mixer.music.load("sorry.mp3")


def alphaJ():
    pygame.mixer.music.load("letter tutorials/intro.mp3")
    pygame.mixer.music.play()
    return learnLetter("j", "letter tutorials/intro.mp3")

def alpha(letter):
    pygame.mixer.music.load("letter tutorials/intro" + letter + ".mp3")
    pygame.mixer.music.play()
    time.sleep(8)
    return learnLetter(letter, "intro" + letter + ".mp3")


#####################################################################################
alphaOrder = {"j":"f","f":"d","d":"k","k":"l","l":"s","s":"a","a":"g","g":"h","h":"u","u":"y","y":"r","r":"t","t":"e","e":"i","i":"o","o":"w","w":"q","q":"p","p":"m","m":"n","n":"v","v":"b","b":"c","c":"x","x":"z"}

client = texttospeech.TextToSpeechClient()
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

pygame.mixer.init()
pygame.mixer.music.load("letter tutorials/introSkip.mp3")
pygame.mixer.music.play()
start = input()
quit = False
count = 0
while not quit:
    if start == "free":
        start = free()
        count = 0
    elif start == "skip":
        start = skip()
        count = 0
    else:
        if count == 0:
            start = alphaJ()
            count += 1
        else:
            start = alpha(alphaOrder[start])
    if start == "quit":
        quit = True
pygame.mixer.init()
pygame.mixer.music.load("bye.mp3")
pygame.mixer.music.play()
time.sleep(2)

