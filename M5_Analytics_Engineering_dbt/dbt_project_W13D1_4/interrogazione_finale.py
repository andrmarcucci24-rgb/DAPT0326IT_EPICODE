import duckdb

con = duckdb.connect("flusso.duckdb", read_only=True)

# Il modello dbt è una normale tabella del database
print("Modello dbt: tabella fatturato_per_citta")
con.sql("SELECT * FROM fatturato_per_citta").show()

# La stessa query dell'esercizio 2, scritta direttamente sulle tabelle di origine
query_equivalente = """
    SELECT c.city,
           ROUND(SUM(o.amount), 2) AS fatturato,
           COUNT(*) AS numero_ordini
    FROM ordini AS o
    JOIN clienti AS c
      ON o.customer_id = c.customer_id
    GROUP BY c.city
    ORDER BY fatturato DESC
"""
print("Query SQL equivalente, senza dbt")
con.sql(query_equivalente).show()

# Confronto: righe presenti in un risultato e non nell'altro (in entrambe le direzioni)
solo_dbt = con.sql(f"SELECT * FROM fatturato_per_citta EXCEPT ({query_equivalente.replace('ORDER BY fatturato DESC', '')})").fetchall()
solo_sql = con.sql(f"({query_equivalente.replace('ORDER BY fatturato DESC', '')}) EXCEPT SELECT * FROM fatturato_per_citta").fetchall()
print("Righe solo nel modello dbt:", len(solo_dbt))
print("Righe solo nella query SQL:", len(solo_sql))
print("I risultati coincidono" if not solo_dbt and not solo_sql else "ATTENZIONE: risultati diversi")

con.close()
