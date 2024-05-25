import os, threading, time
from pynput import keyboard
from colorama import Fore

class Speedtest():
    
    def __init__(self, string): #Initierer classe variablene
        self.listener = keyboard.Listener(on_press=lambda event: self.process_press(event)) #initierer keyboard bibloteket
        self.tim = 1 #Tid variabel
        self.fails = 0 #Fail variabel
        self.answer = string #Progresjon variabel
        self.string = string #Orginal tekst variabel
        self.wps = 0 #Hvor mange ord du har tastet

    def start(self): #Starter spillet
        print(self.answer)
        self.listener.start() #Lytter på keyboardet og kjører spillet
        self.listener.join() #Når den er ferdig så går den videre
        return self.result

        
    def process_press(self, keypress):
        os.system("cls") #Clearer terminalen
        if self.wps == 1: #hvis du har startet og skrive
            thread = threading.Thread(target=self.timer) #Lager thread
            thread.start() #Starter thread

        try: #Prøver om keyprss kan være .char som er character eller bokstav
            current_key = keypress.char 
        except AttributeError: #Hvis det er noe annet en bokstav
            if str(keypress) == "Key.space": #Om det er space
                current_key = " "
            else:  #Hvis ikke så er current key noe
                current_key = "noe"

        self.check_progress(current_key) #Sjekker progresjon og printer progresjon
        
        arrow= ""
        for i in range(len(self.string.replace(self.answer, ''))-1): #Sjekker hvor i setningen pilen skal være
            arrow+=" " #plusser på en space for hvor mye lengre det er
        arrow+="^"

        green_text = f"{Fore.GREEN + self.string.replace(self.answer, '')}" #Lager grønn progresjon
        white_text = f"{Fore.WHITE + self.answer}\n" #Lager hvit tekst
        arrow = f"{Fore.GREEN + arrow + Fore.WHITE}\n" #Lager grønn pil
        WPM = f"WPM:{self.wps/self.tim}" #Lager Words per second tskt

        print(green_text + white_text + arrow + WPM) #Printer progresjonen

    def check_progress(self, keypress): #Sjekker progresjon og printer progresjon
        if keypress == self.answer[0]: #Sjekker om keypress er riktig bokstav i setningen
            self.answer = self.answer[1:] #Tar vekk første bokstav
            self.wps += 1 #Plusser på en på antall klikk
        elif keypress != "noe": #Hvis keypress er en bokstav og feil
            self.fails+=1 
        if not self.answer: #Hvis du har fullført setningen da er self.answer ""
            self.result = "Fails: "+str(self.fails)+" | Time: "+str(self.tim) #Lagrer resultatet
            self.listener.stop() #Stopper keyboard listeneren

    def timer(self): #Timer 
        while True:
            time.sleep(1)
            self.tim+=1
