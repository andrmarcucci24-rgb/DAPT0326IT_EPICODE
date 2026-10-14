### Tipo di problema e preparazione dei dati
## Esercizio 1 - Dati: df con clienti di almeno 200 righe generati con Numpy (np.random.seed(42)): mesi, reclami, spesa (numeriche), contratto (mensile, annuale, biennale), churn (0/1, circa 15% di valori 1)
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.metrics import (confusion_matrix, classification_report,
                             roc_auc_score, RocCurveDisplay)
import matplotlib.pyplot as plt

rng = np.random.default_rng(42) # questo è il generatore di numeri casuael 

n = 250 # numero clienti 

# genero il df 
clienti = pd.DataFrame({
    "mesi": rng.integers(
        1, 
       73, 
       n   # qui gli dico di prendere i mesi dal generatore casuale nel formato intero da 1 a 72 
    ),
    "reclami": rng.poisson(
        0.8, 
        n   # qui gli dico di generarmi numeri intera da una distribuzione di poisson presi sempre da rng
    ),
    "spesa": rng.uniform(
        20, 
        140, 
        n # qui prende i numeri casuali da rng da 20 a 140
    ), 
    "contratto": rng.choice(
        ["Mensile", "Annuale", "Biennale"],
        size = n,
        p = [0.55, 0.30, 0.15], # qui gli ho detto di scegliere casualmente fra queste 3 categorie dividendo casualmente il numero di clienti presi da n con p che indica la probabilità di ogni categoria 
    ),
    "churn" : rng.binomial(
        1,       # gli sto dicendo fare una singola prova per cliente, che in questo caso se 0 allora non abbandona se 1 allora abbandona il servizio (che sarebba la probabilità di successo in questo caso) 
        0.15,    # probabilità di successo (abbandono del servizio) pari al 15%
        size = n   # prendendo i dati dalla nostra serie di numeri 
    )
})

print(clienti.head())

# 1. classificare tre casi (fatturato del mese successivo, reso di un ordine si/no, gruppi di negozi simili) come regressione, classificazione o clustering indicandon la colonna target 

# target = fatturato -> regressione, in quanto voglio prevedere quanto fatturerà il negozio il mese successivo 
# target = reso -> classificazione,  vado ad assegnare una osservazione ad una classe, voglio prevedere se il risultato è si (fatto reso), no (non fatto il reso)
# target = negozi simili -> clustering, in questo caso vado a raggruppare i negozi sulla base di caratteristiche simili (fatturato, contratto ecc) individuando i gruppi di negozi maggiormente simili tra loro 

# 2. applicare pd.get_dummies alla colonna contratto con drop_first = True e dtype = int, poi separare X (feature) e y (churn)

# .get_dummies() trasforma una variabile categorica in numerica
new_df = pd.get_dummies(clienti,
               columns = ["contratto"], # seleziono la colonna 
               drop_first = True, # elimina la prima categoria dell'ordinamento la usa come categoria di riferimento, in questo caso autunnale che però implicitamente rimane perché ve diamo in df 0 sotto biennale e 0 sotto mensile dello stesso cliente il contratto è annuale
               dtype = int        # trasforma in numeri 0 e 1 anziché in booleani
)


# la variabile target è churn, quindi quella che voglio prevedere, quindi la variabile dipendente

X = new_df.drop(columns=["churn"]) # gli dico di escludere la colonna di churn
y = new_df["churn"]

print(X.shape)
print(y.shape)

# 3. dividere i dati con train_test_split() e verificare se le medie tra train e test coincidono 

X_train, X_test, y_train, y_test = train_test_split(
    X,                  
    y,                  
    test_size=0.20,     
    stratify=y,         
    random_state=42,    
)

# la quota di churn coincidie 

y_train.mean() # np.float64(0.15)
y_test.mean()  # np.float64(0.14)

# 4. standardizzare le feature con StandardScaler: fit_transform() su X_train, transform() su X_test
from sklearn.preprocessing import StandardScaler

# creo l'oggetto scaler 
scaler = StandardScaler()

# Calcolo media e deviazione standard sul training set
# e standardizzo le feature di X_train
X_train_scaled = scaler.fit_transform(X_train) 

# fit() clacola media e dev st di ogni feature usando esclusivamente X_train
# transform() utilizza questi parametri per standardizzare i dati 

# Standardizzo X_test usando i parametri calcolati su X_train
X_test_scaled = scaler.transform(X_test)

