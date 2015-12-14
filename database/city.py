# -*- encoding=utf-8 -*-

import MySQLdb

HOST = 'localhost'
USER = 'root'
PASSWORD = '19660120Zlp'# my mother's birthday!
DATABASE = 'ACTE'

db = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)
cursor = db.cursor()

wordlist = []
with open('city.txt', 'r') as fr:
    for word in fr.readlines():
        a = word.strip().split(' ')
        cursor.execute('insert into City(CID,name)value('+word[0]+',\''+word[1]+'\'')')
        wordlist.append(a)

db.close()