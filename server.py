import socket, random, threading

def getstring(): #Denne funksjonen finner random tekst
    tekster = [ #liste over tekster
    "I språkvitenskapen defineres tekst som en helhetlig, sammen hengende, språklig ytring med en bestemt kommunikativ funksjon. En tekst gir uttrykk for en kommunikativ intensjon, som å informere om noe, å oppfordre til handling eller å uttrykke talerens følelser.",
    
    "Videre består den av språklige tegn, som har et innhold og et uttrykk, og formidler på den måten referensielt innhold, det vil si informasjon om en reell, hypotetisk eller fiktiv verden.",

    "Tegnene er uttrykt i en viss modalitet, som skrift eller tale, og i et visst medium, som avis, bok, TV eller internett. Mange tekster inkluderer flere modaliteter, som bilder, musikk eller gestikk, og disse kalles da sammensatte eller multimodale tekster.",

    "Man vet ikke med sikkerhet hvor kakaotreet stammer fra, men vilt voksende arter er funnet i skogene omkring Amazonas og Orinoco i Sør-Amerika.",

    "Det var etter at Kristofer Columbus og HernanCortes kom fra Spania til Mellom-Amerika helt i begynnelsen av 1500-tallet, at man iEuropa for alvor fikk høre om kakao.",

    "Aztekerne i Mexico hadde da gjennom lange tider dyrket kakaotrær, som de trodde hadde guddommelig opprinnelse. Bønnene ble til og med brukt som betalingsmiddel, og de forskjellige provinser betalte en del av sin skatt i form av kakaobønner."
    ]

    return random.choice(tekster) # Gir tilbake en random tekst fra "tekster" variablen

def listen(): #Denne funksjonen lytter etter connectioner til pc-en
    while True: #While løkke slik at den altid lytter
        connection, address = listener.accept() # Lagrer en koneksjon i "connection" variabelen

        connections.append(connection) #Lagrer konneksjonen i connections listen

def matchmaking(): #Funksjon som finner to brukere som kan spille mot hverandre
    while True:
        if len(connections) > 1: #hvis det er flere som har konneksjon
            p1 = random.choice(connections) #tar en random person konneksjon fra listen og lagrer i p1
            connections.remove(p1) #Fjerner personen fra listen
            p2 = random.choice(connections)
            connections.remove(p2)
            thread = threading.Thread(target=lobby,args=(p1,p2)) # Lager en "Thread" som kan kjøre uavhengig av main koden
            thread.start() #Starter Threaden

def lobby(p1,p2): #En lobby hvor to brukere spiller mot hverandre
    string = getstring() #Får en random tekst og lagrer i "string"
    broadcast([p1,p2], [string,string]) #Sender teksten til begge brukerne
    results = recieve([p1,p2]) #Får resultatene til begge brukerne
    broadcast([p1,p2], [results[1],results[0]]) #Sender resultatene til brukerne

def broadcast(participants, messages): #Sender info
    for player in participants: #For løkke med alle brukerne
        player.send(messages[participants.index(player)].encode()) #Sender informasjon til bruker. Infoen er på samme plassering av brukeren i listen

def recieve(participants): #Får information fra "participants"
    messages = [] #Lager en liste slik at jeg kan lagre infoen
    for player in participants:
        messages.append(player.recv(1024).decode()) #Får info fra player og lagrer i "messages"
    return messages #Retunerer listen

connections = [] #liste over folk som er connecta til serveren

IP = "localhost"
PORT = 8888
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Lager en socket
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Setter instillingene
listener.bind((IP, PORT))
listener.listen(0) #Lytter på ipeen og porten

thread1 = threading.Thread(target=listen) 
thread = threading.Thread(target=matchmaking)
thread1.start()
thread.start()
thread.join()
thread1.join()
