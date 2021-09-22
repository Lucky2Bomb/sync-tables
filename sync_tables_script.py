#!/usr/bin/python
from SyncTables import get_sync_tables
from connect import connect
from TestCommands import *
from GettingDataTable import *

debug = True

main_table = 'articles'
dublicate_table = 'articles_dublicate'


def run_all_commands(cursor):

    headers_table_list = get_headers(main_table, cursor).copy()
    
    start_commands(get_sync_tables(
        main_table_name=main_table,
        dublicate_table_name=dublicate_table, headers_list=headers_table_list
    ), cursor=cursor, debug=debug)


if __name__ == '__main__':
    connect(run_all_commands, debug)