# su X_test si usa solo transform perché devo applicare le stesse medie e dev st calcolate sul training set 
# usando fit_transform()anceh sul test set calcolerebbe nuovi parametri basati sui dati test 

# verifico se le dimensioni coincidono 
print(X_train_scaled.shape)
print(X_test_scaled.shape)

## Definizione: scrivere la definizione di data leakage e spiegare perché lo scaler non va addestrato sull'intero dataset
# Data leakage: si verifica quando informazioni del test set (o non disponibili  al momento della previsione) entrano nel processo di addestramento, anche indirettamente tramite il preprocessing. Le prestazioni misurate risultano così ottimistiche e non si ripetono su dati realmente nuovi.
# Lo scaler non va addestrato sull'intero dataset perché media e deviazione standard includerebbero anche i dati di test: il modello "vedrebbe" in anticipo informazioni che dovrebbero restare sconosciute, e il test non simulerebbe più dati mai visti. Per questo: fit solo su X_train, poi transform su entrambi.

### Regressione Logistica per il churn
## Esercizio 2 - X_train, X_test, y_train e y_test dell'esercizio precedente 

# 1. con il modello z = -1,0 + 0,6 reclami - 0,04 mesi calcolare a mano z e p per un cliente con 4 reclami e 12 mesi, poi verificare il risultato in python con una funzione sigmoide
z_model = -1.0
reclami = 4
mesi = 12

# z
z = z_model + 0.6 * reclami - 0.04 * mesi

# + 0.6 reclami = più reclami, z più alto, più churn
# - 0.04 mesi: più anzianità, z più basso, meno churn 

print(z) # 0.9199999999999999 -> il cliente con 4 reclami e 12 mesi ha il 71,5% di porbabilità di abbandonare 

# p 
def sigmoide(z):
    return 1 / (1 + np.exp(-z))

print(sigmoide(z)) # 0.7150421057009897

# Perché la sigmoide:
# La regressione lineare può dare qualsiasi numero, mentre una probabilità sta tra 0 e 1. 
# il modello calcola prima un punteggio lineare come una regressione normale, poi lo schiaccia tra 0,1 con la sigmoide.

# 2. addestrre LogisticRegression(max_iter=1000) con fit su X_train_scaled e y_train e ottenere le classi previste con predict su X_test_scaled
from sklearn.linear_model import LogisticRegression

# Creo il modello
model = LogisticRegression(max_iter=1000)

# Addestro il modello sui dati di training
model.fit(X_train_scaled, y_train)

# Previsione delle classi: il modello è addestrato su dati scalati,
# quindi va usato X_test_scaled
y_pred = model.predict(X_test_scaled)
print(y_pred)

# 3. Probabilità di churn (colonna 1 = classe 1) e conteggio con due soglie
prob_churn = model.predict_proba(X_test_scaled)[:, 1]

n_05 = (prob_churn >= 0.5).sum()   # True conta come 1, quindi sum() conta i clienti
n_03 = (prob_churn >= 0.3).sum()
print("Churn previsti con soglia 0.5:", n_05) # Churn previsti con soglia 0.5: 0
print("Churn previsti con soglia 0.3:", n_03) # Churn previsti con soglia 0.3: 0


# 4. costruire òa series dei coefficienti con index=X.columns, calcolare gli odds ratio con np,exp() e ordinarli con sort_value()
# Coefficienti, odds ratio e ordinamento
coef = pd.Series(model.coef_[0], index=X.columns)   # coef_ ha shape (1, n_feature)
odds_ratio = np.exp(coef).sort_values(ascending=False)
print(odds_ratio)


## Definizione: odds ratio e spiegare perché la regressione logistica è un algoritmo di classificazione 
# Odds ratio: rapporto tra gli odds (p / (1-p)) dopo e prima di un aumento di una unità di una feature, a parità delle altre. È pari a exp(coefficiente).
# OR > 1: la feature aumenta le probabilità di churn; OR < 1: le riduce; OR = 1: nessun effetto.

# La regressione logistica è un algoritmo di classificazione perché la variabile target è categorica (0/1). Il modello stima la probabilità di appartenere alla classe 1 tramite la sigmoide e poi assegna la classe confrontando la
# probabilità con una soglia (di default 0.5). Il nome "regressione" deriva dal fatto che internamente regredisce i log-odds su una combinazione lineare delle feature.

