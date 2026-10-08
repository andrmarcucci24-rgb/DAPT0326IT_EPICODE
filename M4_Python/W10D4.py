### Valori nulli
## Esercizio 1 - Dati: un DataFrame con colonne nome, eta e citta per 8 righe, costruito con un dizionario di liste
# 1. costruire un df clienti con le 3 colonne, inserendo almeno 3 valori nulli (None) in totale, non tutti sulla stessa colonna 
import pandas as pd

clienti = pd.DataFrame({
    "nome": ["Andrea", "Marco", "Luca", "Francesca", "Giulia", "Alessandro", "Matteo", "Sofia"],
    "eta": [20, 30, 40, 23, None, 37, None, 89],
    "citta": ["Roma", "Milano", "Napoli", None, "Torino", "Verona", "Catania", "Ancona"]
    })

clienti
type(clienti)

# 2. usare .isna() sull'intero DF e poi .isna().sum() per contare i valori nulli in ciascuna colonna

NA = clienti.isna()
print(NA) # restituisce un DF con valori booleani dove True indica valori NaN

NA_sum = clienti.isna().sum()
print(NA_sum) # restituisce un Series sommando i True di ogni indice


# 3. usare .dropna() per ottenere un nuovo DF senza righe null, assegnando il risultato a un nuoca variabile 

drop_na = clienti.dropna()
print(drop_na)

## definizione richiesta: valore nullo in pandas e perché .dropna() non modifica il DF originale 
# un valore nullo è un valore mancante o non disponibile all'interno di un DF
# .dropna() restituisce un DF dovo sono stati eliminati i valori NaN, per conservare il risultato bisogna assegnarlo ad una nuova variabile

### Ordinamento
## Esercizio 2 - Dati: un dataframe prodotti con colonne nome, categoria e prezzo per 6 prodotti di almeno due categorie diverse 
# 1. ordinare un df per la colonna prezzo assegnanso il risultato a una variabile 

# importo il df .csv
prodotti = pd.read_csv("C:/Users/SZN\Desktop/EPICODE CORSO/esercizi/esercizi python/M4-2-2_Pandas_Avanzato/ESERCIZIO_M4-2-2_E2-E3_prodotti.csv")
prodotti

# assegno ad una variabile il df ordinato per la colonna prezzo in ordine decrescente 
prod_ordinati = prodotti.sort_values("prezzo", ascending=False)
prod_ordinati

# 2. ordinare il df passando una lista di due colonne a .sort_values(): prima categoria in ordine crescente e poi prezzo in decrescente 
prod_due = prodotti.sort_values(
    ["categoria", "prezzo"],
    ascending=[True, False]
)

print(prod_due)

### Filtri con condizioni multiple
## Esercizio 3 
# 1. costurire un filtro che selezioni i prodotti con prezzo superiore a una soglia a scelta e categoria uguale a un valore a scelta 
prezzo_sup = prodotti[(prodotti["prezzo"] > 100) & (prodotti["categoria"] == "Computer")]

print(prezzo_sup)

# 2. usare .isin() per selezionare i prodotti che appartengono a una lista di due categorie a scelta, senza scrivere due condizioni unite da |
lista_prod = prodotti[prodotti["categoria"].isin(["Computer", "Accessori"])]

print(lista_prod)

# 3. negare il filtro del punto 2 con tilde per ottenere i pordotti che non appartengono a quelle categorie 
lista_neg = prodotti[~prodotti["categoria"].isin(["Computer", "Accessori"])]

print(lista_neg)

## definizione: definizione di .isin() e spiegare perché in pandas si usano & e | invedi di and e or per combinare condizioni
# .isin() verifica se i valori di una series appartengono a un insieme di valori che speicifichiamo in forma di lista e restituisce una series booleana 

### Strategie di imputazione 
## Esercizio 4
## dati Sereis temperature con sei valori, di cui uno nullo in posizione intermedia 

temperature = pd.Series([20, 21, None, 24, 25])

# 1. applica separatamente .fillna() con un valore fisso a scleta, . ffill() e interpolate() alla stessa serei ottenendo 3 output distinti 

print(temperature.fillna(22)) # sostituisco il NaN con un valore fisso 
print(temperature.ffill()) # usa l'ultimo valore di disponibile prima del NaN
print(temperature.interpolate()) # genera un valore medio tra il valore subito prima e subito dopo NaN

# 2. applicare .bfill() alla stessa series e confrontare il suo risultato con quello di .ffill()

print(temperature.bfill()) # usa il valore immediatamente successivo a quello NaN

# 3. indicare per un caso in cui il valore nullo fosse il primo elemento della Series invece che uno intermedio, quale dei quattro medoti non riuscirebbe a rimepirlo
# non riuscirebbe a riempirlo .ffill() in quanto non è presente un valore disponibile prima del NaN

