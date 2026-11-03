import os
import duckdb

# Nuovo database in un formato leggibile anche da dbt
con = duckdb.connect("flusso_v2.duckdb", config={"storage_compatibility_version": "v1.2.0"})

# Copio le due tabelle dal file originale (aperto in sola lettura)
con.execute("ATTACH 'flusso.duckdb' AS origine (READ_ONLY)")
con.execute("CREATE TABLE clienti AS SELECT * FROM origine.clienti")
con.execute("CREATE TABLE ordini AS SELECT * FROM origine.ordini")

con.sql("SHOW TABLES").show()
con.close()

# Sostituisco il vecchio file con quello convertito
os.replace("flusso_v2.duckdb", "flusso.duckdb")
print("Fatto")
