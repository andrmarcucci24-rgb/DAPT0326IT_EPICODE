import duckdb

# Apro il database in sola lettura (lo script sta accanto a ecommerce.duckdb)
con = duckdb.connect("ecommerce.duckdb", read_only=True)

# Le tre colonne dell'esercizio, più il prodotto quantità x prezzo che useremo come regola
print("=== quantity, unit_price, amount DI TUTTI GLI ORDINI ===")
con.sql("""
    SELECT order_id,
           quantity,
           unit_price,
           amount,
           quantity * unit_price AS quantity_x_unit_price
    FROM raw_orders
    ORDER BY order_id
""").show(max_width=200, max_rows=30)

con.close()
