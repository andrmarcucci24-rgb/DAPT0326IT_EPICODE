
### Costrutto if/elif/else
## Esercizio 1 - Dati: temperatura = 78°C rilevata su un macchinario, con tre soglie: alllarme se superiore a 80, attenzione se superiore a 60, normale altirmenti. 
temperatura = 78  # creo l'oggetto temperatura

## 1. scrivere un costrutto if/elif/else che stampi "Allarme", "Attenzione", "Normale" in base al valore di temperatura usando gli operatori di confronto corretti 

# fornisco le condizioni, siccome python valuta le condizioni dall'alto verso il basso e si ferma alla prima condizione vera
if temperatura > 80:    # valuta prima se la temperatua è maggiore di 80, e in questo caso è FALSE, quindi va avanti finché non incontra la condizione TRUE 
    print("ALLARME!")
elif temperatura > 60:
    print("SURRISCALDAMENTO!")
else: 
    print("OK!") 

## 2. modificare il valore di temperatura con altri due valori che attivino gli altri rami 
temperatura = 40

if temperatura > 80:  
    print("ALLARME!")
elif temperatura > 60:
    print("SURRISCALDAMENTO!")
else: 
    print("OK!") 


temperatura = 85

if temperatura > 80:  
    print("ALLARME!")
elif temperatura > 60:
    print("SURRISCALDAMENTO!")
else: 
    print("OK!") 

## 3. Definizione richiesta: spiegare perché in nessun caso vengono eseguiti più di uno tra i rami if, elif ed else
# Perché vengono fornite delle condizioni, python le scorre dall'alto verso il basso finché non incontra quella condizione che è TRUE e si ferma 

## scrivere la definizione di costrutto condizionale e la differenza tra elif ed else 
# Un costrutto condizionale è una struttura del linguaggio che permette a un programma di eseguire blocchi di codice diversi a seconda che una condizione sia vera o falsa
# elif indica un altro caso specifico da controllare mentre else è il caso residuo che raccoglie tutto quello che non è compreso dalle condizioni precedenti

### Ciclo for
## Esercizio 2 - Dati: articoli = ["penna", "quaderno", "zaino"] e prezzi = {"penna": 1.5, "quaderno": 3.0, "zaino": 25.0}
articoli = ["penna", "quaderno", "zaino"]
prezzi = {"penna": 1.5, "quaderno": 3.0, "zaino": 25.0}

## 1. usare il ciclo for per stampare ogni elemento della lista articoli, uno per riga 
for nomi in articoli: 
    print(nomi)

## 2. usare un ciclo for con il metodo .items() per stampare ogni coppia articolo prezzo del dizionario prezzi 
for articolo, prezzo in prezzi.items():
    print(articolo, prezzo)

## 3. all'interno del ciclo sul dizionario, usare un if per stampare un messaggio aggiuntivo solo per gli articoli con prezzo superiore a 10
for articolo, prezzo in prezzi.items():
    print(articolo, prezzo)
    if prezzo > 10: 
        print("Cheap")

## Definizione richiesta: definizione del ciclo for e spiegare la differenza tra iterare direttamente su un dizionario e iterare con .items()
# Il ciclo for è una struttura di controllo che permette di ripetere un blocco di codice per ogni elemento di una sequenza
# iterando direttamente su dizionario python scorre solo le chiavi, con .items() otteniamo coppie chiave-valore che puoi separare in due variabili 

### Funzioni con parametri e return
## Esercizio 3 - Dati: una funzione da scrivere per calcoalre il totale di un ordine, dato da un prezzo unitario e una quantità

# 1. definira una funzione calcola_totale(prezzo, quantita) che restituisca con return il prodotto tra i due parametri 

# definisco la funzione 
def calcola_totale(prezzo, quantita):
    totale_ordine = prezzo*quantita
    return totale_ordine

# check funzione 
print(calcola_totale(850.69,12))

# 2. richiamare la funzione una volta con argomenti posizionali e una volta con argomenti keyword invertendo l'ordine, e stampare entrambi i risultaiti

print(calcola_totale(850.69,12)) # argomenti posizionali 
print(calcola_totale(quantita = 12, prezzo = 850.69)) # argomenti keyword con ordine invertito 

# 3. modificare la funzione aggiungendo un parametro sconto con valore default 0, che riduce il totale della percentuale indicata qaundo viene passato un valore diverso da 0 
def calcola_totale(prezzo, quantita, sconto = 0):
    totale_ordine = prezzo*quantita*(1-sconto/100) # 1 è il 100% dle prezzo fisso al quale sottraiamo il valore dello cosnto, in questo caso il 30% 
    return totale_ordine

# check con lo socnto del 30%
print(calcola_totale(850.69,12,30))

## Definizione richiesta: definizione di funzione e di parametro con valore di default, indicando quando l'argomento sconto può essere omesso nella chiamta
# una funzione è un blocco di codice nominato che può ricevere dati in ingresso, eseguire delle operazioni e restituire un risultato. 
# un parametro con valore di default è un parametro al quale assegnamo un valore gia nella definizione sconto = 0, possimao omettre l'argomento sconto quando non si vuole applicare nessuno sconto, essenfo di default 0 applica in automatico lo 0% di sconto 

