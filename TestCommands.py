
from WorkWithStringList import get_list_as_string, get_new_list_without_item
import lorem
from random import randrange

def get_create_tables(main_table_name = 'main_table', dublicate_table_name = 'dublicate_main_table'):
    f""" create tables in the PostgreSQL database"""
    return (
        f"""
            DROP TABLE IF EXISTS {main_table_name} CASCADE;
            """,
        f"""
            DROP TABLE IF EXISTS {dublicate_table_name} CASCADE;
            """,
        f"""
            CREATE TABLE IF NOT EXISTS {main_table_name} (
                id          SERIAL PRIMARY KEY,
                title       VARCHAR(150) NOT NULL,
                description TEXT NOT NULL,
                updated_at  TIMESTAMP,
                created_at  TIMESTAMP,
                deleted_at  TIMESTAMP
            );
            """,
        f"""
            CREATE TABLE IF NOT EXISTS {dublicate_table_name} (
                id          SERIAL PRIMARY KEY,
                title       VARCHAR(150) NOT NULL,
                description TEXT NOT NULL,
                updated_at  TIMESTAMP,
                created_at  TIMESTAMP,
                deleted_at  TIMESTAMP,
                {main_table_name}_id  INTEGER
            );
            """
    )


def get_push_test_data(main_table_name = 'main_table', dublicate_table_name = 'dublicate_main_table'):
    return(
        f"""
        INSERT INTO {main_table_name}(title, description, updated_at, created_at, deleted_at) 
            VALUES(
                'title1', 
                'description1', 
                '2021-09-20 10:56:28.338706', 
                '2021-09-20 10:56:28.338706', 
                null)
        """,
        f"""
        INSERT INTO {main_table_name}(title, description, updated_at, created_at, deleted_at) 
            VALUES(
                'title2', 
                'DESCRIPTION FROM ORIGINAL TABLE', 
                '2021-09-20 10:56:11.000002', 
                '2021-09-20 10:16:28.000002', 
                null)
        """,
        f"""
        INSERT INTO {main_table_name}(title, description, updated_at, created_at, deleted_at) 
            VALUES(
                'title3', 
                'description3', 
                '2021-07-20 08:00:21.337406', 
                '2021-08-20 09:50:22.373701', 
                '2021-09-20 10:56:00.003704'
                )
        """,
        f"""
        INSERT INTO {main_table_name}(title, description, updated_at, created_at, deleted_at) 
            VALUES(
                'title4', 
                'description4', 
                '2021-09-20 01:06:55.338222', 
                '2021-09-20 01:06:55.338222', 
                null)
        """,
        f"""
        INSERT INTO {dublicate_table_name}(title, description, updated_at, created_at, deleted_at, {main_table_name}_id) 
            VALUES(
                'title2', 
                'DESCRIPTION {main_table_name} DUBLICATE', 
                '2021-09-20 10:56:11.000001', 
                '2021-09-20 10:16:28.000001', 
                null,
				2
			);
        """,
    )

def get_push_test_random_data(table_name):
    random_time_create = f'{str(randrange(24))}:{str(randrange(60))}:{str(randrange(60))}'
    random_time_update = f'{str(randrange(24))}:{str(randrange(60))}:{str(randrange(60))}'
    return(
        f"""
        INSERT INTO {table_name}(title, description, updated_at, created_at, deleted_at) 
            VALUES(
                '{lorem.sentence()}', 
                '{lorem.sentence()}', 
                '2021-09-20 {random_time_create}.{str(randrange(1000000))}', 
                '2021-09-20 {random_time_update}.{str(randrange(1000000))}', 
                null)
        """,
    )

def start_commands(commands, cursor, debug = False):
    try:
        for command in commands:
            cursor.execute(command)
            if(debug):
                print('-----------------------------------------------')
                print('===================COMMAND=====================')
                print(command)
                print('==|=========================================|==')
                print('--|-----------------------------------------|--')

    except Exception as error:
        print(error)
