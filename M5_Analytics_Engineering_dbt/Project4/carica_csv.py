import duckdb

# Database in formato leggibile anche da dbt (come in converti_db.py del Giorno 1)
con = duckdb.connect("ecommerce.duckdb", config={"storage_compatibility_version": "v1.2.0"})

# Tabella da creare -> file CSV da cui prendere i dati (raw_ = dati grezzi)
csv_per_tabella = {
    "raw_orders": "orders.csv",
    "raw_customers": "customers.csv",
    "raw_products": "products.csv",
    "raw_order_items": "order_items.csv",
}

# read_csv legge il file, CREATE TABLE ... AS SELECT lo trasforma in una tabella
for tabella, file_csv in csv_per_tabella.items():
    con.execute(f"""
        CREATE OR REPLACE TABLE {tabella} AS
        SELECT * FROM read_csv('{file_csv}')
    """)

print("=== TABELLE ===")
con.sql("SHOW TABLES").show()
print("\n=== NUMERO DI RIGHE ===")
con.sql("""
    SELECT 'raw_orders' AS tabella, COUNT(*) AS righe FROM raw_orders
    UNION ALL
    SELECT 'raw_customers', COUNT(*) FROM raw_customers
    UNION ALL
    SELECT 'raw_products', COUNT(*) FROM raw_products
    UNION ALL
    SELECT 'raw_order_items', COUNT(*) FROM raw_order_items
""").show()

con.close()
