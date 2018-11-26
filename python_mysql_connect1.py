#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import Error

def connect():
    try:
        conn = mysql.connector.connect(host='localhost',
													   database='name_db',
													   user='username',
													   password='pass_db')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()

if __name__ == '__main__':
    connect()
