README – Log delle operazioni svolte e analisi dati finale



ESERCIZIO 1.
 
file prezzi:
- creo backup file: file_backup e file_clean
- eliminato tutte le righe null con Removed blank rows
- eliminato le prime due righe con Remove Top Rows per mancanza di dati esempio di variabile presente "xxx"
- promosso l'attuale prima riga come intestazione usando Use First Row as Headers
- cambiato il tipo di formato delle colonne: città in text e prezzo medio in currency con change type
- usato la currency italiana perché le città sono italiane
- check colonna città con menù a tendina per vedere se c'è qualcosa di strano 
- trim e clean per sicurezza nella colonna text 
- standardizzato nomi città con Capitalize each Word
- check colonna prezzo medio per vedere se c'è qualcosa di strano
- eliminato colonna 2 per assenza di dati con Remove Columns
- check se ci sono duplicati nella tabella 

file strutture_ricettive:
- creo backup file: file_backup e file_clean
- promosso la prima riga come intestazione usando Use First Row as Headers
- check del type delle colonne
- trim e clean delle colonne Città e Denominazione 
- standardizzato i nomi con Capitalize Each Word Città e Denominazione
- check delle colonne per vedere se c'è qualche nome strano nelle due colonne 

RISULTATO ESERCIZIO 1: 
- Foglio prezzi_clean
- Foglio prezzi_backup (foglio nascosto nel file)
- Foglio strutture_ricettive_clean
- Foglio strutture_ricettive_backup (foglio nascosto nel file)




ESERCIZIO 2. 

left_join:
- Merge Queries as new
- scelto quali dataset far parlare: Strutture_ricettive_clean con prezzi_clean 
- scelto la chiave: Città 
- fatto un left outer
- scelto quale variabile espandere: PREZZO MEDIO 
- Riordinato le colonne così che per ogni struttura sia associato il prezzo della sua città, non ci sono strutture alle quali non è associato un prezzo, perché con il merge le variabili nella chiave "Città" matchavano tutte
- Rinomita la colonna "PREZZO MEDIO" eliminando i riferimenti al dataset "prezzi" per standardizzare

RISULTATO ESERCIZIO 2: 
- Forglio left_join_backup




ESERCIZIO 3.
 
- duplicato la tabella mergiata per avere un backup file: file_left_joi_backup e file_left_join_operativo
- standardizzato la colonna Categoria con Capitalize Each Word
- Check della colonna per vedere la presenza di cose strane
- Group By Città e Categoria -> contato il numero di strutture usando Group By advanced scegliendo per quali colonne raggruppare e quale operazione svolgere (count)

RISULTATO ESERCIZIO 3:
- Foglio left_join_operativo




ESERCIZII 4 e 5. 

