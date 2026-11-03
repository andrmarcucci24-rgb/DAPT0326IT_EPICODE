import duckdb

# Per ciascun database elenco le tabelle presenti (apertura in sola lettura)
for nome in ["ecommerce_dev.duckdb", "ecommerce_prod.duckdb"]:
    con = duckdb.connect(nome, read_only=True)
    print(f"=== TABELLE IN {nome} ===")
    con.sql("SHOW TABLES").show()
    con.close()
