-- created_at: 2026-11-03T19:56:33.571898600+00:00
-- finished_at: 2026-11-03T19:56:33.573695600+00:00
-- elapsed: 1ms
-- outcome: success
-- dialect: duckdb
-- node_id: not available
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "connection_name": "", "dbt_version": "2.0.0", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */

    
    select schema_name
    from system.information_schema.schemata
    
    where lower(catalog_name) = '"ecommerce_prod"'
    
  
  ;

-- created_at: 2026-11-03T19:56:33.574400500+00:00
-- finished_at: 2026-11-03T19:56:33.575038700+00:00
-- elapsed: 638us
-- outcome: success
-- dialect: duckdb
-- node_id: not available
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "connection_name": "", "dbt_version": "2.0.0", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */

    
        select type from duckdb_databases()
        where lower(database_name)='ecommerce_prod'
        and type='sqlite'
    
  ;

-- created_at: 2026-11-03T19:56:33.575335700+00:00
-- finished_at: 2026-11-03T19:56:33.575619600+00:00
-- elapsed: 283us
-- outcome: success
-- dialect: duckdb
-- node_id: not available
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "connection_name": "", "dbt_version": "2.0.0", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */

    
    
        create schema if not exists "ecommerce_prod"."main"
    ;

-- created_at: 2026-11-03T19:56:33.598171400+00:00
-- finished_at: 2026-11-03T19:56:33.605401700+00:00
-- elapsed: 7ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_orders
-- query_id: not available
-- desc: get_relation > list_relations call
SELECT table_catalog, table_schema, table_name, table_type FROM information_schema.tables WHERE table_schema = 'main' AND lower(table_catalog) = lower('ecommerce_prod');

-- created_at: 2026-11-03T19:56:33.595640700+00:00
-- finished_at: 2026-11-03T19:56:33.605402300+00:00
-- elapsed: 9ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_products
-- query_id: not available
-- desc: get_relation > list_relations call
SELECT table_catalog, table_schema, table_name, table_type FROM information_schema.tables WHERE table_schema = 'main' AND lower(table_catalog) = lower('ecommerce_prod');

-- created_at: 2026-11-03T19:56:33.596012600+00:00
-- finished_at: 2026-11-03T19:56:33.607996200+00:00
-- elapsed: 11ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_customers
-- query_id: not available
-- desc: get_relation > list_relations call
SELECT table_catalog, table_schema, table_name, table_type FROM information_schema.tables WHERE table_schema = 'main' AND lower(table_catalog) = lower('ecommerce_prod');

-- created_at: 2026-11-03T19:56:33.594679900+00:00
-- finished_at: 2026-11-03T19:56:33.608217100+00:00
-- elapsed: 13ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_orders_items
-- query_id: not available
-- desc: get_relation > list_relations call
SELECT table_catalog, table_schema, table_name, table_type FROM information_schema.tables WHERE table_schema = 'main' AND lower(table_catalog) = lower('ecommerce_prod');

-- created_at: 2026-11-03T19:56:33.614963500+00:00
-- finished_at: 2026-11-03T19:56:33.624285100+00:00
-- elapsed: 9ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_orders
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.ecommerce_dev_prod.stg_orders", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */

  
    
    
    create  table
      "ecommerce_prod"."main"."stg_orders__dbt_tmp"
  
    as (
      select
    *,
    'prod' as ambiente
from "ecommerce_prod"."main"."raw_orders"
    );
  
    
  ;

-- created_at: 2026-11-03T19:56:33.616991900+00:00
-- finished_at: 2026-11-03T19:56:33.625945100+00:00
-- elapsed: 8ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_orders_items
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.ecommerce_dev_prod.stg_orders_items", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */

  
    
    
    create  table
      "ecommerce_prod"."main"."stg_orders_items__dbt_tmp"
  
    as (
      select * from "ecommerce_prod"."main"."raw_order_items"
    );
  
    
  ;