- creato nuovo sheet "liste"
- estratto tutti i nomi delle strutture combinando le funzioni =SORT() e =UNIQUE() dalla tabella left_join_backup
- creato menu a tendina in B3 che fa riferimento allo sheet "liste" con lo strumento Data Validation scegliendo in allow la voce list dandogli poi le specifiche di "liste"
- utilizzato la funzione =XLOOKUP() per estrarre da left_join_backup in base al nome della struttura presente in B3 la variabile che fa riferimento alla colonna A (CITTA', INDIRIZZO, EMAIL, INDIRIZZO WEB)
- gestendo i valori mancanti con "not found missing data"
- utilizzato la funzione =COUNTA() per ottenere il numero totale di strutture da left_join_backup
- utilizzato la funzione =COUNTIFS() per ottenere il numero di strutture per località da left_join_backup in base al variare della variabile città in B4 con il menu a tendina in B3

RISULTATI ESERCIZIO 4 e 5:
- Foglio liste
- Foglio RICERCA




ESERCIZIO 6. 

- creato sheet "elenco_categorie" 
- estratto le categorie ed il numero di strutture per ogni categoria combinando più funzioni dinamiche in un'unica formula dal dataset left_join_operativo: 
   - =UNIQUE() prende le categorie uniche 
   - =COUNTIFS() conta quante strutture appartengono a ciascuna categoria
   - =HSTACK() affianca l'elenco delle categorie con il numero di strutture associato
   - =SORT() ordina in base al numero di strutture in ordine decrescente

- estratto un'area libera dalla tabella left_join_operativo, combinando:
   - =FILTER() per estrarre le strutture appartenenti alla città associata 
   - =SORTBY() ordinare il risultato in base alla categoria
- estratto l'elenco delle città uniche nello sheet "liste" combinando =SORT() E =UNIQUE()
- creato menu a tendina per selezionare la città dinamicamente in D24 che fa riferimento allo sheet "liste" con lo strumento Data Validation scegliendo in allow la voce list dandogli poi le specifiche di "Lista città" nello sheet "liste"
- creato tabella dinamica che si aggiorna al cambiare la città dal menù a tendina sotto la voce "Elenco città"

RISULTATO ESERCIZIO 6:
- Foglio elenco_categorie




ESERCIZIO 7, 8 e 9.

- esercizi svolti nel foglio "prezzi_clean"
- calcolato Media, Mediana, Moda, Varianza, Deviazione standard, Q1 e Q3 con le rispettive funzioni
- calcolato IQR con la formula =Q3-Q1 ed i limiti di Tukey: inferiore =Q1-(1.5*IQR) e superiore =Q3+(1.5*IQR) per valutare l'eventuale presenza di outlier
- per controllare se ci fossero valori oltre i limiti di Tukey ho utilizzato una formula con funzioni annidate =IF() =COUNTIF() mettendo come condizione di restituire "no outlier" o "si outlier" se interrogando la colonna PREZZO MEDIO vengono riscontrati valori oltre i due limiti
 
- costruito la tabella frequenze: 
  - definito le classi usando la funzione =MIN() e =MAX() per ottenere il prezzo minimo e il prezzo massimo nella colonna "PREZZI MEDI"
  - scelto di dividere in 4 classi per comodità
  - definito l'ampiezza delle classi calcolando la differenza tra prezzo minimo e prezzo massimo combinando con la  funzione =ROUND() per arrotondare in eccesso 
  - estratto il limite superiore di ogni classe per la colonna limiti con la funzione =VALUE() 
  - calcolato frequenza assoluta e frequenza relativa con =FREQUENCY() combinata con =TAKE() per estrarre i 4 valori
  - estratto la classe modale con la funzione =INDEX() combinata con =MATCH() e =MAX() che cerca ed estrae la classe più frequente
  - costruito un istogramma che rappresenta la distribuzione delle frequenze relative dei prezzi medi per ogni classe di prezzo 

RISULTATI e COMMENTI ESERCIZIO 7, 8 e 9:
- tabella statistica descrittiva 
- tabella di frequenze
- istogramma  
- sulla base dei dati di statica descrittiva ottenuti la distribuzione appare approssimativamente simmetrica, poiché la media (73,5) coincide con la mediana (73,5).
- la classe modale individuata, in seguito all'analisi della distribuzione dei prezzi medi per classe di prezzo, è quella che comprende i valori che vanno da 30 a 52. 
- Inoltre, l'analisi degli outlier svolta secondo il criterio dei limiti di Tukey non evidenzia la presenza di valori anomali.



ESERCIZIO 10.

- esercizio svolto nel foglio "probabilità"
- estratto da left_join_backup il numero totale di strutture con =COUNTA(), il numero totale di alberghi e B&B con =COUNTIF()
- calcolato la probabilità che estraendo casualmente venga fuori un albergo =totale Alberghi/Totale strutture
- calcolato la probabilità che estraendo casualmente venga fuori un B&B = totale B&B/Totale strutture
- calcolato la probabilità che su due lanci indipendenti esca tutte e due le volte albergo =P(albergo)^2
- il risultato visualizzato è 0 (1/64) perché la cella è nel formato frazione ed il numero è molto piccolo 

RISULTATI ESERCIZIO 10: 
- P(albergo) = 1/8
- P(B&B) = 2/7
- P(2 alberghi) = 1/64



ESERCIZIO 11. 

- esercizio svolto nel foglio "probabilità"
- usando i dati di statistica descrittiva ricavati negli esercizi precedenti mi sono calcolato i limiti superiori e inferiori entro ± 1 e 2 deviazioni standard dalla media =media ± deviazione standard e =media ± 2*deviazione standard
- stimato la quota di città con prezzo medio entro ±1σ usando la funzione =NORM.DIST(limite superiore;media;σ;T) - NORM.DIST(limite inferiore;media;σ;T) e lo stesso per la quota entro ±2σ

RISULTATI e COMMENTO ESERCIZIO 11:
- quota di città entro ±1σ 68%
- quota di citta entro ±2σ 95% 
- Assumendo che i prezzi medi siano distribuiti normalmente, si stima che circa il 68% delle città abbia un prezzo medio compreso entro ±1 deviazione standard dalla media e circa il 95% entro ±2 deviazioni standard.



ESERCIZIO 12. 

- esercizio svolto nel foglio "probabilità"
- creato piccola tabella dinamica con menù a tendina per poter selezionare la città che si preferisce, presa dalla lista precedentemente creata che si trova nel foglio "liste" tramite il Data Validation
- estratto con la funzione =XLOOKUP() il prezzo medio facendo riferimento alla cella in cui c'è la città selezionata dal menù a tendina 
- calcolato lo z score con la funzione =STANDARDIZE()
- calcolato la probabilità di trovare un prezzo inferiore con la funzione =NORM.S.DIST()

RISULTATI E COMMENTO ESECIZIO 12.
 
- lo z-score misura la distanza del prezzo medio della città selezionata rispetto alla media dei prezzi, espresso in deviazioni standard. Pertanto, in base alla città selezionata si ottiene uno z score > 0 nel caso di un prezzo superiore alla media e < 0 nel caso di un prezzo inferiore alla media. 
- con =NORM.S.DIST() ho calcolato la probabilità cumulata associata allo z score stimando la quota di città con un prezzo inferiore o uguale a quello della città selezionata.
- di conseguenza città con z score > 0 hanno una probabilità cumulata più alta, mentre città con z score < 0 hanno una probabilità cumulata più bassa

ESEMPIO ESERCIZIO 12:    

selezionando in maniera interattiva la città di Corinaldo la tabellina restituisce un prezzo medio pari a 75 e calcola lo z score pari a 0.05. Questo valore indica che il prezzo medio di Corinaldo è leggermente superiore alla media complessiva dei prezzi delle città. La probabilità cumulata è pari al 52%, pertanto ci dice che circa il 52% delle città presenta un prezzo medio inferiore o uguale a quello di Corinaldo. Sempre assumendo si tratti di una distribuzione normale dei prezzi medi delle città. 


ESERCIZIO 13.
 
- esercizio svolto nel foglio "inferenza_confronto_tra_gruppo"
- generato una tabella pivot in un nuovo foglio "inferenza_confronto_tra_gruppi" a partire dalla tabella presente nel foglio "prezzi_clean"
- calcolato l'inferenza tramite la media con =AVERAGE(), la σ con =STDEV.S() poiché le città sono trattate come campione, ed N con =COUNT(). 
- calcolato alpha con la formula =1-confidenza, in questo caso al 95%
- calcolato errore standard della media dividendo la deviazione standard campionaria per la radice quadrata del numero di città combinando =σ/SQRT(N)
- calcolato il margine di errore con =CONFIDENCE.NORM()
- calcolato i limiti superiore e inferiore sommando e sottraendo alla medie il margine di errore 

RISULTATI ESERCIZIO 13:
 
- l'intervallo di confidenza al 95% ottenuto per il prezzo medio delle città, indica che, con un livello di confidenza del 95%, il prezzo medio della popolazione stimato è compreso tra 69.97 e 77.03.


ESERCIZIO 14. 

- esercizio svolto nel foglio "inferenza_confronto_tra_gruppo"
- fatto lo stesso lavoro dell'esercizio precedente cambiando il livello di confidenza nelle altre due tabelline rispettivamente al 90 e al 99% 

RISULTATI ESERCIZIO 14: 

- l'intervallo di confidenza al 90% ottenuto per il prezzo medio delle città, indica che, con un livello di confidenza del 90%, il prezzo medio della popolazione stimato è compreso tra 76.46 e 70.54.
- l'intervallo di confidenza al 99% ottenuto per il prezzo medio delle città, indica che, con un livello di confidenza del 99%, il prezzo medio della popolazione stimato è compreso tra 78.13 e 68.87.
- Si può notare che, all'aumentare del livello di confidenza, aumenta anche il margine di errore e l'intervallo di confidenza si amplia. Di conseguenza, aumenta la probabilità che l'intervallo contenga il vero prezzo medio della popolazione. Viceversa, diminuendo il livello di confidenza, il margine di errore si riduce e l'intervallo diventa più stretto, diminuendo la probabilità di contenere il vero prezzo medio della popolazione. 
- Quadruplicando la numerosità campionaria, il margine di errore si dimezza, poiché è inversamente proporzionale alla radice quadrata della numerosità del campione. Di conseguenza, l'intervallo di confidenza diventa più stretto e la stima del prezzo medio della popolazione risulta più precisa.


ESERCIZIO 15. 

- esercizio svolto nel foglio "TEST_ipotesi_A_B"
- generato una tabella pivot dal foglio "left_join_backup"
- impostato le città in Rows, in values è stato inserito il prezzo medio, mentre le categorie sono state utilizzate come colonne, ottenendo il prezzo medio distinto per ciascuna categoria (Alberghi e Agriturismi)
- filtrato con il menu a tendina per alberghi e agriturismi
- estratto con la funzione =FILTER() solo le città che presentano un prezzo medio per entrambe le categorie prese in esame: Alberghi e Agriturismi
- impostato l'ipotesi:
  - definito i Gruppi: A e B
  - definito H0 -> nessuna differenza
  - definito H1 -> differenza rilevante 
  - definito code -> 2 (perché la traccia non parla di maggiore o minore)
  - calcolato il p-value -> usando la funzione =T.TEST()

RISULTATO ESERCIZIO 15: 

- È stato effettuato un t-test a due code per dati appaiati, considerando come unità di analisi la città. Il p-value ottenuto è pari a 0.46, superiore al livello di significatività α = 0,05. Pertanto non si rifiuta l'ipotesi nulla (H0): non vi sono evidenze statistiche sufficienti per affermare che il prezzo medio delle città con alberghi sia significativamente diverso dal prezzo medio delle città con agriturismi. 



ESERCIZIO 16. 

- esercizio svolto nel foglio "Relazioni_tra_variabili"
- generato una tabella pivot dal foglio "left_join_backup", come righe ho impostato le città, e in values ho messo la conta delle categorie per città e la somma dei prezzi medi per città. 
- generato una tabellina dove calcolo la covarianza con la funzione =COVARIANCE.S() ed il coefficiente di correlazione con =CORREL()

RISULTATO ESERCIZIO 16: 
- covarianza -> 11.27 (positiva)
- r -> 0.0010
- La covarianza positiva indica una lieve tendenza delle due variabili a muoversi nella stessa direzione, tuttavia il coefficiente di correlazione pari a 0,0010, essendo prossimo allo zero, evidenzia l'assenza di una relazione lineare significativa tra il numero di strutture presenti in una città e il suo prezzo medio. Pertanto, nel campione analizzato, sulla base dei dati ottenuti, il numero di strutture non sembra essere associato a variazioni sistematiche del prezzo medio.



ESERCIZIO 17.

- Esercizio svolto nel foglio "regressione".
- Copiati e incollati i dati relativi al numero di strutture e al prezzo medio dalla pivot generata nel foglio "Relazioni_tra_variabili", poiché Excel non consente di generare direttamente uno scatter plot a partire da una tabella pivot.
- Generato il diagramma di dispersione (scatter plot) e aggiunta la linea di tendenza lineare, visualizzando anche l'equazione della retta e il valore di R² tramite le impostazioni del grafico.
- Applicato il ToolPak di Excel per eseguire la regressione lineare e analizzare R², Significance F e p-value del coefficiente. 

RISULTATI ESERCIZIO 17: 

- Il modello di regressione non risulta significativo: il valore di R² è praticamente nullo e il p-value (0,9509) è maggiore di 0,05. Pertanto, il numero di strutture non sembra avere una relazione lineare significativa con il prezzo medio delle città.

ESERCIZIO 18. 

- esercizio svolto nel foglio "regressione"
- generato un tabellina "previsione e limiti" dove con la retta di regressione ottenuta stimiamo il prezzo medio di una città con 156 strutture. 

RISULTATI ESERCIZIO 18: 

- Utilizzando il modello di regressione ottenuto, è stato stimato il prezzo medio di una città considerando un determinato numero di strutture (156). La previsione è stata effettuata tramite l'equazione della retta di regressione: Prezzo medio=73.435+0.002189*Numero strutture.
- Un limite della previsione è che il modello presenta un R² praticamente nullo e non risulta statisticamente significativo, quindi il numero di strutture non è una variabile informativa per prevedere il prezzo medio. 
 







