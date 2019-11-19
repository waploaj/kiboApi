from kibo.Config.database import mysql
import pymysql
import   smtplib
from email.message import EmailMessage
import os

msg = EmailMessage()
msg["from"] = "abdallah@mu-agency.com"
msg["to"] = "mewaploaj@hotmail.com"
msg["subject"] = f"Un error occured on {os.getcwd()}"


def kasaa():

        try:
            employee_id =1
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            return cursor
        except Exception as e:
            # with smtplib.SMTP_SSL("mu-agency.com",465) as server:
            #     server.login("abdallah@mu-agency.com","1234Xta12345.")
            #     msg.set_content(e)
            #     server.send_message(msg)
            print("An email has been sent to waploaj")