### Metriche di valutazione e overfitting 
## Esercizio 3 - Dati: modello y_pred e probabilità dell'esercizio 2; costo di un falso positivo 20 euro e costo di un falso negativo 300 euro

# 1. calcolare confusion_matrix(y_test, y_pred), riportare TN, FP, FN e TP e verificare che la loro somma coincida con le righe del test set 
conf = confusion_matrix(y_test, y_pred)
print(conf)

# [[43  0] qui ci sta dicendo il numeor di clienti che non abbandonano e il modella ha previsto (TN), FP 0 ci dice nessun falso allarme il cliente non ha mai detto abbandona- a un cliente che poi è rimasto 
# [ 7  0]] 7 FN clienti che hanno abbandonato davvero ma il modello ha detto resta, sono i mancati allarmi, cioè i clienti persi senza che tu potessi fare nulla, 0 TP nessun cliente a rischio individuato

# la somma 43+0+7+0 = 50 cioè le righe del test set, quindi il controllo del punto 1 è soddisfatto 

# 2. Metriche a mano, ricavate dalla matrice di confusione
TN, FP, FN, TP = conf.ravel()

accuracy = (TP + TN) / (TP + TN + FP + FN)
# Precision = TP/(TP+FP) = 0/0: indefinita perché il modello non prevede mai churn.
# Per convenzione la pongo a 0.
precision = TP / (TP + FP) if (TP + FP) > 0 else 0
recall = TP / (TP + FN) if (TP + FN) > 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
print(f"Accuracy: {accuracy:.2f}, Precision: {precision:.2f}, Recall: {recall:.2f}, F1: {f1:.2f}")

# Confronto con sklearn
print(classification_report(y_test, y_pred, zero_division=0))

# Baseline: prevedere sempre 0
baseline = (y_test == 0).mean()
print("Accuracy baseline:", baseline)
# L'accuracy coincide con la baseline: il modello non aggiunge nulla rispetto a "nessuno abbandona".

# 3. Costo degli errori con le due soglie
def costo(soglia):
    y_s = (prob_churn >= soglia).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_test, y_s, labels=[0, 1]).ravel()
    return fp * 20 + fn * 300

costo_05 = costo(0.5)
costo_03 = costo(0.3)
print("Costo soglia 0.5:", costo_05)
print("Costo soglia 0.3:", costo_03)
# Se i due costi sono uguali, nessuna soglia è migliore: lo scrivo nel commento.

# 4. calcolare roc_auc_score(y_test, proba), disegnare la curva con RocCurvwDisplay e conforntare model.score() su train e test per diagnosticare underfitting o overfitting
# AUC: misura quanto bene il modello mette i clienti che abbandonano sopra quelli che restano nella classifica di probabilità, indipendentemente dalla soglia
print("AUC:", roc_auc_score(y_test, prob_churn))
RocCurveDisplay.from_predictions(y_test, prob_churn)
plt.plot([0, 1], [0, 1], "k--")    # linea del caso casuale

print("Score train:", model.score(X_train_scaled, y_train))
print("Score test :", model.score(X_test_scaled, y_test))

# Il modello prevede sempre 0: accuracy 0.86 uguale alla baseline, ma recall 0
# sulla classe churn. Le soglie 0.5 e 0.3 danno lo stesso costo (2100 euro),
# quindi nessuna è migliore. AUC = 0.53, vicino al caso. Score train (0.85) e
# test (0.86) simili: nessun overfitting. Il modello non apprende nulla di utile
# perché il churn è stato generato in modo casuale, indipendente dalle feature.

## Definizione: definizione di precision e di recall e indicare quale delle due va priviligiata nel churn e perché 
# Precision: tra i clienti previsti come churn, la quota che abbandona davvero
# = TP / (TP + FP). Risponde a: "quando il modello dà l'allarme, quanto è affidabile?"
#
# Recall: tra i clienti che abbandonano davvero, la quota individuata dal modello
# = TP / (TP + FN). Risponde a: "quanti clienti a rischio riesco a trovare?"
#
# Nel churn va privilegiata la recall: un falso negativo (cliente perso senza
# averlo segnalato) costa 300 euro, un falso positivo (offerta data a un cliente
# che sarebbe rimasto) ne costa 20. Conviene accettare più falsi allarmi pur di
# individuare il maggior numero possibile di clienti a rischio. La precision resta
# comunque da monitorare, per non spendere troppo in campagne di retention inutili.

