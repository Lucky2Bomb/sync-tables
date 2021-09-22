# About project

This project need for copy data from *main table* to *dublicate table*. All data in two tables don't deleted, but, if in *main table* column deleted_at != [null] then row don't copied and updated in dublicate table

# Commands (start from root directory)
 
+ **.\batch\run_main** - create two database and push first test data in database
+ **.\batch\push_test_data** - push test data (random data (randrange + lorem)) in main table
+ **.\batch\push_test_data_dublicate_table** - push test data in dublicate of main table
+ **.\batch\sync** - start insert and update rows from *main_table* to *dublicate_main_table*
+ **.\batch\run_test** - start unittests