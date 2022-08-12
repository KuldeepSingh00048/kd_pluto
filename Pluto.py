import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyttsx3
from tkinter import *
from facial_recogntion_part_2 import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good..morning..sir!")

    elif 12 <= hour < 18:
        speak("good..afternoon..sir!")

    else:
        speak("good..evening..sir!")

    speak("i..am..pluto........made..by...kuldeep...ajeet...ajay..sir...as..i..get..eliminated..from..your..solar"
          "..system"
          "..by..the..scientist..of..nasa....because..i..am..very..far...from..the..sun!!!!"
          "so..they..bring..back..me..in..the..form..of..Artificial...intelligence.."
          "...what..can..i..do..for..u"
          "..any..help..you "
          "..want..from..me..from..above..option...than..please..tell..me"
          "...u..can..speak..i..am..Listening..u...")
#############################################################################################
def music():                                                                                #
    r =sr.Recognizer()                                                                      #
    with sr.Microphone()as source:                                                          #
        print("Please tell me the song name sir ")                                          #
        speak("Please tell me the song name sir ")                                          #
        r.pause_threshold = 1                                                               #
        audio = r.listen(source)                                                            #
    try:                                                                                    #          music() function
        print("wait a second sir for result : ")                                            #
        speak("wait..a..second..sir..for..result : ")                                       #
        musicname = r.recognize_google(audio, language='en-in')                             #
    except:                                                                                 #
        speak("sorry say that again please..")                                              #
        return "None"                                                                       #
    return musicname                                                                        #
#############################################################################################
                                                                                            #
def wakeup():                                                                               #
    # It takes microphone input from the user and returns string output                     #
    r = sr.Recognizer()                                                                     #
    with sr.Microphone() as source:                                                         #
        print("listening...")                                                               #
                                                                                            #
        r.pause_threshold = 1                                                               #
        audio = r.listen(source)                                                            #   wakeup function()
                                                                                            #
    try:                                                                                    #
        print("Recognizing...")                                                             #
        text = r.recognize_google(audio, language='en-in')                                  #
    except Exception as e:                                                                  #
        # print(e)                                                                          #
        speak("pluto..can..not..able..to..hear..your..voice......please..speak..clear")     #
        return "None"                                                                       #
    return text                                                                             #
#############################################################################################
def on_google():                                                                    #
    r =sr.Recognizer()                                                              #
    with sr.Microphone()as source:                                                  #
        print("please just tell the word or line that u want to search about...")   #
        r.pause_threshold = 1                                                       #
        audio = r.listen(source)                                                    #
    try:                                                                            #            on_google function()
        print("wait a second sir for result : ")                                    #
        word = r.recognize_google(audio, language='en-in')                          #
    except:                                                                         #
        speak("sorry say that again please..")                                      #
        return "None"                                                               #
    return word                                                                     #
#####################################################################################
def takeCommand():                                                        #
    # It takes microphone input from the user and returns string output   #
    r = sr.Recognizer()                                                   #
    with sr.Microphone() as source:                                       #
        print("listening...")                                             #
        r.pause_threshold = 1                                             #
        audio = r.listen(source)                                          #
                                                                          #
    try:                                                                  #
        print("Recognizing...")                                           #
        query = r.recognize_google(audio, language='en-in')               #                      takeCommand function()
        print(f"User said: {query}\n")                                    #
                                                                          #
    except Exception as e:                                                #
        # print(e)                                                        #
        speak("Say that again please...")                                 #
        return "None"                                                     #
    return query                                                          #
