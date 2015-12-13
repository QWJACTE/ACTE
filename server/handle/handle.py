'''
This file used for handle msg from Client
and resend msg to the Client for require
'''

'''
Here saved the mysql user and password
'''
HOST = 'localhost'
USER = 'root'
PASSWORD = '19660120Zlp'# my mother's birthday!
DATABASE = 'ACTE'

from flask import Flask, request, jsonify, render_template
import MySQLdb

def handle(msg):
    return 'good', 'get it'

def signup(uid, password):
    '''
    This method used for user to signup
    uid and password is necessary.
    '''
    return jsonify(success=False,msg='注册成功')
    # Open database connection
    # db = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)
    # # prepare a cursor object using cursor() method
    # cursor = db.cursor()
    # if findUserByUid(cursor, uid):
    #     success = False
    #     data = '用户已经存在'
    # else:
    #     success = True
    #     insertUser(cursor, uid, password)
    #     Userid = cursor.fetchone()[0]
    #     data = jsonify(msg='注册成功',username=uid,Userid=id)
    # # disconnect from server
    # db.close()
    # return jsonify(success=success,msg=data)

def findUserByUid(cursor, uid):
    '''
    This method use uid to find if the user exist.
    If so, return True, else return False.
    '''
    if cursor.execute('select * from User where UID = \''+uid+'\'') == 1:
        return True
    else return False

def insertUser(cursor, uid, password):
    '''
    insert a new user
    '''
    cursor.execute('insert into User(UID, password) value(\''+uid+'\',\''+password+'\')')