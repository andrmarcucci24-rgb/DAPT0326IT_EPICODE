### 1. Esplorare e analizzare dati con duckdb e python

# importo la libreria 
import duckdb

# mi connetto ad un db locale 
con = duckdb.connect("vendite.duckdb")

# creo una tabella con le colonne order_id, customer_id, order_date, product, quantity, unit_price
con.execute("""
    CREATE OR REPLACE TABLE orders (
        order_id    INTEGER,
        customer_id INTEGER,
        order_date  DATE,
        product     VARCHAR,
        quantity    INTEGER,
        unit_price  DECIMAL(10, 2)
    )
""")

# controllo se la struttura della tabella è quella che volevo 
con.sql("DESCRIBE orders").show()

# popolo la tabelle con i dati 
con.execute("""
INSERT INTO orders (order_id, customer_id, order_date, product, quantity, unit_price) VALUES
(1001, 1, '2026-01-05', 'Laptop',           1, 899.99),
(1002, 2, '2026-01-07', 'Mouse',            2,  19.90),
(1003, 3, '2026-01-12', 'Tastiera',         1,  49.50),
(1004, 1, '2026-01-15', 'Monitor 27"',      2, 229.00),
(1005, 4, '2026-01-20', 'Webcam',           1,  59.99),
(1006, 5, '2026-02-02', 'Cuffie',           3,  39.90),
(1007, 2, '2026-02-09', 'Laptop',           1, 949.00),
(1008, 6, '2026-02-14', 'Hub USB-C',        4,  24.50),
(1009, 3, '2026-02-18', 'Monitor 27"',      1, 219.00),
(1010, 7, '2026-02-25', 'Mouse',            1,  21.50),
(1011, 1, '2026-03-03', 'Tastiera',         2,  47.00),
(1012, 8, '2026-03-08', 'Laptop',           2, 879.00),
(1013, 4, '2026-03-11', 'Cuffie',           1,  42.00),
(1014, 5, '2026-03-19', 'Webcam',           2,  57.50),
(1015, 9, '2026-03-27', 'Hub USB-C',        1,  26.00),
(1016, 2, '2026-04-01', 'Monitor 27"',      1, 235.00),
(1017, 6, '2026-04-06', 'Mouse',            3,  18.90),
(1018, 10, '2026-04-13', 'Tastiera',        1,  52.00),
(1019, 3, '2026-04-21', 'Cuffie',           2,  38.50),
(1020, 7, '2026-04-30', 'Laptop',           1, 925.00)
""")

# interrogo per vedere se il popolamento è andato bene e il numeor totale di righe 
con.sql("SELECT * FROM orders LIMIT 5").show()
con.sql("SELECT COUNT(*) AS totale_record FROM orders").show()


# visualizzo il numero di righe e verifico il numero totoale di record
con.sql("""
     SELECT 
        COUNT(*) AS righe 
     FROM orders
""").show()

# calcolo il fatturato complessivo moltiplicando quantità per prezzo unitario 
con.sql("""
    SELECT 
        SUM(quantity * unit_price) AS fatturato_totale
    FROM orders 
""").show()

# calcolo il fatturato complessivo moltiplicando quantità per prezzo unitario 
con.sql("""
    SELECT
        product,
        SUM(quantity * unit_price) AS fatturato
    FROM orders
    GROUP BY product
    ORDER BY fatturato DESC
""").show()

# conteggio degli ordini presenti per ciascun cliente 
con.sql("""
    SELECT
        customer_id,
        COUNT(order_id) as numero_ordini
    FROM orders
    GROUP BY customer_id
""").show()

# chiudo la connessione 
con.close()

# DATA WAREHOUSE: è un'architettura ELT creata per rendere disponibili dati provenienti da fonti differenti per attività di analisi e reporting 
# oltre ad essere un luogo di storage dei dati è anche l'ambiente in cui vengono eseguite molte delle trasformazioni che li rendono utili.
# E' un sistema centralizzato e condiviso, pensato per grandi volumi di dati (es. Amazon Redshift)

# DuckDB è un db analitico open source progettato per eseguire query SQL e operazioni di analisi dei dati in modo efficiente, 
# senza ricorrere necessariamente a un server database separato, gira dentro il programma che lo usa (esempio un script python con import duckdb)
# i dati stanno in un singolo file locale (in questo caso vendite.duckdb)

# Entrambi servono per le analisi, tuttavia cambia architettura, scala e ruolo, poiché uno gira in locale sulla macchina di chi lo usa, l'altro è una piattamforma centrale in un'azienda condivisa da più utenti. 



