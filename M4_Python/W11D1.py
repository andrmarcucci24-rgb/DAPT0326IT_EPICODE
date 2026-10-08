# importo il dataset di riferimento 
import pandas as pd 
vendite = pd.read_csv("ESERCIZIO_M4-3-1_E1_vendite_mensili.csv")

# vedo la struttura del dataframe
print(vendite)

### Matplotlib
## Esercizio 1 - grafico a linee personalizzato 
# Dati: l'andamento delle vendite mensili di un negozio in un anno, 12 valori a scelte 

# importo la libreiria matplotlib.pyplot
import matplotlib.pyplot as plt

# 1. disegno un grafico a linee delle vendite mensili del 2026
plt.plot(vendite["mese"], vendite["vendite_2026"])

# 2. personalizzo il grafico con titolo etichette assi e unità di misura
plt.title("Andamento delle vendite", color = "red")
plt.xlabel("mese", color = "red")
plt.ylabel("vendite 2026", color = "red")

# 3. aggiungo una seconda serie a scelta (tipo vendite anno precedente) sullo stesso grafico con una leggenda che distingua le due serie 
plt.plot(vendite["mese"], vendite["vendite_2026"], label="2026", color ="yellow")
plt.plot(vendite["mese"], vendite["vendite_2025"], label="2025", color ="green")

plt.ylabel("vendite", color = "red")
plt.legend()

plt.show()

### Seaborn 
## distribuzioni e confronto categorico 
# Dati: un DF ordini con colonne importo (numerica) e categoria (categoria, almeno 3 valori), con almeno 30 righe a scelta

# richiamo il df
ordini = pd.read_csv("ESERCIZIO_M4-3-1_E2_ordini.csv")

# check df
print(ordini)

# 1. richiamare seaborn e usare sns.countplot() per mostrare quante osservazioni ha ciascuna categoria 
import seaborn as sns

sns.countplot(
    data=ordini,
    x="categoria"
)

ordini["categoria"].value_counts() # check per vedere se il numero rappresentato torna 

# 2. usare sns.histplot() sulla colonna importo per mostrare quante osservazioni ha ciascuna categoria
sns.histplot(
    data = ordini,
    x = "importo",
    bins = 20,
    kde = True
)


# 3. usare sns.boxplot() per confrontare la distribuzione di importo tra le categorie 
sns.boxplot(
    data = ordini, 
    x = "categoria",
    y = "importo"
)

## definizione: un outlier è un valore che si discosta in modo anomalo rispetto alla distribuzione 
# in un boxplot possiamo vederlo perché quei valori sono osservabili in quanto si discostano dal box che mostra la distribuzione dei dati
# un istogramma rappresenta i valori in intervalli, quindi un valore molto alto può finire in un intervallo, soprattutto se l'asse x è molto estesa ad esempio 

### Plotly
## Esercizio 3 - Correlazione e interattività
# Dati: un DF con almeno 4 colonne numeriche e una colonna data, relativo a un fenomeno a scelta (dati meteo o vendite giornaliere)

# upload df richiesto 
df = pd.read_csv("ESERCIZIO_M4-3-1_E3-E4_dati_giornalieri.csv")

# 1. calcolare la matrice di correlazione tra le colonne numeriche con .corr(numeric_only = True) e visualizzarla con sns.heatmat() impostando annot = True e i limiti vmin = -1, vmax =1

df_corr = df.corr(numeric_only=True) # definisco la matrice di correlazione 

# visualizzo con seabonr heatmap
sns.heatmap(
    data = df_corr,
    annot=True, 
    vmin= -1, 
    vmax=1
)

# 2. convertire la colonna data in datatype data con pd.to_datetime() e diseganre un lineplot interattivo dell'andamento nel tempo di une delle colonne numeriche con px.line()
df["data"] = pd.to_datetime(df["data"])

# check che la trasformazione sia avvenut
df.dtypes

# importo la libreria Plotly per il grafico interattivo 
from plotly import express as px

plot = px.line(
    df,
    x="data",        # gli dico quale variabile deve stare sulle x
    y="fatturato",   # quale varibaile sulle y
    title="Andamento del fatturato nel tempo", # titolo 
    labels={"data": "Data", "fatturato": "Fatturato (€)"}, # rinomino le lables 
    markers=True,    # mette un punto su ogni colonna 
)

plot.show()

# 3. dalla heatmap del punto 1 individuare la coppia di colonne con la correlazione più forte positiva e negativa e costruire un px.scatter tra quelle due colonne 
# la correlazione più forte è tra numero ordini e fatturato con 0.89 e non ci sono correlazioni negative
scatterplot_1 = px.scatter(
    df, 
    x = "fatturato",
    y = "numero_ordini"
)

scatterplot_1.show()

# 4. aggiungere al grafico del punto 3 il parametro hover_name o un parametro color a scelte per distingue i punti in base a una colonna categorica o temporale aggiuntiva
scatterplot = px.scatter(
    df, 
    x = "fatturato",
    y = "numero_ordini",
    #color = "temperatura",   # qui se metto la variabile che mi interessa abbina il colore dei punti a quella determinata variabile o altrimenti do il colore che voglio ai punti
    hover_name = "data", 
    title = "correlazione fatturato - numero ordini nel tempo", 
    labels= {"fatturato": "Fatturato", "numero_ordini": "N_ordini"}
)

scatterplot.show()

## Definizione: scrivere la definizione di correlazione e spiegare perché una heatmap è più efficace di più scatterplot 
# la correlazione mostra una relazione tra due variabili e quanto in un range di valori compreso da -1 a +1 e mostra quanto due variabili variano insieme es. se il valore è più vicino ad +1 una cresce e l'altra pure
# la visualizzazione con un heatmap è più efficace di uno scatterplot perché la prima riassume la correlazione tra tutte le variabili in un'unica figure
# con un df da 4 colonne ad esempio servono 6 scatterplot per mostrare la realzione tra tutte le variabili 