## definizione: imputazione e spiegare la differenza concettuale tra un valore imputato .fillna() e uno stimapto con .interpolate()
# L'imputazione è il processo con cui si sostituiscono i valori mancanti di un dataset con valori stimati o scelti secondo un determinato criterio, così da poter utilizzare i dati nelle successive analisi
# .fillna() il valore mancante viene sostituito con un valore specificato direttamente, ad esempio una costante, la media o la mediana dei dati
# .interpolate(), invece, il valore mancante viene stimato sulla base dei valori disponibili prima e dopo il valore mancante

### Raggruppamento e aggregazione
## Esercizio 5 - un df vendite 

# 1. raggruppare il df per la colonna prodotto e calcolare la media della colonna importo per cascun gruppo 
vendite = pd.read_csv("C:/Users/SZN\Desktop/EPICODE CORSO/esercizi/esercizi python/M4-2-2_Pandas_Avanzato/ESERCIZIO_M4-2-2_E5_vendite.csv")

mean_sales = vendite.groupby("prodotto")["importo"].mean()
mean_sales

# 2. usare .agg() per calcolare contemporaneamente media e somma per ciscun prodotto in un'unica istruzione 
mean_sum_sales = vendite.groupby("prodotto")["importo"].agg(["mean", "sum"])

mean_sum_sales

# 3. raggruppare per le due colonne prodotto e regione insieme e usare .get_group() per recueperare le righe originali di una combinazione specifica
group = vendite.groupby(["prodotto", "regione"]).get_group(("Notebook", "Centro"))

g = group.get_group(("Notebook", "Centro")) # gli passo un tupla e non una lista perché ogni gruppo è identificato dalla combinazinoe di due colonne 

print(g)
print(group)

### Merge, concat e date 
## Esercizio 6 - Dati: due DF ordini e cliente 
# load df
ordini = pd.read_csv("ESERCIZIO_M4-2-2_E6_ordini_da_concatenare.csv")
clienti = pd.read_csv("ESERCIZIO_M4-2-2_E6_clienti.csv")

# 1. unire ordini e clienti con pd.merge, usando id_cliente come chiave e how="left" per ottenere il nome del cliente su ogni riga 

# check df 
ordini
clienti

# left join usando come chiave id_cliente 
merge = pd.merge(ordini, clienti, on = "id_cliente", how = "left")

# check
merge # le date essendo nel formato diverso più colonne per i clienti e per le date questo è da fixare 

# 2. convertire la colonna data_str del DF unito in un vero datatype data con pd.to_datetime(), usando il parametro dayfirst appropriato per il formato indicato, in un nuova colonna data
data_fix = pd.to_datetime(merge["data_str"], dayfirst = True)

# 3. usare l'accessor .dt sulla colonna data per estrarre il mese in una colonna aggiuntiva, poi usare pd.concat() per accodare un secondo piccolo DF di ordini con le stesse colonne 
merge.dtypes # data          datetime64[us]  dall'output vedo che è in formato datetime64

# quindi essendo nel formato datetime64 posso usate il .dt per estrarre le componenti in un contenitore, poiché funziona soltanto su colonne di tipo data 
merge["data"].dt.year        # anno (2026)
merge["data"].dt.month       # mese come numero (4)
merge["data"].dt.day         # giorno del mese (10, 28)
merge["data"].dt.day_name()  # nome del giorno
merge["data"].dt.month_name()  # nome del mese ("April")

# creo colonna aggiuntiva col mese 
merge["mese"] = merge["data"].dt.month

# pd.concat() incolla più df uno sotto l'altro o uno affinco all'altro, non come merge che unisce sulla base di una chiave comune, come in SQL
new_order = pd.DataFrame({
    "id_ordine": [209, 210],
    "id_cliente": [2, 4],
    "importo": [75.0, 120.5],
    "data_str": ["02/05/2026", "15/05/2026"],
    "nome_x": ["Luca Bianchi", "Anna Neri"],
    "data": pd.to_datetime(["02/05/2026", "15/05/2026"], dayfirst=True),
    "mese": [5, 5],
    "nome_y": ["Luca Bianchi", "Anna Neri"],
})

risultato = pd.concat([merge, new_order], ignore_index=True)
risultato # vediamo i due df impilati uno sull'altro 



## Definizione: merge e spiegare perché pd.concat() non richiede una colonna chiave comune come invece richiede pd.merge()
# il pd.merge permette di unire due dataframe sfruttando una colonna chiave per far corrispondere le righe dei due df confrontando i valori della colonna chiave
# pd.concat() è diverso perché non ha bisogno di una colonna chiave che permette il confrontare le righe dei due df ma li impilia semplicemente  

