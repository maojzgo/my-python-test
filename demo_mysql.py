import mysql.connector
import logging

def query():
    config={'host':'10.53.145.203',
            'user':'dc_etl',
            'password':'123456',
            'database':'dc_ods'}
    try:
        conn = mysql.connector.connect(**config)

        sql_query = 'select \'abc\',current_date ;'
        cursor = conn.cursor()
        cursor.execute(sql_query)

        for s, d in cursor:
            print(s, d)
    except mysql.connector.Error as e:
        logging.error(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    query()