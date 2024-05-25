import socket, TypingTest, time, os

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #lager en socket

print("Velkommen til BATTLETYPER") #Printer velkommen tekst
time.sleep(2)
os.system("cls") #Fjerner tekst fra terminal

IP = "xxx.xxx.xxx"
PORT = 8888
connection.connect((IP, PORT)) #Prøver å connecte til ipeen og porten
print("Matchmaking") #Venter på info fra serveren

tekst = connection.recv(1024).decode() #Får informasjon fra konneksjonen og lagrer i "tekst"
os.system("cls")

bt = TypingTest.Speedtest(tekst) #Initierer classen

for i in range(3,0,-1): #Teller ned fra 3 til 1
    print(f"Starting in: {i}")
    time.sleep(1)
    os.system("cls")

result = bt.start() #Starter spillet og lager resultatet i "result"

connection.send(result.encode()) #Sender resultatet

print("Waiting for the other player")
p2_result = connection.recv(1024).decode() #Får resultatet til motstander
os.system("cls")

print("YOU: " + result + "\nTHEM: " + p2_result) #Printer resultatene
time.sleep(5) #Gir deg tid til å se resultatene
os._exit(0) #Går ut av programmet
