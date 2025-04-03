class Ristorante():
    # Attributi di classe
    menu = []  # Lista che rappresenta il menu del ristorante
    aperto = False

    def __init__(self, nome, cucina):
        # Inizializza un'istanza della classe Ristorante con nome e tipo di cucina
        self.nome = nome
        self.cucina = cucina
       

    def descrivi_ristorante(self):
        # Stampa una descrizione del ristorante, inclusi il nome, il tipo di cucina e il menu
        print(f"IL RISTORANTE SI CHIAMA {self.nome}")
        print(f"LA SUA CUCINA È DI TIPO {self.cucina}")
        print(f"IL MENU DA NOI SERVITO È QUESTO: {self.menu}")

    
    def stato_apertura(self):
        # Stampa lo stato di apertura del ristorante (aperto o chiuso)
        print("Stato del ristorante:", "Aperto" if self.aperto else "Chiuso")

    def apertura(self, risposta):
        # Modifica lo stato di apertura del ristorante in base alla risposta dell'utente
        if risposta.upper() == "SI":
            self.aperto = True
            print("RISTORANTE APERTO")
        else:
            self.aperto = False
            print("RISTORANTE CHIUSO")

    def mostra_menu(self):
        # Stampa il menu aggiornato del ristorante
        print("\nMenu aggiornato:")
        for voce in self.menu:
            print(f'{voce["piatto"]}: {voce["prezzo"]}€')
        print("-" * 20)

    def rimuovi_piatto(self, nome_piatto):
        # Rimuove un piatto dal menu in base al nome
        for elemento in self.menu:
            if elemento["piatto"] == nome_piatto:
                self.menu.remove(elemento)
                print(f'"{nome_piatto}" rimosso dal menu.')
                return
        print(f'"{nome_piatto}" non trovato nel menu.')

    def aggiungi_piatto(self, nome_piatto, prezzo_piatto):
        # Aggiunge un piatto al menu
        self.menu.append({"piatto": nome_piatto, "prezzo": prezzo_piatto})
        print(f'"{nome_piatto}" aggiunto al menu con prezzo {prezzo_piatto}€.')

# Funzioni esterne per interagire con la classe Ristorante
def aggiungi_piatto(ristorante):
    # Richiede all'utente di inserire un piatto e il suo prezzo, e lo aggiunge al menu
    nome_piatto = input("Inserisci il nome del piatto: ")
    prezzo = int(input("Inserisci il prezzo: "))
    ristorante.aggiungi_piatto(nome_piatto, prezzo)

def rimozione(ristorante):
    # Richiede all'utente di inserire il nome di un piatto da rimuovere e lo elimina dal menu
    piatto = input("Inserisci il nome del piatto da rimuovere: ")
    ristorante.rimuovi_piatto(piatto)

def apertura(ristorante):
    # Richiede all'utente se vuole aprire o chiudere il ristorante
    risposta = input("Ciao, vuoi aprire il ristorante? (SI/NO): ")
    ristorante.apertura(risposta)

def menu(ristorante):
    # Mostra il menu del ristorante
    ristorante.mostra_menu()

# PROGRAMMA PRINCIPALE
print("Benvenuto nel sistema di gestione del ristorante!")
c = True
Ristorante1 = Ristorante("Villa Borghese", "Cucina Contemporanea")

while c:
    print("\nSeleziona un'opzione:")
    print("1. Stampa descrizione del ristorante")
    print("2. Controlla stato di apertura")
    print("3. Apri o chiudi il ristorante")
    print("4. Aggiungi un piatto al menu")
    print("5. Rimuovi un piatto dal menu")
    print("6. Mostra il menu")
    print("7. Esci dal sistema")


    scelta = int(input("Inserisci il numero della tua scelta: "))
    match scelta:
        case 1:
            print("\n--- Descrizione del Ristorante ---")
            Ristorante1.descrivi_ristorante()
        case 2:
            print("\n--- Stato di Apertura ---")
            Ristorante1.stato_apertura()
        case 3:
            print("\n--- Apertura/Chiusura del Ristorante ---")
            apertura(Ristorante1)
        case 4:
            print("\n--- Aggiungi un Piatto ---")
            aggiungi_piatto(Ristorante1)
        case 5:
            print("\n--- Rimuovi un Piatto ---")
            rimozione(Ristorante1)
        case 6:
            print("\n--- Menu del Ristorante ---")
            menu(Ristorante1)
        case 7:
            print("\nGrazie per aver utilizzato il sistema. Arrivederci!")
            c = False
        case _:
            print("\nScelta non valida. Riprova.")





