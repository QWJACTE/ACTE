# -*- encoding=utf-8 -*-
#!/usr/bin/python

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
        try:
            cursor.execute('insert into City(CID,name) values(\''+a[0]+'\',\''+a[1]+'\')')
            db.commit()
        except:
            db.rollback()
        wordlist.append(a)

db.close()
