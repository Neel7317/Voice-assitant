
from selenium import webdriver
from News import *
from joke import *
import pyttsx3 as p
import speech_recognition as sr
import randfacts
from weather import *
class infow():
    def __init__(self):
        
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Downloads\\chromedriver_win32\\chromedriver.exe")
    def get_info(self,qry):
        self.qry=qry
        self.driver.get(url="https://www.wikipedia.org/")
        search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(qry)
        enter=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
        enter.click()

    def play(self,qry):
        self.qry=qry
        self.driver.get(url="https://www.youtube.com/results?search_query="+qry)
        enter=self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        enter.click()





engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',150)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    #print(voices)
    engine.runAndWait()

r =sr.Recognizer()

speak('Hello, I am your voice assistent')
speak('Temprature in surat is '+ str(temp())+'and with' +str(des())) 
speak("how are you?")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise=(source,1.2) 
    print("Listening")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("I am also having a good day sir")
speak("what can i do for you")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise=(source,1.2) 
    print("Listening....")
    audio=r.listen(source)
    text2=r.recognize_google(audio)
    print(text2)

if "information" in text2:
    speak("which kind of information do you want to know about?")

    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise=(source,1.2) 
        print("Listening....")
        audio=r.listen(source)
        infor=r.recognize_google(audio)
        speak("Searching {} in wikipedia".format(infor))
    ass=infow()
    ass.get_info(infor)

elif "play" and "video" in text2:   
    speak("you want me to play which video?")

    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise=(source,1.2) 
        print("Listening....")
        audio=r.listen(source)
        vid=r.recognize_google(audio)
        speak("playing {} in youtube".format(vid))
    ass2=infow()
    ass2.play(vid)

elif "news" in text2:
    print("sure sir, Now i read news for you.")   
    speak("sure sir, Now i read news for you.")   
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "jock" or "jocks" in text2:
    speak("sure sir get ready for some chukles")
    l=jokes()
    print(l[0])
    speak(l[0])
    print(l[1])
    speak(l[1])
        
elif "fact" or "facts" in text2:
    speak("sure sir,")
    x=randfacts.getFact()
    print(x)
    speak("Did you know"+x)

