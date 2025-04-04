# 🍝 Gestione Ristorante in Python

Questo progetto è un semplice sistema di gestione per un ristorante, scritto in **Python**, che permette di:

- Visualizzare le informazioni del ristorante
- Gestire lo stato di apertura/chiusura
- Aggiungere e rimuovere piatti dal menu
- Visualizzare il menu aggiornato

Il codice utilizza **programmazione orientata agli oggetti (OOP)** per rappresentare il ristorante come una classe.

---

## 📦 Struttura del codice

- `Ristorante` è la classe principale, che contiene:
  - Attributi come `nome`, `cucina`, `menu`, `aperto`
  - Metodi per descrivere il ristorante, modificare il menu, e gestire lo stato

- Funzioni esterne:
  - `aggiungi_piatto()`: chiede all’utente un piatto e lo aggiunge al menu
  - `rimozione()`: rimuove un piatto inserito dall’utente
  - `apertura()`: gestisce lo stato aperto/chiuso
  - `menu()`: stampa il menu corrente

- Ciclo principale:
  - Permette all'utente di scegliere cosa fare tramite un semplice menu numerato

---

## ▶️ Esecuzione

Per eseguire il programma, basta lanciare lo script in Python 3:

```bash
python ristorante.py
