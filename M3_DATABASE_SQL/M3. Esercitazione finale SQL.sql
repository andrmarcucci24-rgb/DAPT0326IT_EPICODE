/*Task 2 - DDL: Creazione delle tabelle
Consegna: descrive la struttura delle tabelle utili a modellare lo scenario ToysGroup tramite sintassi DDL e implementare fisicamente in SQL Server (o DBMS equivalente)
creo le tabelle sviluppate a livello concettuale e logico con gli schemi del Task 1a e 1b */

-- Creo il mio database
create database ToysGroup;
use ToysGroup;

-- Creo Product
create table Product (
                      ProductID varchar(50) primary key,
                      ProductName varchar(50),
                      Category varchar(50)
);

-- Creo Region
create table Region ( 
                     RegionID varchar(50) Primary key, 
                     RegionName varchar(50),
					 State varchar(50)
);

-- Creo Sales
create table Sales (
                    SalesID int primary key, 
                    ProductID varchar(50), 
                    RegionID varchar(50), 
                    SalesDate date,
                    SalesQuantity int,
                    SalesAmount decimal(10,2),
foreign key(ProductID)          
         references Product(ProductID),   -- tra Product e Sales la cardinalità è 1:N
foreign key(RegionID)
		 references Region(RegionID)    -- tra Region e Sales la cardinalità è 1:N
);
 
 /* Task 3 - Popolamento dati
 Consegna: popolarele tabelle con dati a scelta: pochi record per tabella sono sufficienti
 1- inserire in product almeno 4 prodotti distribuiti su almeno 2 categori diverse.
 2- inserire in region almeno 3 stati ditribuiti su almeno 2 regioni di vendità.
 3 inserire in Sales almeno 10 transazioni distribuite su più anni per poter confrontare periodi diversi.
 Vincolo: ogni INSERT in Sales usa solo ProductID e RegionID già presenti nelle rispettive tabelle
 Criterio di completamento: le query INSERT utilizzate sono riportate insieme al risultato, non solo il dato finale. */
 
 -- Popolamento Product: 4 prodotti, 2 categorie (Bikes, Accessories)
insert into Product (ProductID, ProductName, Category) values
('bikes-100', 'mountain bike 26"', 'bikes'),
('bikes-200', 'road bike carbon', 'bikes'),
('acc-100', 'bike helmet', 'accessories'),
('acc-200', 'water bottle', 'accessories');

-- Popolamento Region: 3 stati, 2 regioni di vendita (westeurope, northamerica)
insert into Region (RegionID, RegionName, State) values
('we-fr', 'westeurope', 'france'),
('we-de', 'westeurope', 'germany'),
('na-us', 'northamerica', 'usa');

-- Popolamento Sales: 10 transazioni distribuite su più anni (2023-2025)
insert into Sales (SalesID, ProductID, RegionID, SalesDate, SalesQuantity, SalesAmount) values
(1,  'bikes-100', 'we-fr', '2023-01-15', 2, 450.00),
(2,  'bikes-200', 'we-de', '2023-03-22', 1, 1200.00),
(3,  'acc-100',   'na-us', '2023-06-10', 5, 125.00),
(4,  'acc-200',   'we-fr', '2023-09-05', 10, 80.00),
(5,  'bikes-100', 'na-us', '2024-02-11', 3, 675.00),
(6,  'bikes-200', 'we-fr', '2024-05-18', 2, 2400.00),
(7,  'acc-100',   'we-de', '2024-08-27', 8, 200.00),
(8,  'acc-200',   'na-us', '2024-11-30', 15, 120.00),
(9,  'bikes-100', 'we-de', '2025-01-09', 1, 225.00),
(10, 'bikes-200', 'na-us', '2025-04-14', 4, 4800.00);
 
 -- Check del risultato del popolamento 
 select * from Product;
 select * from Region;
 select * from Sales;
 
 /* Task 4a - Integrità e JOIN
 Consegna: verificare l'unicità delle chiavi primarie e costruire l'elenco delle transazioni con INNER JOIN
 1- Per ciascuna tabella, scrivere una query che verifichi l'univocità della chiave (una query per tabella).
 2- Con INNER JOIN  tra Sales, Product e Region, esporre codice prodotto, categoria, stato, regione di vendita e data per ogni transazione.
 3- Aggiungere una colonna Booleana: True se sono passati più di 180 giorni dalla data di vendita, false altrimenti.
 Attenzione: un INNER JOIN scarta le transazioni senza corrispondenza in product o Region: verificare che non manchi nessuna riga rispetto a Sales. 
 Criterio di completamento: il numero di righe del punto 2 coincide con il numero di righe Sales. */
 
 -- verifica dell'univocità delle chiavi primarie 
 -- Product
 select ProductID, 
		count(*) as occurrences
