'''
Follows 12 rules: 

A) Rule 1: The information rule:
All information in a relational database is represented explicitly at the logical level and in exactly one way by values in tables.

B) Importance of Relational Databases:
- Standardization of data model: Once your data is transformed into the rows and columns format, your data is standardized and you can query it with SQL
- Flexibility in adding and altering tables: Relational databases gives you flexibility to add tables, alter tables, add and remove data.
- Data Integrity: Data Integrity is the backbone of using a relational database.
- Standard Query Language (SQL): A standard language can be used to access the data with a predefined language.
- Simplicity : Data is systematically stored and modeled in tabular format.
- Intuitive Organization: The spreadsheet format is intuitive but intuitive to data modeling in relational databases.

C) 
Online Analytical Processing (OLAP): Used for analysis => complex queries => total # of shoes sold(aggregate the data)
                               =>  complex analytical and ad hoc queries, including aggregations. => optimized for reads.

Online Transactional Processing (OLTP): Used for transactions => simple queries => price of shoes
                               => for less complex queries in large volume. Queries are read, insert, update, and delete.

D) Structuring the DB: 
Queries: 
1. Normalization: increase data integrity(queries must return correct answer) and reduce redundancy(copies) => goes through 3 normal forms
2. DeNormalization: to increase performance => there could be copies of data


E) Normalization: 
First Normal Form (1NF):

- Atomic values: each cell contains unique and single values => no set, list, tuple in a column
- Be able to add data without altering tables
- Separate different relations into different tables=> we don't want just 1 giant table that holds everything!
- Keep relationships between tables together with foreign keys => we need a way to keep the relationship between tables

Second Normal Form (2NF):

- Have reached 1NF
- All columns in the table must rely on the Primary Key

Third Normal Form (3NF):

- Must be in 2nd Normal Form
- No transitive dependencies => if there's a duplicate data in a column, break it down to 2 separate tables.

Remember, transitive dependencies you are trying to maintain is that to get from A-> C, you want to avoid going through B.
'''
#F) Exercise: 

    import psycopg2
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    cur = conn.cursor()
    conn.set_session(autocommit=True)

    cur.execute("CREATE TABLE IF NOT EXISTS music_store (transaction_id serial primary key, Customer_Name varchar, Cashier_Name varchar\
    , Year int, Albums_Purchased text[])")
    cur.execute("INSERT INTO music_store (transaction_id, Customer_Name, Cashier_Name\
    , Year, Albums_Purchased) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (1 , 'Amanda', 'Sam', 2000, ['Rubber Soul', 'Let it Be'])) 
    cur.execute("INSERT INTO music_store (transaction_id, Customer_Name, Cashier_Name\
    , Year, Albums_Purchased) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (2 , 'Toby', 'Sam', 2000, ['My Generation']))
    cur.execute("SELECT * FROM music_store;")

    row = cur.fetchone()

    while row:
       print(row)
       row = cur.fetchone()
# result: 
#Table Name: music_store
#column 0: Transaction Id
#column 1: Customer Name
#column 2: Cashier Name
#column 3: Year 
#column 4: Albums Purchased
# (1, 'Amanda', 'Sam', 2000, ['Rubber Soul', 'Let it Be'])
# (2, 'Toby', 'Sam', 2000, ['My Generation'])


# 1st normal form: list of songs => individual rows. 
## TO-DO: Complete the CREATE table statements and INSERT statements

cur.execute("CREATE TABLE IF NOT EXISTS music_store4 (transaction_id int, Customer_Name varchar,\
     Cashier_Name varchar, Year int, Albums varchar)")


#    cur.execute("CREATE TABLE IF NOT EXISTS music_store2 (#####);")

cur.execute("INSERT INTO music_store4 (transaction_id, Customer_Name, Cashier_Name\
    , Year, Albums) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (1 , 'Amanda', 'Sam', 2000, 'Rubber Soul'))

cur.execute("INSERT INTO music_store4 (transaction_id, Customer_Name, Cashier_Name\
    , Year, Albums) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (2 , 'Amanda', 'Sam', 2000, 'Let it Be'))


cur.execute("INSERT INTO music_store4 (transaction_id, Customer_Name, Cashier_Name\
    , Year, Albums) \
                 VALUES (%s, %s, %s, %s, %s)", \
  (3 , 'Toby', 'Sam', 2000, 'My Generation'))

cur.execute("SELECT * FROM music_store4;")

row = cur.fetchone()

while row:
   print(row)
   row = cur.fetchone()

'''
(1, 'Amanda', 'Sam', 2000, 'Rubber Soul')
(1, 'Amanda', 'Sam', 2000, 'Let it Be')
(2, 'Toby', 'Sam', 2000, 'My Generation')
'''

# 2nd Normal Form =>  While each of the records in the table is unique, our Primary key (transaction id) is not unique. => break it up into 2 tables => transactions and albums sold

# We create two new tables transactions and albums sold and insert data into these tables

cur.execute("CREATE TABLE IF NOT EXISTS transactions (transaction_id int, \
                                                           customer_name varchar, cashier_name varchar, \
                                                           year int);")

cur.execute("CREATE TABLE IF NOT EXISTS albums_sold (album_id int, transaction_id int, \
                                                          album_name varchar);")

cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_name, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (1, "Amanda", "Sam", 2000))

cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_name, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (2, "Toby", "Sam", 2000))
    
cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_name, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (3, "Max", "Bob", 2018))
    

cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (1, 1, "Rubber Soul"))
cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (2, 1, "Let it Be"))
    
cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (3, 2, "My Generation"))
    
cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (4, 3, "Meet the Beatles"))

cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (5, 3, "Help!"))

print("Table: transactions\n")
cur.execute("SELECT * FROM transactions;")

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

print("\nTable: albums_sold\n")
cur.execute("SELECT * FROM albums_sold;")
row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

'''
Table: transactions
(1, 'Amanda', 'Sam', 2000)
(2, 'Toby', 'Sam', 2000)
(3, 'Max', 'Bob', 2018)

Table: albums_sold
(1, 1, 'Rubber Soul')
(2, 1, 'Let it Be')
(3, 2, 'My Generation')
(4, 3, 'Meet the Beatles')
(5, 3, 'Help!')
'''
#### Let's do a `JOIN` on this table so we can get all the information we had in our first Table. 

# 3rd normalization: transactions table => employee name is redundant => transaction table(with employee id for name) + employee table
#Table Name: transactions2 
#column 0: transaction Id
#column 1: Customer Name
#column 2: Cashier Id
#column 3: Year

#Table Name: employees
#column 0: Employee Id
#column 1: Employee Name

#Table Name: albums_sold: keep intact
#column 0: Album Id
#column 1: Transaction Id
#column 3: Album Name

# table 1:
cur.execute("CREATE TABLE IF NOT EXISTS transactions2 (transaction_id int, customer_name varchar, cashier_id int, year int);")
cur.execute("CREATE TABLE IF NOT EXISTS employees (employee_id int, employee_name varchar);")
cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year) VALUES (%s, %s, %s, %s)", (1, "Amanda", 1, 2000))
cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year) VALUES (%s, %s, %s, %s)",(2, "Toby", 1, 2000))
cur.execute("INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year) VALUES (%s, %s, %s, %s)", (3, "Max", 2, 2018))

# table 2
cur.execute("INSERT INTO employees (employee_id, employee_name) VALUES (%s, %s)", (1, "Sam"))
cur.execute("INSERT INTO employees (employee_id, employee_name) VALUES (%s, %s)", (2, "Bob"))

'''
Table: transactions2

(1, 'Amanda', 1, 2000)
(2, 'Toby', 1, 2000)
(3, 'Max', 2, 2018)

Table: albums_sold

(1, 1, 'Rubber Soul')
(2, 1, 'Let it Be')
(3, 2, 'My Generation')
(4, 3, 'Meet the Beatles')
(5, 3, 'Help!')

Table: employees

(1, 'Sam')
(2, 'Bob')
'''

'''
# F: Denormalization: opposite of normalization
  - to improve read PERFORMANCE(quick queries) at the expense of write performances(by adding redundant data)=> 
 - comes after normalization
 - joins can be slow
 - models it differently
 - if 2 tables have same column, then updating or deleting or join or any operation on it would be time consuming.
   so with these 2 tables, just do 2 queries on each even if it has a duplucate columns!

  -Normalization is about trying to increase data INTEGRITY by REDUCING the number of COPIES of the data. Data that needs to be added or updated will be done in as few places as possible. vs   Denormalization is trying to increase performance by reducing the number of joins between tables (as joins can be slow). Data integrity will take a bit of a potential hit, as there will be more copies of the data (to reduce JOINS).
  - Denorm example: 1 , 'Amanda', 'Sam', 2000, ['Rubber Soul', 'Let it Be'] => for the seek of speed, it's ok to have a list!
'''
# Denormalization: create a table for that specific query!

