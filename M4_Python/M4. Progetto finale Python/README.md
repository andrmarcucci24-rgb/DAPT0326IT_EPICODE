# Analisi vendite e rivenditori: Python, Pandas, visualizzazione e Machine Learning

Esercizio finale del Modulo 4 (AI & Data Analytics, Epicode Institute of Technology).
Il progetto analizza un dataset di vendite di un'azienda con rivenditori, prodotti e regioni, e copre l'intero percorso di un'analisi dati: Python di base, ispezione e pulizia dei dati, aggregazioni, serie temporali, visualizzazione, regressione lineare, classificazione (churn) e clustering.

---

## Indice

1. [Scenario](#scenario)
2. [Dataset](#dataset)
3. [Struttura della repository](#struttura-della-repository)
4. [Task svolti](#task-svolti)
5. [Risultati documentati nel notebook](#risultati-documentati-nel-notebook)
6. [Istruzioni di esecuzione](#istruzioni-di-esecuzione)
7. [Note importanti sull'esecuzione](#note-importanti-sullesecuzione)
8. [Versioning con Git e GitHub](#versioning-con-git-e-github)
9. [Autore](#autore)

---

## Scenario

Un'azienda vende prodotti (categorie come Outdoor, Giochi da tavolo e Giocattoli) attraverso una rete di rivenditori distribuiti in più stati e regioni di vendita. Il management vuole rispondere a domande di business:

- Quanto fattura l'azienda, per categoria, regione e stato?
- Come cambia il fatturato nel tempo e in quale mese c'è il picco?
- Il fatturato si può prevedere nei mesi successivi?
- Quali rivenditori rischiano di smettere di ordinare (**churn**)?
- Si possono raggruppare i rivenditori in segmenti omogenei per comportamento d'acquisto, e i segmenti hanno un churn diverso?

Il notebook risponde a queste domande partendo da quattro file grezzi e arrivando a modelli predittivi, con commenti e definizioni teoriche scritte per un livello principiante.

---

## Dataset

I quattro file vanno messi nella stessa cartella del notebook.

| File | Formato | Contenuto |
|------|---------|-----------|
| `ESERCIZIO_M4-4-2_traccia_finale-sales.json` | JSON | Transazioni di vendita (2000 righe): `SalesID`, `ProductID`, `RegionID`, `ResellerID`, `SalesDate`, `Quantity`, `SalesAmount` |
| `ESERCIZIO_M4-4-2_traccia_finale-products.csv` | CSV | Anagrafica prodotti, tra cui `ProductID`, `ProductName`, `Category`, `ListPrice` |
| `ESERCIZIO_M4-4-2_traccia_finale-regions.xlsx` | Excel | Anagrafica regioni: `RegionID`, `State`, `SalesRegion` |
| `ESERCIZIO_M4-4-2_traccia_finale-resellers.csv` | CSV | Dati dei rivenditori, tra cui `ResellerID`, `Ordini12m`, `GiorniUltimoOrdine`, `ScontoMedio`, `Reclami`, `Churn` (0/1) |

Qualità dei dati: `Quantity` e `SalesAmount` hanno ciascuna circa il 5% di valori mancanti (100 righe su 2000).

---

## Struttura della repository

```
.
├── README.md
├── <nome_del_notebook>.ipynb
├── ESERCIZIO_M4-4-2_traccia_finale-sales.json
├── ESERCIZIO_M4-4-2_traccia_finale-products.csv
├── ESERCIZIO_M4-4-2_traccia_finale-regions.xlsx
└── ESERCIZIO_M4-4-2_traccia_finale-resellers.csv
```

> Sostituisci `<nome_del_notebook>` con il nome reale del tuo file `.ipynb`.

---

## Task svolti

### Task 1: Python di base sui dati forniti
Calcoli con strutture dati, cicli e funzioni Python, senza metodi di analisi Pandas.

- Differenze tra lista, tupla, set e dizionario.
- Lettura di prodotti, vendite e regioni e conversione in liste di dizionari con `.to_dict(orient="records")`; `regions` come dizionario `RegionID -> (State, SalesRegion)`; set delle categorie uniche con verifica di appartenenza.
- Fascia di prezzo per ogni prodotto con list comprehension e `if/elif/else`: **bassa** fino a 20 €, **media** fino a 60 €, **alta** oltre.
- Funzione `fatturato_categoria(vendite, prodotti, categoria)` con ciclo `for`, che salta i valori mancanti e restituisce il totale con `return`.
- Ciclo `while` che conta le transazioni necessarie a superare 10.000 € di fatturato cumulato; stampa delle prime cinque transazioni con `vendite[:5]`.

### Task 2: Lettura e ispezione dei dati
- Differenze tra Series e DataFrame, e tra `.loc[]` e `.iloc[]`.
- Lettura dei quattro file con `read_csv`, `read_excel`, `read_json` e ispezione con `.shape`, `.info()`, `.head()`, `.tail()`.
- `.describe()` su `Quantity` e `SalesAmount`; conversione in array NumPy e calcolo vettoriale del prezzo unitario.
- Selezione con `.loc[]` e maschera booleana (categoria Outdoor con `ListPrice` > 30) e con `.iloc[]` (righe 10-19, prime tre colonne).

### Task 3a: Dati mancanti, filtri e ordinamento
- Conteggio e percentuale dei NaN per colonna con `.isna()`.
- Imputazione di `Quantity` con la mediana tramite `fillna()`; eliminazione con `dropna()` delle righe con `SalesAmount` mancante, dichiarando il numero di righe rimosse.
- Estrazione con `.query()` delle transazioni sopra il 90° percentile di `SalesAmount` e ordinamento con `sort_values()` (data crescente, importo decrescente).

### Task 3b: Aggregazione e combinazione dei DataFrame
- Differenze tra `.merge()`, `.join()` e `.concat()`.
- Merge di `sales` con `products` (su `ProductID`) e `regions` (su `RegionID`) con `how="left"`, verificando che il numero di righe resti invariato.
- `groupby()` + `agg()` per fatturato totale, quantità totale e numero di transazioni per `Category` e `SalesRegion`, ordinati per fatturato decrescente.
- Separazione delle vendite 2025 dalle altre con un filtro e ricomposizione con `pd.concat()`, verificando che il totale delle righe coincida con l'originale.

### Task 3c: Serie temporali di vendita
- Conversione di `SalesDate` con `pd.to_datetime()`.
- Estrazione di anno, mese e giorno della settimana con l'accessor `.dt`.
- Fatturato mensile con `groupby()` e variazione percentuale tra mesi consecutivi con `pct_change()`.
- Colonna booleana `Recente`: `True` se la vendita è entro 180 giorni dall'ultima data del dataset.

### Task 4: Visualizzazione e storytelling
Ogni grafico ha un **titolo che enuncia il risultato** (calcolato dai dati con f-string) e assi con unità di misura.

| Domanda di business | Grafico | Libreria |
|---------------------|---------|----------|
| Come evolve il fatturato e quando c'è il picco? | Linee con mese di picco annotato | Matplotlib |
| Come si distribuisce l'importo delle vendite per categoria? | Boxplot | Seaborn |
| Quali variabili dei rivenditori sono più correlate? | Heatmap della matrice di correlazione | Seaborn |
| Quanto fattura ogni stato? | Barre interattive con quantità e transazioni nel tooltip | Plotly |

Il notebook include anche il criterio di scelta del grafico: linee per l'andamento nel tempo, barre per il confronto tra categorie, boxplot per le distribuzioni, heatmap o scatter per le relazioni tra variabili.

### Task 5: Correlazione e regressione lineare
- Definizione di R², intervallo dei valori e perché correlazione e R² alto non dimostrano causalità.
- Matrice di correlazione tra fatturato mensile, quantità mensile e numero di rivenditori attivi, con indicazione della coppia più correlata.
- `train_test_split(test_size=0.2, random_state=42)` e due modelli `LinearRegression`: **semplice** (fatturato su indice del mese) e **multipla** (indice del mese, quantità, rivenditori attivi).
- Riepilogo di `coef_`, `intercept_` e R² su train e test; previsione con il modello semplice del fatturato dei 3 mesi successivi all'ultimo disponibile.

### Task 6a: Classificazione del churn dei rivenditori
- Definizione di apprendimento supervisionato e non supervisionato.
- `X` = `Ordini12m`, `GiorniUltimoOrdine`, `ScontoMedio`, `Reclami`; `y` = `Churn`; `train_test_split` con `stratify=y` e `StandardScaler` con `fit` solo sul training set (per evitare data leakage).
- `LogisticRegression` con `predict()` e `predict_proba()`; matrice di confusione con soglia 0.5 e 0.3.
- Accuracy, Precision e Recall per le due soglie e confronto dell'Accuracy con la baseline "sempre Churn = 0".
- Confronto train/test e diagnosi del modello (underfitting, buon adattamento, overfitting) con una regola basata sul gap.

### Task 6b: Segmentazione dei rivenditori con K-Means
- Definizione di centroide e inerzia, e motivo per cui K-Means non richiede `y` né train/test.
- Fatturato totale per rivenditore da `sales`, standardizzazione di `Ordini12m`, `GiorniUltimoOrdine` e `Fatturato`, inertia per k da 1 a 10 (`KMeans(n_init=10, random_state=42)`).
- Scelta di k con il metodo del gomito (nel notebook `k = 3`) e assegnazione dei cluster con `fit_predict()`.
- Profilo dei cluster con `groupby()` sulle variabili originali, nome assegnato a ciascun cluster e quota di churn per cluster.

### Task 7: Debugging, refactoring e versioning
Quattro frammenti di codice errato analizzati, ciascuno con un commento Markdown che spiega cosa non funziona, come si corregge e come si verifica (con il prompt usato).

| Caso | Codice | Problema principale |
|------|--------|---------------------|
| 1 | Media del fatturato con ciclo `for` | I NaN rendono il totale `nan`; il divisore `len(sales)` conta anche le righe senza importo |
| 2 | Preparazione del modello | Data leakage: lo scaler è addestrato su tutto `X` prima dello split; mancano `random_state`, `test_size`, `stratify` |
| 3 | Filtro vendite Bikes | `and` non è valido tra Series (serve `&` con parentesi) |
| 4 | Funzione di report | Colonne selezionate con `iloc` per posizione: fragile e illeggibile; nomi poco chiari, nessuna docstring |

Il versioning è documentato nella sezione [Versioning con Git e GitHub](#versioning-con-git-e-github).

---

## Risultati documentati nel notebook

Valori riportati nei commenti del notebook (gli altri risultati si ottengono eseguendo le celle):

- `Quantity` e `SalesAmount`: circa 5% di NaN ciascuna (100 record su 2000).
- Categoria con il fatturato più alto: **Outdoor**, con 331.998,4 €, valore coerente tra Task 1 e Task 3b.
- Ultima data presente nel dataset: 2025-12-30; soglia per `Recente` (180 giorni prima): 2025-07-03.
- Media di `SalesAmount` calcolata sulle vendite con importo valido: circa 294,78 €.
- Clustering: k scelto con il gomito = 3.

---

## Istruzioni di esecuzione

### 1. Requisiti
- Python 3.9 o superiore
- Jupyter Notebook, JupyterLab o VS Code con l'estensione Jupyter

### 2. Clona la repository
```bash
git clone https://github.com/<tuo-utente>/<nome-repository>.git
cd <nome-repository>
```

### 3. (Consigliato) Crea un ambiente virtuale
```bash
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 4. Installa le dipendenze
```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn openpyxl jupyter
```

`openpyxl` serve a `pd.read_excel()` per leggere il file `.xlsx` delle regioni.

Se usi Anaconda, la maggior parte dei pacchetti è già inclusa; potrebbe mancare solo `plotly`:
```bash
conda install -c plotly plotly
```

### 5. Verifica i file dei dati
I quattro file `ESERCIZIO_M4-4-2_traccia_finale-*` devono trovarsi nella **stessa cartella del notebook**, perché il codice li legge con percorsi relativi.

### 6. Avvia il notebook
```bash
jupyter notebook
```
Apri il file `.ipynb` ed esegui le celle **dall'alto verso il basso** (`Shift + Invio`).

---

## Note importanti sull'esecuzione

- **Ordine delle celle:** le celle dipendono l'una dall'altra (ad esempio `final_merge`, `monthly`, `mensile`, `X`, `y` vengono riusati più avanti). Esegui il notebook in ordine; se riavvii il kernel, riparti dall'inizio.
- **Celle del Task 7:** contengono volutamente il **codice originale con errori**. Il Caso 3 usa `df`, che nel notebook non esiste, e dà errore. Il Caso 2 usa `X` e `y`, che a quel punto hanno il valore dell'ultimo task. Se usi "Esegui tutto", queste celle possono interrompere l'esecuzione: eseguile singolarmente o saltale.
- **Variabili `sales` e `Sales`:** nel Task 3a l'istruzione `Sales = sales` crea un secondo nome per lo **stesso** oggetto, non una copia. L'imputazione di `Quantity` si riflette quindi anche su `sales`; la successiva `dropna()` crea invece un nuovo DataFrame. Per una vera copia di backup usa `Sales = sales.copy()`.
- **Warning su Windows:** `KMeans` e `joblib` possono mostrare avvisi su memory leak (MKL) e sul conteggio dei core fisici. Sono innocui. Per eliminarli, esegui all'inizio del notebook, prima di importare scikit-learn:
  ```python
  import os
  os.environ["OMP_NUM_THREADS"] = "2"
  os.environ["LOKY_MAX_CPU_COUNT"] = "4"   # numero di core del tuo PC
  ```
- **Grafici Plotly:** se non compaiono in Jupyter, imposta
  ```python
  import plotly.io as pio
  pio.renderers.default = "notebook"   # oppure "browser", "vscode"
  ```
- **Riproducibilità:** gli split e i modelli usano `random_state=42`, quindi i risultati sono ripetibili.
- **Interpretazione:** i nomi dei cluster (fedeli, occasionali, a rischio) sono assegnati guardando i profili; le etichette numeriche 0, 1, 2 sono arbitrarie e possono cambiare se cambiano dati o impostazioni.

---

## Versioning con Git e GitHub

Flusso minimo per pubblicare il progetto:

```bash
git init
git add README.md <nome_del_notebook>.ipynb
git add ESERCIZIO_M4-4-2_traccia_finale-*
git commit -m "Aggiunge notebook, dataset e README"
git branch -M main
git remote add origin https://github.com/<tuo-utente>/<nome-repository>.git
git push -u origin main
```

Per le modifiche successive, usa commit piccoli con messaggi chiari (ad esempio `Corregge gestione NaN nel Caso 1`).

---

## Autore

**Andrea Marcucci**
Corso AI & Data Analytics, Epicode Institute of Technology

