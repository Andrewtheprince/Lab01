from random import randint

class Domanda:
    def __init__(self, domanda, difficolta, risposta_giusta, risposta_sbagliata1, risposta_sbagliata2, risposta_sbagliata3):
        self.domanda = domanda
        self.difficolta = difficolta
        self.rispostaGiusta = risposta_giusta
        self.rispostaSbagliata1 = risposta_sbagliata1
        self.rispostaSbagliata2 = risposta_sbagliata2
        self.rispostaSbagliata3 = risposta_sbagliata3

    def __str__(self):
        return self.domanda + self.difficolta + self.rispostaGiusta + self.rispostaSbagliata1 + self.rispostaSbagliata2 + self.rispostaSbagliata3

    def mostra_difficolta(self):
        return self.difficolta
    def mostra_domanda(self):
        return self.domanda
    def mostra_risposta_giusta(self):
        return self.rispostaGiusta
    def mostra_risposta_sbagliata1(self):
        return self.rispostaSbagliata1
    def mostra_risposta_sbagliata2(self):
        return self.rispostaSbagliata2
    def mostra_risposta_sbagliata3(self):
        return self.rispostaSbagliata3

class Player:
    def __init__(self, nickname, punteggio = 0):
        self.nickname = nickname
        self.punteggio = punteggio

    def __str__(self):
        return self.nickname + " " + str(self.punteggio)

def leggi_domande():
    lista_domande = []
    infile = open("domande.txt", "r", encoding="utf-8")
    righe = infile.readlines()
    count = 0
    while count <= len(righe):
        domanda = Domanda(righe[count], righe[count + 1], righe[count + 2], righe[count + 3], righe[count + 4], righe[count + 5])
        lista_domande.append(domanda)
        count += 7
    infile.close()
    return lista_domande

def leggi_giocatori():
    lista_giocatori = []
    infile = open("punti.txt", "r", encoding = "utf-8")
    riga = infile.readline()
    while len(riga) != 0:
        pezzi = riga.split(" ")
        player = Player(pezzi[0], int(pezzi[1]))
        lista_giocatori.append(player)
        riga = infile.readline()
    return lista_giocatori

def scegli_domanda(difficolta, lista_domande):
    domande_scelte = []
    for d in lista_domande:
        if d.mostra_difficolta() == (difficolta + "\n"):
            domande_scelte.append(d)
    num = randint(0, len(domande_scelte) - 1)
    if len(domande_scelte) == 0:
        return ""
    else:
        return domande_scelte[num]

def gioco(domande, giocatori):
    count = 0
    domanda = scegli_domanda(str(count), domande)
    while domanda != "":
        risposta1 = domanda.rispostaSbagliata1
        risposta2 = domanda.rispostaGiusta
        risposta3 = domanda.rispostaSbagliata2
        risposta4 = domanda.rispostaSbagliata3
        print(f"Livello {count}) {domanda.mostra_domanda()}1. {risposta1}2. {risposta2}3. {risposta3}4. {risposta4}")
        risposta = input("Inserisci la risposta: ")
        if risposta == "2":
            print(f"Risposta Corretta!")
            count += 1
            domanda = scegli_domanda(str(count), domande)
        else:
            print(f"Risposta Sbagliata! La risposta corretta era: 2")
            break

    print(f"Hai totalizzato {count} punti!")
    nickname = input("Inserisci il tuo nickname: ")
    return nickname, count

def main():
    domande = leggi_domande()
    giocatori = leggi_giocatori()
    (nickname, count) = gioco(domande, giocatori)


main()
