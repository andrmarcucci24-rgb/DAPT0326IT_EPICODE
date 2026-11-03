import duckdb 
 
# Apro il database in sola lettura: dbt ha già creato la tabella 
con = duckdb.connect("flusso.duckdb", read_only=True) 
 
print("Tabelle nel database:") 
con.sql("SHOW TABLES").show() 
 
print("Contenuto del modello fatturato_per_citta:") 
con.sql("SELECT * FROM fatturato_per_citta").show() 
 
con.close() 