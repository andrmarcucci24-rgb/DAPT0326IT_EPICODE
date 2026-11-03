import duckdb
 
# ------------------------------------------------------------------
# 0. Ricreo i CSV del Giorno 2 (ricostruzione: i dati originali della traccia non erano disponibili)
#    Le prime 5 righe di orders coincidono con l'output atteso della guida.
#    Anomalie inserite di proposito:
#      - 2016: amount (150) diverso da quantity * unit_price (3 * 40 = 120)  -> test di coerenza
#      - 2008: unit_price negativo                                           -> test prezzo negativo
#      - 2010: customer_id vuoto
#      - 2012: customer_id 106, che non esiste in customers.csv
#      - 2014: quantity vuota (il test di coerenza non la vede: NULL non è né uguale né diverso)
#      - riga del 17/09: order_id vuoto
# ------------------------------------------------------------------
orders_csv = """order_id,customer_id,order_date,status,quantity,unit_price,amount
2001.0,101.0,2026-09-01,completed,2,25.0,50.0
2002.0,102.0,2026-09-02,shipped,1,120.0,120.0
2003.0,101.0,2026-09-03,placed,3,15.0,45.0
2004.0,103.0,2026-09-04,returned,1,80.0,80.0
2005.0,104.0,2026-09-05,completed,4,10.0,40.0
2006.0,105.0,2026-09-06,completed,2,35.0,70.0
2007.0,102.0,2026-09-07,shipped,5,8.0,40.0
2008.0,103.0,2026-09-08,completed,1,-30.0,-30.0
2009.0,104.0,2026-09-09,placed,2,45.0,90.0
2010.0,,2026-09-10,completed,3,20.0,60.0
2011.0,101.0,2026-09-11,shipped,1,60.0,60.0
2012.0,106.0,2026-09-12,completed,2,12.5,25.0
2013.0,105.0,2026-09-13,returned,6,5.0,30.0
2014.0,102.0,2026-09-14,completed,,18.0,36.0
2015.0,103.0,2026-09-15,placed,2,22.0,44.0
2016.0,104.0,2026-09-16,completed,3,40.0,150.0
,105.0,2026-09-17,shipped,1,55.0,55.0
2018.0,101.0,2026-09-18,completed,4,9.5,38.0
"""
 
customers_csv = """customer_id,customer_name,city
101,Marco Rossi,Milano
102,Giulia Bianchi,Roma
103,Luca Verdi,Milano
104,Anna Neri,Torino
105,Sara Gallo,Roma
"""
 
with open("orders.csv", "w", encoding="utf-8", newline="") as f:
    f.write(orders_csv)
with open("customers.csv", "w", encoding="utf-8", newline="") as f:
    f.write(customers_csv)
 
# ------------------------------------------------------------------
# 1. Da qui in poi è lo script della guida, invariato
# ------------------------------------------------------------------
 
# Creo il database in un formato leggibile anche da dbt (come in converti_db.py dell'esercizio 4 del Giorno 1)
con = duckdb.connect("ecommerce.duckdb", config={"storage_compatibility_version": "v1.2.0"})
 
# read_csv legge il file (riga di intestazione e tipi riconosciuti da DuckDB),
# CREATE TABLE ... AS SELECT lo trasforma in una tabella
con.execute("CREATE OR REPLACE TABLE raw_orders AS SELECT * FROM read_csv('orders.csv')")
con.execute("CREATE OR REPLACE TABLE raw_customers AS SELECT * FROM read_csv('customers.csv')")
 
print("=== TABELLE ===")
con.sql("SHOW TABLES").show()
print("\n=== STRUTTURA DI raw_orders ===")
con.sql("DESCRIBE raw_orders").show(max_width=200)
print("\n=== PRIME RIGHE DI raw_orders ===")
con.sql("SELECT * FROM raw_orders LIMIT 5").show(max_width=200)
print("\n=== NUMERO DI RIGHE ===")
con.sql("""
    SELECT 'raw_orders' AS tabella, COUNT(*) AS righe FROM raw_orders
    UNION ALL
    SELECT 'raw_customers', COUNT(*) FROM raw_customers
""").show()
 
con.close()