
class Ristorante():
    
    menu=[]
    aperto=False
    
    
    def __init__(self,nome,cucina):
        
        
        self.nome=nome
        self.cucina=cucina
       
        
        
    
    def descrivi_ristorante(self):
        
        print("IL RISTORANTE SI CHIAMA ",self.nome,"\n LA SUA CUCINA E' DI TIPO ",self.cucina,"IL MENU DA NOI SERVITO E' QUESTO : \n,",self.menu)
        
    
    
    def stato_apertura():
        
        print(Ristorante.aperto)
    
    
    
    
    def apertura(risposta):
        
        if(risposta=="SI"):
            
            Ristorante.aperto=True
            print("RISTORANTE APERTO")
            
    
        else:
            Ristorante.aperto=False 
            print("RISTORANTE CHIUSO")
            
    
    
    def mostra_menu():
        print("\n Menu aggiornato:")
        for voce in Ristorante.menu:
            print(f'{voce["piatto"]}: {voce["prezzo"]}€')
        print("-" * 20)
    
    
   
    def rimuovi_piatto(nome_piatto):
       
      
        for elemento in Ristorante.menu:
            if elemento["piatto"] == nome_piatto:
                Ristorante.menu.remove(elemento)
       
        print(f' "{nome_piatto}" rimosso dal menu.')
        
    
    def aggiungi_piatto(nome_piatto, prezzo_piatto):
         Ristorante.menu.append({"piatto": nome_piatto, "prezzo": prezzo_piatto})
         
    
 
 

def aggiungi_piatto(ristorante):
    
    
    nome_piatto=input("inserisci nome del piatto")
    prezzo=int(input("inserisci prezzo"))
    
    ristorante.aggiungi_piatto(nome_piatto,prezzo)
    

def rimozione(ristorante):
    
    piatto=input("inserisci nome del piatto da rimuovere")
    ristorante.rimuovi_piatto(piatto)
    
    
def apertura(ristorante):  
    
    risposta=input("ciao vuoi aprire il ristorante?")
    ristorante.apertura(risposta)

def menu(ristorante):
    
    Ristorante1.mostra_menu()
    
    
    
     
     
 
    
    
    

#PROGRAMMA


c=True
Ristorante1=Ristorante("Villa Borghese","Cucina Contemporanea")
while(c):
    
    
    scelta=int(input("CIAO, SELEZIONA LA TUA OPZIONE :\n 1.STAMPA DESCRIZIONE\n2.STATO APERTURA\n3APERTURA O CHIUSURA\n4.AGGIUNGI PIATTO\n4.RIMUOVI PIATTO\n5.STAMPA MENU"))
    
    match scelta:
            
            case 1:
                Ristorante1.descrivi_ristorante
            
            case 2:
                
                Ristorante1.stato_apertura()
            case 3:
                Ristorante1.apertura(Ristorante1)
                
            case 4:
                aggiungi_piatto(Ristorante1)
            
            case 5:
                rimozione(Ristorante1)
            
            case 6: 
                menu(Ristorante1)
            
            
            case 7: 
                print("ESCI DAL SISTEMA")
                c=False
                


           
        