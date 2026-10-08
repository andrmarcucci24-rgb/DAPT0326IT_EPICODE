### Array Numpy
## Esercizio 1 - Dati: temperature in gradi celsius da caricare rappresentare e analizzare con Numpy
# 1. importare NumPy e creare un Array a partire dalla lista temperature

# importo numpy
import numpy as np
import pandas as pd

# importo il dataset T°
ds = pd.read_csv("C:/Users/SZN/Desktop/EPICODE CORSO/esercizi/esercizi python/M4-2-1_Pandas_NumPy/M4-2-1_Pandas_NumPy/ESERCIZIO_M4-2-1_E1_temperature.csv")

# controllo la struttura dei dati importati è un data frame
type(ds)

# converto in array
temperature = np.array(ds)

type(temperature)

# 2. convertire l'array in gradi Fahrenheit applicando la formula in un'unica operazione vettoriale 
T_fahrenheit = (temperature*9/5) + 32
    
print(T_fahrenheit) # stampo la conversione 

# 3. calcolare media, minimo e massimo dell'array originale in gradi celsius con numpy

def sta_descr(temperature):           # definisco la funzione per l'array temperature, voglio calcolare la statistica descrittiva per quei dati
    mean = temperature.mean()         # al corpo della gli dico di calcolare separatamente i tre valori 
    minimo = temperature.min()
    massimo = temperature.max()

    return mean, minimo, massimo      # me li faccio restituire tutti e 3 insieme

print(sta_descr(temperature))         # stampo i valori ottenuti dalla funzione

## Definizione richiesta: scrivere la definizione di array numpy e di operazione vettoriale, spiegando perché la conversione del punto 2 non richiede un ciclo esplicito
# Un array NumPy è una struttura dati che contiene una sequenza di elementi generalmente dello stesso tipo, accessibili tramite indice. Può essere monodimensionale o multidimensionale
# Un'operazione vettoriale è un'operazione che viene applicata direttamente a tutti gli elementi di un array, senza dover scrivere esplicitamente un ciclo for

### Pandas Series
## Esercizio 2 - Dati un elenco di 5 città con la rispettiva popolazione, da rappresentare con una Series Pandas

# importo pandas
import pandas as pd

# importo il dataset
ds = pd.read_csv("C:/Users/SZN/Desktop/EPICODE CORSO/esercizi/esercizi python/M4-2-1_Pandas_NumPy/ESERCIZIO_M4-2-1_E2_citta_popolazione.csv")

print(ds) # vedo le variabili del mio dataframe

# 1. creo una Series con le popolazioni come valori e i nomi delle città come incidi
serie= pd.Series(
    [2755309, 1366180, 908082, 856745, 625956],
    index = ["Roma", "Milano", "Napoli", "Torino", "Palermo"]
)

print(serie)
# 2. accedere al valore di una città specifica usando la sua etichetta di indice, non la posizione numerica
serie["Roma"] # così accedo al valore assegnato alla città specifica, poiché nel costruire una serie l'ho indicata come indice 

# 3. creare una seconda series a partire da un dizionario città:popolazione e verificare che il risultato sia equivalente a quello del punto 1
dizionario = {
    "Roma": 2755309,
    "Milano": 1366180,
    "Napoli": 908082,
    "Torino": 856745,
    "Palermo": 625956
}

creo_series = pd.Series(dizionario)

print(creo_series)

## Definizione richiesta: definizione di Series e spiegare la differenza tra l'indice di una Series e la posizione numerica di un elmento in una lista
# Una Series è una struttura unidimensionale di Pandas costituita da una sequenza di valori associati a un indice, ogni valore può essere associato tramite la propria etichetta o tramite posizione
# L'indice di una serie è l'etichetta associata a ciascun valore e può essere una stringa ad esmepio (anche un numero o una data)
# La posizione di un elemento in una lista sindica l'ordine in cui l'elemento si trova nella lista

### Pandas DataFrame
## Esercizio 3 - Dati: un piccolo catalogo prodotti con nome categoria e prezzo per 4 prodotti
# 1. costruire un dizionario con le tre liste (nome, categoria, prezzo) e creare un dataframe con pandas

# importo dataset csv
prodotti = pd.read_csv("C:/Users/SZN/Desktop/EPICODE CORSO/esercizi/esercizi python/M4-2-1_Pandas_NumPy/ESERCIZIO_M4-2-1_E3_prodotti.csv")

# vedo la tipologia dell'oggetto 
type(prodotti)

# creo dizionario come richiesto
dizionario_prod = {
    "nome": ["Notebook", "Mouse", "Monitor", "Tastiera"],
    "categoria": ["Computer", "Accessori", "Monitor", "Accessori"],
    "prezzo": [899.0, 29.9, 249.0, 79.9]
}

# stampo l'oggetto e vedo a che categoria appartiene -> dict
print(dizionario_prod)
type(dizionario_prod)

# creo DF 
df_prod = pd.DataFrame(dizionario_prod)

# stampo DF e vedo la categoria di apprtenenza pandas.DataFrame
print(df_prod)
type(df_prod)

# 2. ispezionare il DataFrame con .shape e . columns stampando i risultati 
print(df_prod.shape) # (4, 3) 4 righe e 3 colonne 
print(df_prod.columns) # restituisce nome delle colonne e tipologia dell'oggetto

# 3. selezionare la colonna prezzo del DataFrame e verificare con type() che il risultato sia una Series
type(df_prod["prezzo"]) # il risultato è una Series perché con quella sintassi, ossia le singole parentesi quadre si estraggono i valori di quella colonna in formato Series
type(df_prod[["prezzo"]]) # questa sintassi, doppie parentesi quadre, estrae la colonna come dataframe

