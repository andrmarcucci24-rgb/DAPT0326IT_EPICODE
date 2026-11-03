import duckdb

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