from Product
group by ProductID
having count(*) > 1;

-- Region
select RegionID, 
		count(*) as occurrences
from Region
group by RegionID
having count(*) > 1;

-- Sales
select SalesID, 
		count(*) as occurrences
from Sales
group by SalesID
having count(*) > 1;
  -- le query non restituiscono nessuna riga, non ci sono righe che condividono lo stesso valore, quindi la PK è univoca 
 
 -- INNER JOIN per esporre tutte quello che è richiesto dalle condizioni del punto 2
select 
    p.ProductID,      -- codice prodotto
    p.ProductName,
    p.Category,       -- categoria del prodotto (da Product)
    r.State,          -- stato di appartenenza della regione (da Region)
    r.RegionName,      -- regione di vendita
    s.SalesDate,       -- data della transazione
    s.SalesAmount      -- importo della transazione
from Sales as s
inner join Product as p on s.ProductID = p.ProductID   -- collega ogni vendita al suo prodotto
inner join Region as r  on s.RegionID = r.RegionID;    -- collega ogni vendita alla sua regione

-- Aggiunta della colonna Booleana
select 
    p.ProductID,      
    p.ProductName,
    p.Category,       
    r.State,          
    r.RegionName,      
    s.SalesDate,       
    s.SalesAmount,
    -- per aggiungere la colonna booleana faccio un subquery in select 
    case          
       when datediff((
              select max(SalesDate) 
              from Sales),
              s.SalesDate) > 180 then 'True'   -- gli dico che nel caso in cui la differenza in SalesDate sia superioe a 180 giorni dall'ultima vendita
		else 'False'       -- inserisci 'True' se inferiore 'False'
        end as More180Days
from Sales as s
inner join Product as p on s.ProductID = p.ProductID  
inner join Region as r  on s.RegionID = r.RegionID; 

/* Task 4b - Aggregazioni e raggruppamenti 
Consegna: calcolare il fatturato aggregato per diverse chiavi di analisi con GROUP BY e HAVING. 
1- Fatturato totale per prodotto e per anno (SUM(SalesAmount) raggruppato per ProductID e anno di SalesDate.
2- Fatturato totale per stato e per anno, ordinato per data e per fatturato decrescente. 
3- Categoria di prodotto più richiesta dal mecato, misurata come quantità totale venduta. 
Vincolo: l'anno si estrae dal campo data con una funzione built-in (es. YEAR(SaleseDate)), non scritto a mano.
Criterio di completamento: ogni query di raggruppamento riporta solo le colonne usate in GROUP BY e gli aggregati richiesti.
DA RICORDARE: HAVING filtra i gruppi dopo l'aggregazione; WHERE filtra le righe prima di raggruppare. Una condizione SUM o COUNT va sempre in HAVING. */

-- Fatturato totale per prodotto e per anno
select 
    p.ProductID,
    year(s.SalesDate) as SalesYear, -- estraggo soltanto l'anno con funzione built-in 
    sum(s.SalesAmount) as Total     -- estraggo la somma dell fatturato totale  
from Sales as s
inner join Product as p on s.ProductID = p.ProductID
group by p.ProductID,               -- raggruppo per prodotto
         year(s.SalesDate);         -- e per anno di vendita

-- Fatturato totale per stato e per anno, ordinato per data e per fatturato decrescente
select 
    r.State, 
    year(s.SalesDate) as SalesYear, 
    sum(s.SalesAmount) as Total
from Sales as s
inner join Region as r on s.RegionID = r.RegionID
group by r.State,              -- raggruppo per stato
         year(s.SalesDate)     -- e per anno di vendita