## Definizione Richiesta: scrivere la definizione di DataFrame e spiegare perché ogni sua colonna è di fatto una Series
# Un DF è una struttura bidimensionale organizzata in righe e colonne dove ogni colonna può presentare dati di un tipo specifico e possiede un porprio indice 
# La singola colonna di un DF è una Series perché è una struttura unidimensionale costituita da una sequenze di valori associati allo stesso indice, come se fosse un insieme di Series con lo stesso indice


### Lettura e ispezione 
## Esercizio 4 - Dati: un DF ordini con colonne id_ordine, cliente, importo, citta e 12 righe, alcune con valori mancanti nella colonna importo, da costruire con un dizionario di liste

# 1. costruire il DF ordini a partire da un dizionario di liste con le quattro colonne indicate inserendo almeno due valori (None) nella colonna importo 
ordini = pd.DataFrame({
    "id_ordine": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "cliente": ["Andrea", "Marco", "Luca", "Francesca", "Giulia", "Alessandro", "Matteo", "Sofia", "Chiara", "Davide", "Elena", "Simone"],
    "importo": [100, 200, 400, None, 1000, 30, 3000, None, 8000, 90, 800, 900],
    "citta": ["Roma", "Milano", "Napoli", "Palermo", "Torino", "Verona", "Catania", "Ancona", "Trento", "Trieste", "Aosta", "Catanzaro"],
    })

type(ordini)
ordini

# 2. utilizzare la funzione .info() per individuare quante righe della colonna importo contengono valori non nulli
ordini.info() # 2   importo    10 non-null     float64 da questo output capisco che 2 righe nella colonna contengono valoni nulli

# 3. usare .describe() sulla colonna importo e .value_count() sulla colonna citta confrontando le informazioni restituite dai due metodi

# describe mi restituisce la stitistica descrittiva della colonna selezionata. 
ordini[["importo"]].describe() # così mi vengono restituite le statitstiche un df con una singola colonna 
ordini["importo"].describe() # così le stesse statistiche nel formato Series

ordini["citta"].value_counts() # mi restituisce quante volte compare un singolo valore nella colonna selezionata

## definizione: valore mancante e spiegare la differenza tra .info() e .describe()
# un valore mancante è un'osservazione per la quale non è disponibile alcun valore in un dataframe
# .info() ci da informazioni sulla struttura del dataframe, tra cui se ci sono valori mancanti e la tipologia di variabili presenti 
# .describe() calcola le principali statistiche descrittive del dataframe sulle colonne numeriche 

### .loc[] e .iloc[]
## Esercizio 5 - Data: il df dell'esercizio precedente e un df equivalente con almeno 6 righe 
ord = pd.read_csv("C:/Users/SZN/Desktop/EPICODE CORSO/esercizi/esercizi python/M4-2-1_Pandas_NumPy/ESERCIZIO_M4-2-1_E4-E6_ordini.csv")

ord # check del df

# 1. imposta la colonna id_ordine come indice 
index_ord = ord.set_index("id_ordine")

print(index_ord)

# 2. sul df con il nuovo indice selezionare una riga con .loc[] usando l'etichetta di id_ordine e la stessa riga con .iloc[] usando la posizione nuemrica
etichetta_1 = ord.loc[4] # lavora sulle etichette quindi qui mi sta dando tutte le variabili per ogni etichetta della riga 4
print(etichetta_1)

ord.loc[4, "importo"] # così gli ho chiesto di darmi la varibile associata a quella singola etichetta 

ord.iloc[4] # iloc lavora sulla con la posizione, così mi da tutte le variabili della riga 4 con le etichette 

etichetta_2 = ord.iloc[4,3] # il primo numero indica la riga mentre il secondo la colonna, quindi in questo modo ottengo la variabile citta della riga 4 
print(etichetta_2)

# 3. selezionare un intervallo di tre righe consecutive con .loc[] e .iloc[] confrontando quante righe restiuise ciascun intervallo

ord.loc[0:2]

ord.iloc[0:3]

## Definizione: definizione di indicizzazione per etichetta e per posizione, spiegando perché il numero di righe ottenuto al punto 3 con i due approcci può differire

### Masking
# Esercizio 6 - Dati: il DF ordini con colonne importo e citta
ord
# 1. costruire una maschera boolena con individui gli ordini con importo superiore a una soglia a scelta e usarla per filtrare il df con .loc[]
ord["importo"] > 50

# 2. costruire un filtro che combini due condizioni con l'operatore &: importo superiore alla soglia scelta == a una citta a scelta
(ord["importo"] > 50) & (ord["citta"] == "Milano")

# 3. costruire un filtro che usi l'operatore | per selezionare gli ordini di due citta diverse, poi negare lo stesso filtro con l'operatore tilde e confrontare i due risultati 

((ord["citta"] == "Milano") | (ord["citta"] == "Napoli")) # qui riporta true per gli ordini che hanno come citta Milano o Napoli

citta_ord = ord[(ord["citta"].isin(["Milano", "Napoli"]))] # questo è lo stesso output, ma se inserisco tutto il blocco tra parentesi quadre con davanti il df di riferimento mi estrae un df con tutti i dati che mi interessano sulla base della maschera boolena 
citta_ord

(~(ord["citta"]=="Milano") | (ord["citta"] == "Napoli")) # qui riporta True per gli ordini che non hanno Milano o Napoli come citta

## Definizione: Masking 
# è il processo di creazione di una maschera booleana, una sequenza di ture e false usata per selezionare solo gli elementi che soddisfano una determinata condizione