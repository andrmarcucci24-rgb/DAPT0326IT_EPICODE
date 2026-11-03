import shutil

# Due copie del database: una per Development, una per Production
shutil.copy("ecommerce.duckdb", "ecommerce_dev.duckdb")
shutil.copy("ecommerce.duckdb", "ecommerce_prod.duckdb")

print("Create le copie: ecommerce_dev.duckdb e ecommerce_prod.duckdb")
