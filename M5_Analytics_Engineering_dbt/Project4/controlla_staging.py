import duckdb

# Apro il database in sola lettura (lo script sta accanto a ecommerce.duckdb)
con = duckdb.connect("ecommerce.duckdb", read_only=True)

print("=== NUMERO DI RIGHE DEI MODELLI ===")
con.sql("""
    SELECT 'stg_orders' AS modello, COUNT(*) AS righe FROM stg_orders
    UNION ALL
    SELECT 'stg_customers', COUNT(*) FROM stg_customers
    UNION ALL
    SELECT 'stg_products', COUNT(*) FROM stg_products
    UNION ALL
    SELECT 'stg_order_items', COUNT(*) FROM stg_order_items
""").show()

print("\n=== COLONNE E TIPI DI stg_orders ===")
con.sql("SELECT column_name, column_type FROM (DESCRIBE stg_orders)").show()

con.close()
