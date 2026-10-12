### Correlazione 
## Esercizio 1 - Dati: un df con almeno 4 colonne relative ad un fenomeno a scelta(vendite, superficie, prezzo, numero di stanze), con almeno 20 righe 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
case = pd.read_csv("ESERCIZIO_M4-3-2_E1-E3_immobili.csv")

# check di come è fatto il df 
case

# 1. calcolare la matrice di correlazione tra tutte le colonne numeriche con df.corr(numeric_only=True)
corr = case.corr(numeric_only=True)

# visualizzo 
sns.heatmap(
    data = corr,
    vmin = -1,
    vmax = 1,
    annot = True,
    cmap = 'inferno',  
)

# 2. calcorare la correlazione tra due colonne a scelta con df["colA"].corr(df["colB"]) e verificare se i valori coincidono con il punto 1

case["superficie"].corr(case["numero_stanze"]) # np.float64(0.8414208305128209) valore che torna con la matrice del punto 1
case["prezzo"].corr(case["distanza_centro_km"]) # np.float64(-0.08471514935641389) calore che torna con la matrice del punto 1

# 3. individuare dalla marice del punto 1 la coppia di colonne diverse dalla diagonale con il coefficiente più vicino a +1 o a -1 e classificala (forte positiva, forte negativa, debole, quasi assente) 

# stampo la matrice 
corr

# la correlazione con il coefficiente più vicino a 1 è quella prezzo - superficie con r = 0.932547 ed è una correlazione forte positiva
# la correlazione con il coefficiente più vicino a -1 è etaimmobile - prezzo con r = -0.132671 ed è una correlazione debole perché più vicina a 0 che -1

## Definizione: coefficiente di correlazione di Pearson e spiegare perché la diagonale della matrice contiene sempre 1
# il coefficiente di correlazione di Pearson è un indice statistico che misura direzione e intensità di una relazione lineare su una scala che va da -1 a +1 
# la diagonale della marice contiene sempre 1 perché rappresenta la misura di correlazione di una variabile con se stessa, che chiaramente è sempre positiva perfetta, poiché una variabile presenta una relazione lineare perfetta con sé stessa
# se vedessimo 0 allora vorrebbe dire che non c'è correlazione tra quelle due variabili 

### Regressione lineare semplice
## Esercizio 2 - un df con una variabili indipendente numerica x e una variabili dipendente numerica y, correlate tra loro, con almeno 20 righe 

from sklearn.linear_model import LinearRegression    # Serve a creare un modello di regressione lineare, che impara la relazione tra le variabili indipendenti X e la variabile dipendente y
from sklearn.model_selection import train_test_split # divide i dati in training set (dati utilizzati per addestrare il modello) e test set (dati utilizzati per verificare quanto bene il modello predice su dati non usati durante l'addestramento)

# 1. richiamre linearRegression da sklearn.linear_model e train_test_split sklearn.model_selection, poi dividere i dati in set di addestramento e di test con test_size=0.2
serie_storica = pd.read_csv("ESERCIZIO_M4-3-2_E4_serie_storica_mensile.csv")

# separo le variabili, voglio prevedere il prezzo in base al mese 

X = serie_storica[["mese"]] # dovrebbe essere la variabile indipendente (predittore) -> deve essere un df
y = serie_storica["valore"] # variabile dipendente, quella che voglio prevedere -> è una Series

# divido i dati trainig test e trining set 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# test_size = 0.2 destina il 20% dei dati al test 
# random_state = 42 rende rirpoducibile la suddivisione casuale 
# X_train predittori usati per addestrare il modello
# X_test predittori usati per testare il modello 
# y_train Valori reali della variabile dipendente per il training
# y_test Valori reali da confrontare con le previsioni

# Quindi il modello impara dall'80% di dati del training set che gli fornisco e verifica la sua capacità predittiva sul 20% restante 
# vedo la divisione dei dati, perché a questo punto ho solo preparato i dati e non ancora addestrato il modello

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# 2. istanziare un modello di regressione lineare, addestrarlo con .fit() sui dati di addestramento, e stampare model.intercept_ e model.coef_.

# richiama la classe di funzioni importate con sklearn.linear_model
model = LinearRegression() # model è l'oggetto che utilizzo per eseguire la regressione 

# addestro il modello sui dati training 
model.fit(X_train, y_train) # .fit() stima i parametri della retta che meglio descrive la relazione tra le variabili del training set

# stampo intercetta e coefficiente angolare 
print("Intercetta:", model.intercept_) # Intercetta: 102.1869527749052
print("Coefficiente superficie:", model.coef_[0]) # Coefficiente superficie: 4.083092037228543

# 3. usare .predict() sui dati di test e calcolare model.score() sugli stessi dati di test, stampando il valore di R quadro ottenuto.

pred_test = model.predict(X_test) # utilizza il modello addestrato per prevedere i valori della variabile dipendente a partire dai predittori del test set
pred_test

# X_test contiene i mesi selezionati per il test
# model contiene la retta stimata durante l'addestramento
# pred_test contiene i valori di valore previsti dal modello per quei mesi

