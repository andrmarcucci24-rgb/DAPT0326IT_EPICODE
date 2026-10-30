### 2. Creare un flusso di analisi dati con DuckDB
import duckdb

con = duckdb.connect("flusso.duckdb")

con.execute("""
    CREATE OR REPLACE TABLE clienti AS
    SELECT * FROM read_csv('clienti.csv')
""")

con.execute("""
    CREATE OR REPLACE TABLE ordini AS
    SELECT * FROM read_csv('ordini.csv')
""")

con.sql("SHOW TABLES").show()

# verificare il numero di record e i campi disponibili nelle due sorgenti 
con.sql("""
    SELECT 'clienti' AS tabella, COUNT(*) AS record FROM clienti
    UNION ALL
    SELECT 'ordini', COUNT(*) FROM ordini
""").show()

con.sql("DESCRIBE clienti").show()

con.sql("DESCRIBE ordini").show()

# visualizzo il contenuto delle due tabelle
con.sql("SELECT * FROM clienti").show()
con.sql("SELECT * FROM ordini").show()

# join tra ordini e clienti usando customer_id come chiave
con.sql("""
    SELECT o.order_id,
           o.order_date,
           o.amount,
           c.customer_id,
           c.customer_name,
           c.city
    FROM ordini AS o
    JOIN clienti AS c
      ON o.customer_id = c.customer_id
    ORDER BY o.order_id
""").show()

# query che calcola il fatturato e numero di ordini per città
con.sql("""
    SELECT c.city,
           ROUND(SUM(o.amount), 2) AS fatturato,
           COUNT(*) AS numero_ordini
    FROM ordini AS o
    JOIN clienti AS c
      ON o.customer_id = c.customer_id
    GROUP BY c.city
    ORDER BY fatturato DESC
""").show()

# cerco gli ordini che non trovano una corrispondenza nella tabella clienti 
con.sql("""
    SELECT o.order_id,
           o.customer_id,
           o.order_date,
           o.amount
    FROM ordini AS o
    LEFT JOIN clienti AS c
      ON o.customer_id = c.customer_id
    WHERE c.customer_id IS NULL
    ORDER BY o.order_id
""").show()

# chiudo connessione 
con.close()