###########################################################################
if __name__ == "__main__":
    speak("sir..please..let..me..verify..you..for..security..purpose ")
    fr2()
    print("      1.Google                                2.Chrome")
    print("      3.Youtube                               3.Wikipedia")
    print("      5.G-mail                                6.Twitter")
    print("      7.Telegram                              8.Time")
    print("      9.Whatsapp                             10.Instagram ")
    print("     11.u want to open python code           12.Listen a song")
    print("     13.Tic Tac Toe                          14.calculator")
    print("     15.You want to write a notes            16.u want to search something on google ")
    print(" ")
    print(" ")
    print("If you want to open this above things than u have to wake up the pluto...")
    print(" ")
    print("speak 'wake up pluto'..")
    wishMe()
    while True:
            while True:
                # if 1:
                query = takeCommand().lower()

                # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                elif 'no help' in query or 'koi help nahi chahiye' in query:
                    speak(
                        "no problem..sir.....but..any..help..u..want..then..please..wakeup..me...because..i..am..going"
                        "..to..sleep..as..u..don't..need..any..help")
                    speak("and..thank..u..for..using..me..in..the..form..of...artificial..intelligence!!!")
                    print("and..thank..u..for..using..me..in..the..form..of...artificial..intelligence!!!")
                    print("...for waking up pluto u have to rerun this program!!!!")
                    exit()
                elif 'open youtube' in query or 'youtube open' in query:
                    webbrowser.open("youtube.com")

                elif 'open whatsapp' in query or 'whatsapp open' in query:
                    webbrowser.open("whatsapp.com")

                elif 'open instagram' in query or 'instagram open' in query:
                    webbrowser.open("instagram.com")

                elif 'open google' in query or 'google open' in query:
                    webbrowser.open("google.com")

                elif 'the time' in query or 'time kya' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif 'open gmail' in query or 'gmail open' in query:
                    webbrowser.open("gmail.com")

                elif 'open twitter' in query or 'twitter open' in query:
                    webbrowser.open("twitter.com")

                elif 'open telegram' in query or 'telegram open ' in query:
                    webbrowser.open("telegram.com")

                elif 'open chrome' in query or 'chrome open ' in query:
                    webbrowser.open("chrome.com")

                elif 'calculator' in query:
                    def btnClick(numbers):
                        global operator
                        operator = operator + str(numbers)
                        text_Input.set(operator)


                    def btnClearDisplay():
                        global operator
                        operator = ""
                        text_Input.set("")


                    def btnEqualsInput():
                        global operator
                        sumup = str(eval(operator))
                        text_Input.set(sumup)
                        operator = ""


                    cal = Tk()
                    cal.title("calculator")
                    operator = ""
                    text_Input = StringVar()

                    txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=15, insertwidth=4,
                                       bg="darkgray", justify='right').grid(columnspan=4)

                    btn7 = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                  text="7", bg="slategray", command=lambda: btnClick(7)).grid(row=1, column=0)

                    btn8 = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                  text="8", bg="slategray", command=lambda: btnClick(8)).grid(row=1, column=1)

                    btn9 = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                  text="9", bg="slategray", command=lambda: btnClick(9)).grid(row=1, column=2)

                    Addition = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                      text="+", bg="darkslategray", command=lambda: btnClick("+")).grid(row=1, column=3)
                    # =======================================================================================

                    btn4 = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                  text="4", bg="slategray", command=lambda: btnClick(4)).grid(row=2, column=0)

                    btn5 = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                  text="5", bg="slategray", command=lambda: btnClick(5)).grid(row=2, column=1)

                    btn6 = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                  text="6", bg="slategray", command=lambda: btnClick(6)).grid(row=2, column=2)

                    Subtraction = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                         text="-", bg="darkslategray", command=lambda: btnClick("-")).grid(row=2,
                                                                                                           column=3)

                    # =======================================================================================

                    btn1 = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                  text="1", bg="slategray", command=lambda: btnClick(1)).grid(row=3, column=0)

                    btn2 = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                  text="2", bg="slategray", command=lambda: btnClick(2)).grid(row=3, column=1)

                    btn3 = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                  text="3", bg="slategray", command=lambda: btnClick(3)).grid(row=3, column=2)

                    Multiply = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                      text="*", bg="darkslategray", command=lambda: btnClick("*")).grid(row=3, column=3)

                    # =======================================================================================

                    btn0 = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                  text="0", bg="slategray", command=lambda: btnClick(0)).grid(row=4, column=0)

                    btnClear = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                      text="C", bg="red", command=btnClearDisplay).grid(row=4, column=1)

                    btn = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                 text=".", bg="slategray", command=lambda: btnClick(".")).grid(row=4, column=2)

                    Division = Button(cal, padx=16, pady=16, bd=8, fg="white", font=('arial', 20, 'bold'),
                                      text="/", bg="darkslategray", command=lambda: btnClick("/")).grid(row=4, column=3)

                    btnEquals = Button(cal, bd=16, width=17, fg="white", font=('arial', 20, 'bold'),
                                       text="=", bg="slategray", command=btnEqualsInput).grid(row=5, columnspan=4)

                    cal.mainloop()

                elif 'tic tac toe' in query:
                    def callback(r, c):
                        global player

                        if player == '#' and states[r][c] == 0 and stop_game == False:
                            b[r][c].configure(text='#', fg='red', bg='blue')
                            states[r][c] = '#'
                            player = 'O'
                        if player == 'O' and states[r][c] == 0 and stop_game == False:
                            b[r][c].configure(text='O', fg='yellow', bg='green')
                            states[r][c] = 'O'
                            player = '#'
                        check_for_winner()


                    def check_for_winner():
                        global stop_game
                        for i in range(3):
                            if states[i][0] == states[1][i] == states[2][i] != 0:
                                b[i][0].configure(bg='grey')
                                b[i][1].configure(bg='grey')
                                b[i][2].configure(bg='grey')
                                stop_game = True

                        for i in range(3):
                            if states[0][i] == states[1][i] == states[i][2] != 0:
                                b[0][0].configure(bg='grey')
                                b[1][i].configure(bg='grey')
                                b[2][i].configure(bg='grey')
                                stop_game = True

                            if states[0][0] == states == [1][1] == states[2][2] != 0:
                                b[0][0].configure(bg='grey')
                                b[1][1].configure(bg='grey')
                                b[2][2].configure(bg='grey')
                                stop_game = True
                            if states[2][0] == states == [1][1] == states[0][2] != 0:
                                b[2][0].configure(bg='grey')
                                b[1][1].configure(bg='grey')
                                b[0][2].configure(bg='grey')
                                stop_game = True


                    root = Tk()
                    root.title("TIC TAC TOE *ajay")
                    b = [[0, 0, 0, ],
                         [0, 0, 0, ],
                         [0, 0, 0, ]]
                    states = [[0, 0, 0, ],
                              [0, 0, 0, ],
                              [0, 0, 0, ]]
                    for i in range(3):
                        for j in range(3):
                            b[i][j] = Button(font=("Arial", 50), width=5, bg='white',
                                             command=lambda r=i, c=j: callback(r, c))
                            b[i][j].grid(row=i, column=j)
                    player = '#'
                    stop_game = False

                    mainloop()
                elif 'on google' in query:
                    while True:
                        word = on_google().lower()
                        link = "https://www.google.com/search?q="
                        url = link+word
                        webbrowser.open(url)
                        print("you want to search more on google")
                        word = on_google().lower()
                        if 'no' in word:
                            break
                    break

                elif 'open python code' in query or ' python code open' in query:
                    codePath = "C:\\Users\\THE KULDEEP SINGH\\AppData\\Roaming\\Microsoft\\Windows\\Start " \
                               "Menu\\Programs\\Python 3.7\\IDLE (Python 3.7 64-bit).lnk "
                    os.startfile(codePath)
                elif 'want to write a note' in query or ' note likhna hai' in query:
                    codePath = "C:\\Users\\THE KULDEEP SINGH\\AppData\\Roaming\\Microsoft\\Windows\\Start " \
                               "Menu\\Programs\\Python 3.7\\IDLE (Python 3.7 64-bit).lnk "
                    os.startfile(codePath)
                elif 'play music' in query or  'music play karo' in query:
                    while True:
                        musicname=music().lower()
                        codePath = "C:\\Users\\THE KULDEEP SINGH\\AppData\\Roaming\\Microsoft\\Windows\\Start " \
                               "Menu\\Programs\\Python 3.7\\IDLE (Python 3.7 64-bit).lnk "
                        playmusic = codePath+musicname
                        os.startfile(playmusic)
                        print("U want to listen more music....")
                        musicname=music().lower()
                        if 'no' in musicname or 'nahi' in musicname:
                            break
                    break

