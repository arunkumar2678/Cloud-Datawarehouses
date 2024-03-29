import configparser
import pandas
import psycopg2
from sql_queries import create_table_queries, drop_table_queries, copy_table_queries, insert_table_queries


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        print("table created")
        conn.commit()


def copy_tables(cur,conn):
    for query in copy_table_queries:
        cur.execute(query)
        print("table copied")
        conn.commit()

        
def insert_tables(cur,conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

    
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)
    copy_tables(cur,conn)
    insert_tables(cur,conn)

  
    conn.close()


if __name__ == "__main__":
    main()