# .score() restituisce il coefficiente di determinazione R2, calcolato confrontando le previsioni del modello con i valori osservati nel test set
# verifico quanto bene il modello riesce a descrivere i dati che non ha utilizzato per l'addestramento

print("r2", model.score(X_test, y_test)) # r2 = 0.939608710861787 indica che sul test set il modello descrive una quota elevata della variabilità dei valori osservati rispetto alla previsione basata sulla loro media


## Definizione: intercetta e coefficiente in una regressione lineare semplice, spiegando cosa rappresenta ciascuno dei due nella retta y = b0 + b1x 
# è il valore che assume y quando x=0. Indica il punto in cui la retta incontra l'asse verticale
# indica di quanto varia y all'aumentare di x  (se è positivo, la retta cresce, se è negativo decresce

### Regressione multipla e overfitting 
## Esercizio 3 - un df con una variabili dipendente numerica y e almeno 3 varaibili indipendenti x1, x2, x3 con 25 righe 
case

# 1. costruire una matrice X con tutte e tre le variabili indipendenti e dividere X e y in set di addestramento

X_multi = case[["superficie", "numero_stanze", "distanza_centro_km"]]
y_multi = case["prezzo"]

# divido X e y in set di addestramento
Xm_train, Xm_test, ym_train, ym_test = train_test_split(
    X_multi,
    y_multi,
    test_size = 0.20,
    random_state = 42
)

# me le printo per check 
print(Xm_train.shape)
print(Xm_test.shape)
print(ym_train.shape)
print(ym_test.shape)

# 2. addestrare un modello di regressione lineare multipla con .fit() e associare cisacun coeff al nome della proprioa variabile con dict(zip(X.columns, model.coef_))
model_multi = LinearRegression()

# addestro 
model_multi.fit(Xm_train, ym_train)

# stampo associando il coef ad ogni varibaile 
print("Intercetta:", model_multi.intercept_)  # Intercetta: 43563.09820293286

# zip() mi permette di associare elementi di due o più sequenze uno ad uno 
print("Coefficienti per variabile:", dict(zip(X_multi.columns, model_multi.coef_))) # Coefficienti per variabile: {'superficie': np.float64(2923.752120676237), 'numero_stanze': np.float64(13701.081658591043), 'distanza_centro_km': np.float64(-8462.319209039948)}

# 3. confrontare il valore di R quadro ottenuto sul set di test con quello calcolato sullo stesso set di addestramento usato per il fit, e commentare se la differenza tra i due suggerisce un rischio di overfitting.
r2_train = model_multi.score(Xm_train, ym_train)
r2_test = model_multi.score(Xm_test, ym_test)

print("R² train:", r2_train) # R² train: 0.9431294994974693
print("R² train:", r2_test) # R² test:  0.8876160058686697
print("Differenza:", r2_train-r2_test) # Differenza: 0.05551349362879954

# la differenza tra i due valori è bassa, inoltre il valore di r_train descrive molto bene i dati di addestramento, mentre r_test mantiene una buona capacità anche sui dati non usati sull'addestramento 
# quindi questo non suggerisce che ci sia rischio di overfitting 

# 4. rimuovere una delle tre variabili indipendenti dal modello, ripetere addestramento e valutazione, e confrontare il nuovo R quadro con quello del modello a tre variabil

X_rid = case[["superficie", "distanza_centro_km"]] # rimuovo numero stanze perché è quella che potrebbe essere quella maggiormente correlata con superficie 

Xr_train, Xr_test, yr_train, yr_test = train_test_split(
    X_rid, 
    y_multi, 
    test_size=0.2, 
    random_state=42
    )

model_rid = LinearRegression()

model_rid.fit(Xr_train, yr_train)

rr2_train = model_rid.score(Xr_train, yr_train)
rr2_test = model_rid.score(Xr_test, yr_test)

print("R² train modello con 2 variabili:", rr2_train) # R² train modello con 2 variabili: 0.9370137366487581
print("R² test modello con 2 variabili:", rr2_test) # R² test modello con 2 variabili: 0.8761999811140135

# i risultati sono coerenti con quelli ottenuti dal modello addestrato sulle 3 variabili indipendenti

## Definizione: multicollinearità e perché può rendere instabile l'interpretazione dei coefficienti in una regressione multipla 
# la multicollinearità si verifica quando due variabili indipendenti di una regressione multipla sono fortemente correlate tra loro 
# questo rende difficili capire come ciascuna variabili contribuisca singolarmente alla previsone rendendo i coefficienti difficili da interpretare 


### Dal modello a Forecasting
# Esercizio 4 - df di una serei storica con almeno 24 osservazioni ordinate nel tempo 

# 1. usare il numero del emse ome variabile indipendente e il valore come dipendente ie addestrare una modello di regressione lineare sui dati storici 
serie_storica

# definire le variabili 
X = serie_storica[["mese"]] # variabile indipendente, il numero del mese che usaimo come predittore
y = serie_storica["valore"] # il valore osservato che vogliamo stimare

