## Download and Setup database from [here](https://dev.mysql.com/doc/index-other.html)

- Create a database
- First import schema
- Import data


## Key terminology

- schema
- table
- primary key, foreign key
- foreign key constraints
    - blog database
    - posts table (id, title)
    - comments table (id, body, post_id)
    - orphan record
    - ```sql
        alter table comments 
        add foreign key (post_id) references posts(id)
        on delete cascade/restrict/set null
    ```
 - joins 
    - join (inner join default)
    - left join (left outer join)
    - right join (right outer join)
    - ```sql
        select * from store
        join address 
        on store.address_id = address.address_id
    ```
    
- aggrgate 
    - count, sum, min, max, avg
    - group by
    ```sql
        select  
            customer.customer_id, customer.first_name, customer.last_name, count(rental.rental_id) rentals_checked_out
        from customer
        left join rental
        on rental.customer_id = customer.customer_id
        group by customer.customer_id
    ```
    - more group by, subquery
    ```sql
        select  
            customer.customer_id, 
            customer.first_name, 
            customer.last_name, 
            count(rental.rental_id) as rentals_checked_out,
            address.address as store_address
        from customer
        left join rental
        on rental.customer_id = customer.customer_id
        left join address
        on address.address_id = (
            select address_id from store where store.store_id = customer.store_id
        )
        group by customer.customer_id, address.address
    ```
    - without subquery
    ```sql
        select  
            customer.customer_id, 
            customer.first_name, 
            customer.last_name, 
            count(rental.rental_id) as rentals_checked_out,
            address.address as store_address
        from customer
        left join rental
        on rental.customer_id = customer.customer_id
        left join store
        on store.store_id = customer.store_id
        left join address
        on address.address_id = store.address_id
        group by customer.customer_id, address.address
    ```

- relationship
    - one to one
        - user -> profile
    - one to many
        - user -> post
    - many to many, linking table, pivot table
        - post -> tag