### Ciclo while
## Esercizio 4 - Dati: un capitale iniziale di 1000 euro che cresce del 5% ogni anno, si vuole sapere dopo quanti anni supera i 1500 euro

capitale = 1000 # gli dico il capitale di partenza
anni = 0        # gli imposto il contatore da 0

# 1. scrivere un ciclo while che aggiorni il capitale di anno in anno finché non supera i 1500 aggiornando ad ogni operazione capitale e contatore
# 2. stampare il capitale e il numero di anni trascorsi a ogni iterazione del ciclo

while capitale < 1500:  # gli dico la sogli limite
    capitale *=  1.05  # sarebbe 1 + 0.05 quindi il totale più il 5%
    anni += 1          # gli dico di aumentare di uno il contatore moltiplicando il valore di capitale per l'incremento de 5%
    print(anni, capitale) # questo stampa il risultato del ciclo per ogni anno 
    

print(f"Il capitale supera 1500 euro dopo {anni} anni") # con la f-string dico a python di sotituire la variabile tra parentesi graffe con il suo valore

# 3. indicare quale istruzione, se rimossa dal corpo del ciclo, trasformerebbe questo while in un loop infinito e per quale motivo
#  capitale *= 1.05 se elimino questa riga di codice capitale resta sempre 1000 e la condizione < 1500 è sempre True, quindi il ciclo diventa infinito

## Definizione richiesta:  definizione di ciclo while e spiegare la differenza rispetto al ciclo for in termini di numero di iterazioni noto o non noto in anticipo
# Il ciclo while è una struttura di controllo che ripete un blocco di istruzioni finché una condizione booleana resta vera. La condizione viene valutata prima di ogni iterazione: quando diventa False il ciclo termina.
# Il ciclo for, invece, itera su una sequenza o un iterabile (lista, range, stringa...) e il numero di iterazioni è noto in anticipo: coincide con il numero di elementi dell'iterabile.

### List comprehension
## Esercizio 5 - Dati voti = [5, 8, 6, 9, 4, 7, 10]

voti = [5, 8, 6, 9, 4, 7, 10]
voti_sufficienti = []

# 1. scrivere un ciclo for con append() che costruisca una nuova lista contenente solo i voti maggiori o uguali a 6.
for voto in voti:
    if voto >= 6:
        voti_sufficienti.append(voto)

print(voti_sufficienti)

# 2. scrivere una list comprehension che ottenga lo stesso risultato del punto 1 con la sintassi [espressione for elemento in iterabile if condizione]
voti_sufficienti_lc = [voto for voto in voti if voto >= 6]

print(voti_sufficienti_lc)

# 3. scrivere una seconda list comprehension che moltiplichi per 10 ciascun voto della lista voti, senza alcuna condizione di filtro
voti_x10 = [voto * 10 for voto in voti]

print(voti_x10)

## Definizione richiesta: definizione di list comprehension ed elencare in quali casi è preferibile tornare ad un ciclo for 
# La list comprehension è una sintassi compatta per creare una nuova lista a partire da un iterabile, con la struttura [espressione for elemento in iterabile if condizione]. La parte davanti al for decide cosa viene inserito nella lista, l'if finale (opzionale) filtra gli elementi.


### Funzioni e Librerie
## Esercizo 6 - Dati: un elenco di 5 numeri a scelta, da elaborare con una funzione che usa una libreria della standard library

numero = [50, 100, 150, 200, 250] 

# 1. importare la libreria math e definire una funzione radice_arrotondata(numero, decimali=2) che restituisca con return la radice quadrata di numero, arrotondata al numero di decimali indicato con round() 
import math as m # importo la libreira

# definisco la funzione 
def radice_arrotondata(numero, decimali=2):
    result = m.sqrt(numero)
    return round(result, decimali)

# check funzione
print(radice_arrotondata(50, 6))

# 2. richiamara la funzione su ciascuno dei 5 numeri usando un ciclo for, stampando ogni risultato
for numeri in numero:
    print(radice_arrotondata(numeri))

# 3. richiamare la funzione una volta senza indicare l'argomento decimali e una volta indicandolo esplicitamente come argomento keyword con un valore diverso da 2, conforntando i due output
print(radice_arrotondata(200)) # stampo senza decimali 
print(radice_arrotondata(decimali=5, numero= 250)) # stampo con keyword 

## Definizione richiesta: scrivere la definizione di libreria e spiegare perché il comando import è necessario anche per funzioni della standard library come quelle dei moduli math
# una libreria è una raccolta di codice già scritto e riutilizzabile onrganizzato in funzioni definite che svolgono operazioni, evitando di riscrivere da 0 operazioni comuni
# una standard library è l'insime di librerie che vengono installate insieme all'installazione di python, tuttavia bisogna sempre importarle per utilizzarle poiché non vengono caricati in automatico all'avvio del programma 