order by SalesYear,            -- ordino prima per data (anno)
         Total desc;           -- poi per fatturato decrescente
         
-- Categoria di prodotto più richiesta dal mecato, misurata come quantità totale venduta
select
    p.Category,
    sum(s.SalesQuantity) as TotalQuantitySold  -- somma le quantità vendute all'interno di ogni gruppo
from Sales as s
inner join Product as p on s.ProductID = p.ProductID
group by p.Category                -- crea gruppo per ogni categoria
order by TotalQuantitySold desc    -- ordina per categoria con più vendite 
limit 1;                           -- restituisce solo la categoria con più vendite, eliminando questa riga di codice come output si ottengono tutte le categorie ordinate in base alla quantità di vendite 
 
 /* Task 4c - Subquery e CTE
 Consegna: esporre i prodotti venduti con quantità totoale superiore alla media di vendita dell'ultimo anno censito, in due modi equivalenti. 
 1- Calcolare, con una subquery la quantità media venduta per prodotto nell'ultimo anno censito. 
 2- Usare la subquery del punto 1 in una condizione WHERE per filtrare i prodotti sopra la media. 
 3. riscrivere la stessa query con una CTE che isola il calcolo della media, richiamata dalla query principale. 
 Vincolo: il valore soglia (la media) deve risultare da una query, non deve essere inserito a mano. 
 Criterio di completamento: il result set riporta solo codice prodotto e totale venduto, identico tra la versione con subquery e quella con CTE.
 DA RICORDARE: una CTE non cambia il risultato rispetto a una subquery equivalente: cambia solo la leggibilità, isolando il calcolo con un nome. */

-- Quantità media venduta per prodotto, nell'ultimo anno censito
select 
     avg(TotalProduct) as MeanQuantitySold         -- la media, ossia il valore soglia, deriva dalla subquery in from
from (
-- subquery in from: calcola la quantità totale venduta per prodotto
select 
	 sum(SalesQuantity) as TotalProduct
from Sales
-- filtro where: tengo solo le righe dell'ultimo anno censito
where 
	year(SalesDate) = (select 
					   max(year(SalesDate))        -- subquery scalare: determina l'ultimo anno, calcolato dinamicamente
					   from Sales
)
group by ProductID                                 -- raggruppo per prodotto, come richiesto dalla consegna
) as SalesPerProduct;

-- in una condizione where filtrare i prodotti sopra la media usando la subquery precedente 
select
    ProductID,
    sum(SalesQuantity) as TotalProduct
from Sales
where 
year(SalesDate) = (select              -- solo l'ultimo anno censito
                   max(year(SalesDate)) 
                   from Sales)  
group by ProductID                     -- totale venduto per prodotto
having 
     sum(SalesQuantity) > (
-- subquery del punto 1: media della quantità totale per prodotto, nell'ultimo anno
                         select 
                         avg(TotalProduct)   -- media dei totali per prodotto
                         from ( 
-- tabella derivata: totale venduto per prodotto, nell'ultimo anno
                               select 
                               sum(SalesQuantity) as TotalProduct
                               from Sales
        where 
        year(SalesDate) = (select 
                           max(year(SalesDate)) 
                           from Sales)
group by ProductID
) as SalesPerProduct
);

-- stessa query del punto 2, riscritta con una CTE
-- che isola il calcolo della media (stesso risultato, solo più leggibile)
with mean_quantity as (
    select 
    avg(TotalProduct) as MeanQuantitySold
    from (
        select sum(SalesQuantity) as TotalProduct
        from Sales
        where year(SalesDate) = (select 
                                 max(year(SalesDate)) 
                                 from Sales)
group by ProductID) as SalesPerProduct
)
select
    ProductID,
    sum(SalesQuantity) as TotalProduct
from Sales
where 
year(SalesDate) = (select 
                   max(year(SalesDate)) 
                   from Sales)
group by ProductID
having sum(SalesQuantity) > (select 
                             MeanQuantitySold 
                             from mean_quantity);

