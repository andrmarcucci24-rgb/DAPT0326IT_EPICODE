
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select city
from "flusso"."main"."fatturato_per_citta"
where city is null



  
  
      
    ) dbt_internal_test