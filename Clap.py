# import pyaudio
import sounddevice as sd
import numpy as np
import pyttsx3
import datetime
# from playsound import playsound



hour = int(datetime.datetime.now().hour)


def speak(text):
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


threshold = 0.6
Clap = False


# def jarvis_audio():
#     path = r"D:\\Parween-AI-Assistant\\audio\\start_sound 2.mp3"
#     playsound(path)


def detect_clap(indata,frames,time,status):
    global Clap
    Volume_norm = np.linalg.norm(indata) * 10
    if Volume_norm>threshold:
        # jarvis_audio()
        if hour>=6 and hour<12:
            speak("Good Morning Boss!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon Boss!")    
        elif hour>=0 and hour<6:
            speak("Why are you not sleeping? Boss!")    
        else:
            speak("Good Evening Boss!")    
        Clap = True
        
def Listen_for_claps():
    with sd.InputStream(callback=detect_clap):
        return sd.sleep(1000)    
    
def MainClapExe():   
# if __name__ == "__main__":
    while True:
       Listen_for_claps()
       if Clap == True:
           break
       else:
           pass  
       
# def get_voice_ids():
#     engine = pyttsx3.init()

#     # Get the list of available voices
#     voices = engine.getProperty('voices')

#     print("Available Voices:")
#     for idx, voice in enumerate(voices):
#         print(f"{idx + 1}. ID: {voice.id}, Name: {voice.name}")

#     engine.stop()

# # Run the function to get voice IDs
# get_voice_ids()
                  
       
# jarvis_audio()         