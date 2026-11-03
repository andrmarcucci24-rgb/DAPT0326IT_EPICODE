import duckdb

# Leggo da ciascun database la colonna "ambiente" scritta da dbt in stg_orders
for nome in ["ecommerce_dev.duckdb", "ecommerce_prod.duckdb"]:
    con = duckdb.connect(nome, read_only=True)
    print(f"=== stg_orders IN {nome} ===")
    con.sql("""
        SELECT ambiente, COUNT(*) AS righe
        FROM stg_orders
        GROUP BY ambiente
    """).show()
    con.close()
