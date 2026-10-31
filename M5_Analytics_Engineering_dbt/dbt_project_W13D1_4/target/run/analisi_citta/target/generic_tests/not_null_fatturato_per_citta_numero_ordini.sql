
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select numero_ordini
from "flusso"."main"."fatturato_per_citta"
where numero_ordini is null



  
  
      
    ) dbt_internal_test