# We have normalized tables from previous example:
'''
Table Name: transactions2 
column 0: transaction Id
column 1: Customer Name
column 2: Cashier Id
column 3: Year

Table Name: albums_sold
column 0: Album Id
column 1: Transaction Id
column 3: Album Name

Table Name: employees
column 0: Employee Id
column 1: Employee Name

Table Name: sales
column 0: Transaction Id
column 1: Amount Spent 
'''
# Query 1: 'select transaction_id, customer_name, amount_sent FROM <min number of tables>' => without joinsgiven these tables I wanna know amount spent on each transaction with all the transaction info. 

# solution: 
# a) joins => but we don't want to use join as it can be expensive
# b) denormalization: just add Amount Spent from sales table to transaction 2 table.  
# Table Name: transactions 
# col 0: transaction Id
# col 1: Customer Name
# col 2: Cashier Id
# col 3: Year
# col 4: amount_spent
# Create all Tables and insert the data

cur.execute("CREATE TABLE IF NOT EXISTS transactions (transaction_id int, customer_name varchar, cashier_id int, year int, amount_spent int);")
cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_id, year, amount_spent) VALUES (%s, %s, %s, %s, %s)", (1, "Amanda", 1, 2000, 40))
# without join statement
cur.execute("SELECT transaction_id, customer_name, amount_spent FROM transactions;")


# Query 2: 'select cashier_name, SUM(amount_spent) FROM <min number of tables> GROUP BY cashier_name'
# Create a new table:
# Table Name: cashier_sales
# col: Transaction Id
# Col: Cashier Name
# Col: Cashier Id
# col: Amount_Spent

cur.execute("select cashier_name, SUM(amount_spent) FROM cashier_sales GROUP BY cashier_name;")




#G. Fact vs Dimension tables=> work together for data organization
#          Fact table => facts, metrics => sales => not meant to be undated => How many?
#          Fact table can join dimension table to provide more info on customer
#          Dimension table=> categorizes facts => people, product, place, time => each dimension table will have 1 or more fact table(joined by a foreign key) => Where, what when?
# H. Schemas(for data warehouse): Star vs Snowflake =>
# Schemas = Fact + Dimension tables 
# Star => simplest data mart schema => Fact table in the center surrounded by Dimension tables => looks like a star
#       => easy to denormalize and do queries
# Snowflake => complex data mart schema => multidimensional Fact table in the center surrounded by Dimension tables => looks like a Snowflake


# H. Constraints:
# customer_id int NOT NULL Unique => cannot have null values => can be applied to more than one column.
#                                  => data across all the rows in one column are unique within the table
# The PRIMARY KEY - every table should contain a primary key. The values in this column uniquely identify the rows in the table. 
# Composite index = The PRIMARY KEY for group of columns
# Composite index example:   
#    CREATE TABLE IF NOT EXISTS customer_transactions (
#    customer_id int, 
#    store_id int, 
#    spent numeric,
#    PRIMARY KEY (customer_id, store_id)
#);
# I. Upsert
# In RDBMS language, the term upsert refers to the idea of inserting a new row in an existing table, or updating the row if it already # exists in the table

# Example:
# CREATE TABLE IF NOT EXISTS customer_address (
#    customer_id int PRIMARY KEY, 
#    customer_street varchar NOT NULL);

# INSERT into customer_address ( VALUES (432, '758 Main Street');

# then the person moved to a new address. But we don't want to update the ID. Use ON CONFLICT (customer_id) DO NOTHING; => if ID is duplicate then do nothing.

# INSERT INTO customer_address (customer_id, customer_street) VALUES( 432, '923 Knox Street')  ON CONFLICT (customer_id) DO NOTHING;

# NOw if we want to add more info on the street info. 
# INSERT INTO customer_address (customer_id, customer_street) VALUES ( 432, '923 Knox Street, Suite 1') ON CONFLICT (customer_id) 
# DO UPDATE SET customer_street  = EXCLUDED.customer_street;

