import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random
import numpy as np
import pyttsx3
import subprocess
from Clap import MainClapExe


chatStr = ""
# ! https://youtu.be/Z3ZAJoi4x6Q
vlc = 'C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe'
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Boss: {query}\n Parween: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    try:
        text += response["choices"][0]["text"]
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
        with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
            f.write(text)
    except:
        say("Some Error Occurred. Sorry from Parween")            

def say(text):
    engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    Id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    # Id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_MarkM"
    engine.setProperty('voice',Id)
    print("")
    print(f"==> Parween AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Parween"


def play_random_music():
    music_dir = 'D:\\Parween-AI-Assistant\\music'
    songs = [song for song in os.listdir(music_dir) if song.endswith('.mp3')]
    if songs:
        random_song = random.choice(songs)
        say(f"Playing {random_song}")

        # Use subprocess to open the file with Windows Media Player
        music_path = os.path.join(music_dir, random_song)
        subprocess.Popen([vlc, music_path], shell=True)
    else:
        say("No music files found in the directory.")  
        
def play_random_movie():
    movie_dir = 'D:\\Files For Normal use\\Movie\\Harry Potter' 
    movies = [movie for movie in os.listdir(movie_dir) if movie.endswith('.mkv')]   
    if movies:
        random_movie = random.choice(movies)
        say(f"Playing {random_movie}")
        movie_path = os.path.join(movie_dir, random_movie)
        subprocess.Popen([vlc, movie_path], shell=True)
    else:
        say("No movie files found in the directory.")               
def mainExecution():
    if __name__ == '__main__':
        print('Welcome to Pareen AI')
        say("Welcome to Parween AI")
        while True:
            print("Listening...")
            query = takeCommand()
            # todo: Add more sites
            sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
            for site in sites:
                if f"Open {site[0]}".lower() in query.lower():
                    say(f"Opening {site[0]} sir...")
                    webbrowser.open(site[1])
            # todo: Add a feature to play a specific song
            if "music" in query:
                play_random_music()

            elif "the time" in query:
                hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                say(f"Sir time is {hour} bajke {min} minutes")
            elif "movie" in query:
                play_random_movie()            

            elif "open facetime".lower() in query.lower():
                os.system(f"open /System/Applications/FaceTime.app")

            elif "open pass".lower() in query.lower():
                os.system(f"open /Applications/Passky.app")

            elif "Using artificial intelligence".lower() in query.lower():
                ai(prompt=query)

            elif "Quit".lower() in query.lower():
                exit()
            elif "Exit".lower() in query.lower():
                exit()
            elif "Bhag".lower() in query.lower():
                exit()

            elif "reset chat".lower() in query.lower():
                chatStr = ""

            else:
                print("Chatting...")
                chat(query)
                
MainClapExe()              
say("Please Speak The Password.")
while True:
    print("Listening....")
    query = takeCommand()
    if "Start The Programming".lower() in query.lower():
        print("Password Matched. Boss!")
        say("Password Matched. Boss!")
        mainExecution()
    else:
        print("Password Not Matched. Boss!")       
        say("Password Not Matched. Boss!")       
    break
    
    