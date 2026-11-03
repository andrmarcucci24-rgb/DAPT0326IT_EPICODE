import duckdb

# Apro il database in sola lettura (lo script sta accanto a ecommerce.duckdb)
con = duckdb.connect("ecommerce.duckdb", read_only=True)

# La stessa logica di assert_order_amount_consistency, con la differenza calcolata
print("=== 1. ORDINI CON IMPORTO INCOERENTE ===")
con.sql("""
    SELECT order_id, quantity, unit_price, amount,
           quantity * unit_price AS atteso,
           amount - quantity * unit_price AS differenza
    FROM raw_orders
    WHERE ABS(amount - quantity * unit_price) > 0.01
""").show(max_width=200)

# La stessa logica di assert_no_negative_unit_price
print("\n=== 2. ORDINI CON PREZZO UNITARIO NEGATIVO ===")
con.sql("""
    SELECT order_id, customer_id, status, quantity, unit_price, amount,
           quantity * unit_price AS atteso
    FROM raw_orders
    WHERE unit_price < 0
""").show(max_width=200)

# Un controllo in più: quanti ordini rispettano la regola dell'importo
print("\n=== 3. QUANTI ORDINI RISPETTANO LA REGOLA DELL'IMPORTO ===")
con.sql("""
    SELECT COUNT(*) AS ordini_totali,
           COUNT(*) FILTER (WHERE ABS(amount - quantity * unit_price) <= 0.01) AS coerenti,
           COUNT(*) FILTER (WHERE ABS(amount - quantity * unit_price) > 0.01) AS incoerenti
    FROM raw_orders
""").show()

con.close()