# dividere i dati in training e test 
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Creare e addestrare il modello
model = LinearRegression()
model.fit(X_train, y_train) # stima intercetta e pendenza usando i dati di addestramento

# Fare le previsioni sul test set
pred_test = model.predict(X_test) # calcola i valori stimati per i dati di addestramento 

# Valutare il modello
r2_train = model.score(X_train, y_train) # caclola i coefficiente di terminazione R2, confrontando i valoi osservati con quelli stimati 
r2_test = model.score(X_test, y_test)

print("R² training:", r2_train)
print("R² test:", r2_test)



# 2. a differenza degli esercizi precedenti, dividere i dati in addestramento e test rispettando l'ordine temporale (i mesi più recenti nel test, non una divisione casuale), e spiegare nella cella Markdown perché in questo caso una divisione casuale non sarebbe appropriata

# non dobbiamo usare una divisione casuale
# Con train_test_split() e random_state=42, le osservazioni vengono assegnate casualmente al training set e al test set

# in un vero forecasting, quando facciamo una previsione, non conosciamo ancora i dati futuri
# Per simulare correttamente questa situazione, dobbiamo addestrare il modello sui mesi più vecchi e testarlo sui mesi più recenti.

# definire X e y
X = serie_storica[["mese"]]
y = serie_storica["valore"]

# stabilire il punto di separazione
split = int(len(serie_storica) * 0.8) # split calcola la poisizione in cui effettuare la divisione 

# len(serie_storica) -> 30 reistituisce il numero totoale di righe del df
# len(serie_storica) * 0.8 -> 24.0 moltiplichi il numero di righe per 80% delle osservazioni della serie storica
# int(24.0) -> 24 trasforma il risultato in un numeor intero 
# split = 24 quindi sto dicendo a python di utilizzare24 righe per il training set e le restanti 6 per test set  

# separare i dati rispettando l'ordine temporale

X_train = X.iloc[:split] # seleziona i dati da 0 fino alla 23
X_test = X.iloc[split:] # seleziona da 24 fino a 30

y_train = y.iloc[:split]
y_test = y.iloc[split:]

# in questo modo il df è ordinato cronologicamente, il modello viene addestrato sui mesi più vecchi e testato sui più recenti 

# Addestrare il modello
model = LinearRegression()
model.fit(X_train, y_train)

# Stimare i valori del test set
pred_test = model.predict(X_test)

# Valutare il modello
r2_train = model.score(X_train, y_train)
r2_test = model.score(X_test, y_test)

print("R² training:", r2_train) # R² training: 0.9447156613734841
print("R² test:", r2_test) # R² test: -2.5071151750325447


# 3. usare il modello addestrato per stimare il valore di 3 mesi successivi all'ultimo osservato nella serie, applicando .predict() a nuovi valori del numero del mese

# Individuare l'ultimo mese osservato
ultimo_mese = serie_storica["mese"].max()

# Creare i tre mesi successivi
mesi_futuri = pd.DataFrame({
    "mese": [
        ultimo_mese + 1,
        ultimo_mese + 2,
        ultimo_mese + 3
    ]
})

# Stimare i valori futuri
forecast = model.predict(mesi_futuri)

# Organizzare i risultati
risultati_forecast = mesi_futuri.copy()
risultati_forecast["valore_stimato"] = forecast

print(risultati_forecast)

# 4. confrontare la definizione di prediction e di forecasting alla luce di questo esercizio, indicando quale delle due si applica al punto 1 e quale al punto 3.

# Prediction è una stima prodotta dal modello per osservazioni di cui vogliamo stimare il valore della variabile dipendente, `model.predict(X_test)` stima i valori del test set. Con la divisione casuale iniziale, si tratta di una valutazione su osservazioni non utilizzate per l'addestramento, ma non necessariamente future
# Forecasting è una previsione riferita a un periodo futuro, basata sulle informazioni disponibili fino al presente, `model.predict(mesi_futuri)` stima i valori dei tre mesi successivi all'ultima osservazione

# una prediction può riguardare dati passati o presenti non utilizzati nell'addestramento mentre il forecasting riguarda esplicitamente il futuro


## Definizione: scrivere la definizione di forecasting e spiegare il rischio di estrapolare una previsione molto oltre l'intervallo di dati osservati.

# il forecasting è una prevsione riferita ad un periodo futuro basata sulle informazioni disponibili di una serie storica fino al presente in nostro possesso, da un modello che descrive la relazione tra tempo e varibaile osservata
# è rischioso prevedere troppo lontano perché il modello di regressione lineare assume che la relazione stimata continui anche oltre l'intervallo temporale osservato (estrapolazione) ma nella realtà potrebbero verificarsi cambiamenti di tendenza, ciclicità o stagionalità, oscillazioni casualei o eventi estrmi. 
# motivo per cui più ci allontaniamo dall'intervallo dei dati osservati e meno prudente è assumere che la relazione stimata rimanga valida, poiché le ipotesi del modello diventano più difficili da giustificare
