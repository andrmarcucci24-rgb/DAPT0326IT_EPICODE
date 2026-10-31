import duckdb

# Apro il database di dbt in sola lettura (lo script sta nella cartella del progetto, accanto a flusso.duckdb)
con = duckdb.connect("flusso.duckdb", read_only=True)

# La stessa logica del test unique: i customer_id che compaiono più di una volta
print("=== 1. CLIENTI CON PIÙ DI UN ORDINE (i valori che fanno fallire unique) ===")
con.sql("""
    SELECT customer_id, COUNT(*) AS n_ordini
    FROM ordini
    WHERE customer_id IS NOT NULL
    GROUP BY customer_id
    HAVING COUNT(*) > 1
    ORDER BY customer_id
""").show()

# Gli ordini dietro quei valori
print("\n=== 2. GLI ORDINI DI QUEI CLIENTI ===")
con.sql("""
    SELECT order_id, customer_id, order_date, amount
    FROM ordini
    WHERE customer_id IN (
        SELECT customer_id FROM ordini GROUP BY customer_id HAVING COUNT(*) > 1
    )
    ORDER BY customer_id, order_date
""").show()

con.close()
