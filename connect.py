#!/usr/bin/python
import psycopg2
from config import config
from TestCommands import *
import asyncio


def connect(func, debug=False):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        if(debug):
            print('connect to database')
        cur = conn.cursor()

        func(cur)

        cur.close()
        if(debug):
            print('database connection closed')
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        if(debug):
            print(error)
    finally:
        if conn is not None:
            conn.close()
            if(debug):
                print('database connection closed')


if __name__ == '__main__':
    connect()
