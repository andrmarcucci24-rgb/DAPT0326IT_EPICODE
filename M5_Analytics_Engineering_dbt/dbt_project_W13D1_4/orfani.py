import duckdb

# Apro il database di dbt in sola lettura (lo script sta nella cartella del progetto, accanto a flusso.duckdb)
con = duckdb.connect("flusso.duckdb", read_only=True)

# Ordini il cui customer_id non esiste nella tabella clienti
print("=== ORDINI SENZA UN CLIENTE CORRISPONDENTE ===")
con.sql("""
    SELECT o.order_id, o.customer_id, o.order_date, o.amount
    FROM ordini AS o
    LEFT JOIN clienti AS c ON o.customer_id = c.customer_id
    WHERE c.customer_id IS NULL
    ORDER BY o.order_id
""").show()

con.close()
