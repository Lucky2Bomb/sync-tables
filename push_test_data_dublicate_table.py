#!/usr/bin/python
from SyncTables import get_sync_tables
from connect import connect
from TestCommands import *
from GettingDataTable import *

debug = True

main_table = 'articles'
dublicate_table = 'articles_dublicate'


def run_all_commands(cursor):

    start_commands(get_push_test_random_data(
        dublicate_table), cursor=cursor, debug=debug)


if __name__ == '__main__':
    connect(run_all_commands, debug)
