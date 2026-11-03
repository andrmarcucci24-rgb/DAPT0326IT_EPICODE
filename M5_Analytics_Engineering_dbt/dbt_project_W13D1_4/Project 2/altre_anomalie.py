import duckdb

con = duckdb.connect("ecommerce.duckdb", read_only=True)

# Anomalie che i due test personalizzati NON vedono
print("=== ALTRE ANOMALIE NEI DATI DI raw_orders ===")
con.sql("""
    SELECT 'order_id mancante' AS anomalia, COUNT(*) AS righe FROM raw_orders WHERE order_id IS NULL
    UNION ALL
    SELECT 'customer_id mancante', COUNT(*) FROM raw_orders WHERE customer_id IS NULL
    UNION ALL
    SELECT 'order_id duplicato', COUNT(*) FROM (
        SELECT order_id FROM raw_orders WHERE order_id IS NOT NULL
        GROUP BY order_id HAVING COUNT(*) > 1)
    UNION ALL
    SELECT 'cliente inesistente in raw_customers', COUNT(*)
    FROM raw_orders AS o
    WHERE o.customer_id IS NOT NULL
      AND o.customer_id NOT IN (SELECT customer_id FROM raw_customers)
    UNION ALL
    SELECT 'prezzo unitario uguale a zero', COUNT(*) FROM raw_orders WHERE unit_price = 0
    UNION ALL
    SELECT 'status fuori elenco', COUNT(*) FROM raw_orders
    WHERE status NOT IN ('placed', 'shipped', 'completed', 'returned')
""").show(max_width=200)

con.close()