-- created_at: 2026-11-03T19:56:33.618766200+00:00
-- finished_at: 2026-11-03T19:56:33.631532200+00:00
-- elapsed: 12ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_customers
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.ecommerce_dev_prod.stg_customers", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */

  
    
    
    create  table
      "ecommerce_prod"."main"."stg_customers__dbt_tmp"
  
    as (
      select * from "ecommerce_prod"."main"."raw_customers"
    );
  
    
  ;

-- created_at: 2026-11-03T19:56:33.619044900+00:00
-- finished_at: 2026-11-03T19:56:33.633298900+00:00
-- elapsed: 14ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_products
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.ecommerce_dev_prod.stg_products", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */

  
    
    
    create  table
      "ecommerce_prod"."main"."stg_products__dbt_tmp"
  
    as (
      select * from "ecommerce_prod"."main"."raw_products"
    );
  
    
  ;

-- created_at: 2026-11-03T19:56:33.630571800+00:00
-- finished_at: 2026-11-03T19:56:33.636342500+00:00
-- elapsed: 5ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_orders
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.ecommerce_dev_prod.stg_orders", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */
alter table "ecommerce_prod"."main"."stg_orders__dbt_tmp" rename to "stg_orders";

-- created_at: 2026-11-03T19:56:33.631347100+00:00
-- finished_at: 2026-11-03T19:56:33.637749200+00:00
-- elapsed: 6ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_orders_items
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.ecommerce_dev_prod.stg_orders_items", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */
alter table "ecommerce_prod"."main"."stg_orders_items__dbt_tmp" rename to "stg_orders_items";

-- created_at: 2026-11-03T19:56:33.635668500+00:00
-- finished_at: 2026-11-03T19:56:33.639841800+00:00
-- elapsed: 4ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_products
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.ecommerce_dev_prod.stg_products", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */
alter table "ecommerce_prod"."main"."stg_products__dbt_tmp" rename to "stg_products";

-- created_at: 2026-11-03T19:56:33.634577600+00:00
-- finished_at: 2026-11-03T19:56:33.641367600+00:00
-- elapsed: 6ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_customers
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.ecommerce_dev_prod.stg_customers", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */
alter table "ecommerce_prod"."main"."stg_customers__dbt_tmp" rename to "stg_customers";

-- created_at: 2026-11-03T19:56:33.640446200+00:00
-- finished_at: 2026-11-03T19:56:33.641929700+00:00
-- elapsed: 1ms
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_orders
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.ecommerce_dev_prod.stg_orders", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */

      drop table if exists "ecommerce_prod"."main"."stg_orders__dbt_backup" cascade
    ;

-- created_at: 2026-11-03T19:56:33.642181400+00:00
-- finished_at: 2026-11-03T19:56:33.642669800+00:00
-- elapsed: 488us
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_orders_items
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.ecommerce_dev_prod.stg_orders_items", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */

      drop table if exists "ecommerce_prod"."main"."stg_orders_items__dbt_backup" cascade
    ;

-- created_at: 2026-11-03T19:56:33.644008+00:00
-- finished_at: 2026-11-03T19:56:33.644689100+00:00
-- elapsed: 681us
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_products
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.ecommerce_dev_prod.stg_products", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */

      drop table if exists "ecommerce_prod"."main"."stg_products__dbt_backup" cascade
    ;

-- created_at: 2026-11-03T19:56:33.645787900+00:00
-- finished_at: 2026-11-03T19:56:33.646463500+00:00
-- elapsed: 675us
-- outcome: success
-- dialect: duckdb
-- node_id: model.ecommerce_dev_prod.stg_customers
-- query_id: not available
-- desc: execute adapter call
/* {"app": "dbt", "dbt_version": "2.0.0", "node_id": "model.ecommerce_dev_prod.stg_customers", "profile_name": "ecommerce_dev_prod", "target_name": "prod"} */

      drop table if exists "ecommerce_prod"."main"."stg_customers__dbt_backup" cascade
    ;