/* Task 4d - Windows Function
Consegna: arricchire il result set delle transazioni con una classifica e un totale progressivo, senza perdere il dettaglio di riga.
1- Asseganre a ogni prodotto una posizione in classifica per fatturato totale, all'interno della prorpioa categoria. 
2- calcolare, per ogni transazione, il totoale progressivo del fatturato della regione fino a quella data.
3- Confrontare il fatturato di ogni transazione con quello della transazione precdente della stessa regione.
Vincolo: ogni risultato usa una funzione finestra con Partition By sulla chiave di raggruppamento e order by sul criterio richiesto, senza group by che comprima le righe.
Criterio di completamento: il result set mantiene una riga per transazione, con le colonne agiguntive di classifica e totale progressivo */

-- Asseganre a ogni prodotto una posizione in classifica per fatturato totale, all'interno della prorpioa categoria
with product_totals as (    -- Serve una CTE perché non si può annidare una window function dentro
    select 
        s.SalesID,
        s.ProductID,
        p.Category,
        s.SalesAmount,
        -- fatturato totale del prodotto: PARTITION BY sulla chiave (ProductID), nessun ORDER BY perché è una somma sull'intera partizione, non progressiva
        sum(s.SalesAmount) over (partition by s.ProductID) as ProductTotalRevenue
    from Sales as s
    inner join Product as p on s.ProductID = p.ProductID
)
select 
    SalesID,
    ProductID,
    Category,
    SalesAmount,
    ProductTotalRevenue,
    -- classifica: PARTITION BY sulla categoria (raggruppamento richiesto), ORDER BY sul fatturato totale del prodotto, decrescente
    rank() over (partition by Category order by ProductTotalRevenue desc) as RankInCategory
from product_totals;

-- calcolare, per ogni transazione, il totoale progressivo del fatturato della regione fino a quella data
select 
    s.SalesID,
    s.RegionID,
    r.RegionName,
    s.SalesDate,
    s.SalesAmount,
    -- totale progressivo: PARTITION BY sulla regione
    -- ORDER BY sulla data determina fino a dove sommare
    sum(s.SalesAmount) over (partition by s.RegionID order by s.SalesDate) as RunningTotalRegion
from Sales as s
inner join Region as r on s.RegionID = r.RegionID;

-- confrontare il fatturato di ogni transazione con quello della transazione precedente della stessa regione
select 
    s.SalesID,
    s.RegionID,
    s.SalesDate,
    s.SalesAmount,
-- LAG: recupera il valore di SalesAmount della riga precedente
-- per la prima transazione di ogni regione LAG restituisce NULL, perché non esiste una transazione precedente 
    lag(s.SalesAmount) over (partition by s.RegionID order by s.SalesDate) as PreviousSalesAmount,
-- differenza rispetto alla transazione precedente della stessa regione
    s.SalesAmount - lag(s.SalesAmount) over (partition by s.RegionID order by s.SalesDate) as DiffFromPrevious
from Sales as s;

/* Task 4e - Prodotti invenduti e VIEW
Consegna: individuare i prodotti mai venduti e creare due viste che espongano informazioni pronte per il reporting.
1- individuare i prodotti invenduti con un primo approccio a scelta (es. sottrazione o confronto di insiemi).
2- Risolvere la stessa domanda del punto 1 con un secondo approccio diverso dal primo. 
3- Creare una vista sui prodotti che esponga una versione denormalizzata con codice prodotto, nome prodotto e nome categoria.
4- Creare una vista per informazioni geografiche utile a chi analizza le vendite per area.
Attenzione: i due approcci del punto 1 e del punto 2 devono restituire lo stesso insieme di prodotti.
Criterio di completamento: le due viste sono interrogabili con una select * e non richiedono Join aggiuntivi da parte di chi le usa. */

-- individuare i prodotti invenduti con un primo approccio a scelta
-- unisco Product a Sales mantenendo TUTTI i prodotti (LEFT JOIN),
-- poi tengo solo le righe dove la JOIN non ha trovato corrispondenza (SalesID è NULL) 
select
     p.ProductID,
     p.ProductName,
     p.Category
from Product as p
left join Sales as s on p.ProductID = s.ProductID
where s.SalesID is null;

-- stessa cosa con approccio differente 
-- per ogni prodotto, verifico che NON esista nessuna riga in Sales
-- con lo stesso ProductID: nessun bisogno di JOIN, ragiona per subquery correlata
select 
    p.ProductID,
    p.ProductName,
    p.Category
