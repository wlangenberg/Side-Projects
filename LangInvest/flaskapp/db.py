from datetime import datetime
import os
import psycopg2
import psycopg2.extras

class cursor:
    def __init__(self, database, sql, sqldata, schema='maindb'):
        self.schema = schema
        self.sql = sql
        self.sqldata = sqldata
        self.cursor = None
        self.database = database
        # self.lastid = 0

    # Add True as argument to have the computed sql query printed 
    def connect(self, debug=False):
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                port=5432,
                database=self.database,
                user=os.environ['DB_USERNAME'],
                password=os.environ['DB_PASSWORD'],
                cursor_factory=psycopg2.extras.RealDictCursor)

            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            self.cursor.execute(self.sql, self.sqldata)
            self.connection.commit()
            self.result = self.cursor.fetchall()
            self.cursor.close()
            self.connection.close()
            
        except psycopg2.Error as e:
            self.result = "%s" % (e)
            if self.result != "no results to fetch":
                print(self.result)

        return(self.result)

