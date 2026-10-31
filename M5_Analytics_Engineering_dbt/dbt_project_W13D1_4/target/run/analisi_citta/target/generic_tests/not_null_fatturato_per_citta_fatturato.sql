
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select fatturato
from "flusso"."main"."fatturato_per_citta"
where fatturato is null



  
  
      
    ) dbt_internal_test