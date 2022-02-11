-- Create a database
create database db_name;

-- Drop a database
drop database db_name;

-- Create a table
create table table_name (
    id int primary key auto_increment,
    title varchar(255),
    decription text()
);

-- Drop a table
drop table table_name;

-- Alter a table
alter table table_name
add is_complete column_name;

-- Constraint
not null, unique, primary key, foreign key


-- CRUD

-- create
insert into table_name (column_name1, column_name2, ...)
values (value1, value2, ...)

-- read
select * from table_name

-- update
update table_name
set column_name = value
where condition

-- delete
delete from table_name where condition

-- Select
-- Distinct
-- Where
-- Order by
-- Update
-- Delete
-- Min, Max, Count, Avg, SUm
-- Like
-- Joins
-- Having