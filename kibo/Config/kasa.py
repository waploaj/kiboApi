from kibo.Config.database import mysql
import pymysql
import logging


class Connection:
    conn = None

    def openconnection(self):
        try:
            if self.conn == None:
                self.conn = mysql.connect()
        except pymysql.MySQLError as e:
            print(e)
        finally:
            logging.info("connection was opened")

    def run_query(self,query):
        try:
            self.openconnection()
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                if 'SELECT'.lower() in query.lower():
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
                else:
                    cursor.execute(query)
                    self.conn.commit()
                    affectedrow = cursor.rowcount
                    return f"{affectedrow} number of column affected"
        except pymysql.MySQLError as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                logging.info("connection is closed")




