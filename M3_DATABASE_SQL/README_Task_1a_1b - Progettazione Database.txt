README - Progettazione Database (ToysGroup) - Task 1a/1b

Task 1a - Progettazione concettuale 
OBIETTIVO: individuare le entità dello scenario ToysGroup e le relazioni tra loro in uno schema Entità/relazione

RELEZIONI E CARDINALITA'

- Product/Sales: 1:N un prodotto compare in una o più vendite e ogni vendita è riferita esattamente ad un prodotto.
- Region/Sales: 1:N una regione ha una o più transazioni e ogni transazione è riferita ad una regione 

- Category include Product: 1:N una categoria raggruppa più prodotti e ogni prodotto appartiene ad una categoria 
- State include Region: 1:N uno stato è associato a una regione e una regione può includere più stati. 

Task 1b - Progettazione Logica 
OBIETTIVO: Tradurre lo schema concettuale in tabelle relazionali, con tutte le colonne e le chiavi esterne. 

- Lo schema logico è composto da 3 tabelle: Product, Region e Sales. Le tabelle Category e State non sono più tabelle separate ma sono attributi di Product e Region, rispettivamente, come richiesto dalla consegna. Questo perché a livello logico non serve isolare Category e State in tabelle proprie perché non hanno attributi propri oltre a CategoryName e StateName, quindi li ho 'assorbiti' nelle tabelle Product e Region. 

- Ogni Tabella ha un'unica chiave primaria (ProductID, RegionID, SalesID). 
- Ogni FK referenzia una PK esistente. 