from Product as p
where not exists (
    select 1
    from Sales as s
    where s.ProductID = p.ProductID
);
-- entrmabe le query restituiscono un result set vuoto perché perché tutti i pordotti risultano venduti almeno una volta.

-- VIEW denormalizzata con codice prodotto, nome prodotto e nome categoria
create view vw_product as
select 
    ProductID,
    ProductName,
    Category as CategoryName
from Product;

-- VIEW per informazioni geografiche
-- utile a chi analizza le vendite per area, senza dover fare JOIN
create view vw_sales_by_geography as
select 
    s.SalesID,
    s.SalesDate,
    s.SalesAmount,
    s.SalesQuantity,
    p.ProductID,
    p.ProductName,
    p.Category,
    r.RegionID,
    r.RegionName,
    r.State
from Sales as s
inner join Product as p on s.ProductID = p.ProductID
inner join Region as r on s.RegionID = r.RegionID;

-- interrogo le VIEW ottenendo subito le colonne utili senza dover scrivere altre JOIN che sono già dentro le VIEW
select * from vw_product;
select * from vw_sales_by_geography;

/* Governance & Privacy applicata
Consegna: le quattro strutture proposte violano una regola di Governance & Privacy nel modulo. 
Per Ciascuna, indicare la causa e proporre la versione corretta. */

-- Caso 1 vista pubblica
create view vw_prodotti_rivenditori as 
select ProductID, 
       ProductName, 
       Category, 
       PurchaseCost      -- essendo una vista pubblica destinata ai rivenditori PurchaseCost è un dato sensibile che non serve a nulla al rivenditore quindi io la correggerei eliminando quella riga.
from Product;

-- Versione corretta Caso 1
create view vw_prodotti_rivenditori as 
select ProductID, 
       ProductName, 
       Category 
from Product;

-- Caso 2 scheda fornitori
-- condivisa con il reparto marketing
create table supplierContact (
                      SupplierID int,
                      Phone Varchar(20)  -- siccome è condivisa con il reparto marketing magari questo dato personale è riferito a persone fisiche che quel reparto non può trattare 
);

-- versione corretta caso 2, separo l'accesso per ruolo
-- separo il dato sensibile in una tabella base,
-- ed espongo al marketing solo una vista priva del contatto personale
create table SupplierContact (
    SupplierID int primary key,
    Phone      varchar(20)
);

create view vw_supplier_public as
select SupplierID
from SupplierContact;

-- Caso 3 vista commerciale 
create view vw_sales_margine as
Select SalesID,
       SalesAmount,
       PurchaseCost, 
       Margin     -- PurchaseCost e Margin sono dati- economici sensibili e si trovano dentro una vista commerciale accessibile ad un pubblico ampio 
from Sales;

-- versione corretta caso 3
-- vista per il team commerciale: solo l'importo di vendita, nessun dato di costo/margine
create view vw_sales_commerciale as
select 
    SalesID,
    SalesAmount
from Sales;

-- vista con costo e margine, riservata a finance/management
create view vw_sales_margine_riservata as
select 
    SalesID,
    SalesAmount,
    PurchaseCost,
    Margin
from Sales;

-- Caso 4 log reporting
-- nessuna scadenza
Create Table ReportAccessLog (
                       UserID int, 
                       QueryText varchar(max), -- potrebbe contnere dati personali digitati nelle query senza nessuna scadenza di conservazione
                       AccessDate datetime);

-- versione corretta caso 4 
-- aggiungo una politica di retention esplicita
create table ReportAccessLog (
    UserID      int,
    QueryText   varchar(100),        -- varchar(max) non è sintassi MySQL, limitato a una lunghezza definita
    AccessDate  datetime,
    RetentionExpiry datetime          -- data oltre la quale il record va eliminato/archiviato
);

-- creo una VIEW che filtra in automatico i log più vecchi di 90 giorni impedendone la visualizzazione
-- per evitare di cancellare il dato grezzo, che magari potrebbe servire in futuro
create view vw_report_access_log_active as
select *
from ReportAccessLog
where AccessDate >= date_sub(curdate(), interval 90 day);

