# -*- endcoding=utf-8 -*-
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
null = 'NULL'

from flask import Flask, request, jsonify, render_template
import MySQLdb

def getDC():
    db = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)
    cursor = db.cursor()
    return db, cursor

def handle(msg):
    return 'good'

def signup(uid, password, nickname=null,sex='secret',birthday=null,email=null,location=null):
    '''
    This method used for user to signup
    uid and password is necessary.
    '''
    db, cursor = getDC()
    if findUserByUid(cursor, uid):
        success = False
        data = '用户已经存在'
    else:
        success = True
        if insertUser(db, cursor, uid, password,nickname,sex,birthday,email,location) == 0:
            data = '注册成功'
        else:
            success = False
            data = '注册失败'
    # disconnect from server
    db.close()
    return jsonify(success=success,msg=data)

def findUserByUid(cursor, uid):
    '''
    This method use uid to find if the user exist.
    If so, return True, else return False.
    '''
    if cursor.execute('select * from User where UID = \''+uid+'\'') == 1:
        return True
    else:
        return False

def insertUser(db,cursor,uid,password,nickname,sex,birthday,email,location):
    '''
    insert a new user
    '''
    try:
        cursor.execute('insert into User(UID,password,nickname,sex,birthday,email,location) value(\''+str(uid)+'\',\''+str(password)+'\',\''+str(nickname)+'\',\''+str(sex)+'\',\''+str(birthday)+'\',\''+str(email)+'\',\''+str(location)+'\')')
        db.commit()
        return 0
    except:
        db.rollback()
        return -1

def login(uid, password):
    db, cursor = getDC()
    if findUserByUid(cursor, uid):
        if cursor.fetchone()[2] == password:
            success = True
            data = '登入成功'
        else:
            success = False
            data = '账号或密码错误'
    else:
        success = False
        data = '账号或密码错误'
    db.close()
    return jsonify(success=success,msg=data)

def updatebasic(uid):
    db, cursor = getDC()
    if findUserByUid(cursor, uid):
        db.close()
        return 'nothing'
    else:
        db.close()
        return 'nothing'

def findAllAct(cursor):
    cursor.execute('select * from Activity')
    return [i[0] for i in cursor.fetchall()]

def updaterecommendation(uid):
    db, cursor = getDC()
    return jsonify(success=True, actid=findAllAct(cursor)[0])

def findActByid(cursor,actid):
    return True if 1 == cursor.execute('select * from Activity where id ='+str(actid)) else False

def sendimage(uid,imgtab,imgsection,imgposition):
    db, cursor = getDC()
    actid = imgposition+1
    if findActByid(cursor,actid):
        a = cursor.fetchone()
        url=a[4]
    else:
        url='1'
    return url + '.jpg'

def sendtitle(uid,tab,section,position):
    db, cursor = getDC()
    actid = position+1
    if findActByid(cursor, actid):
        a = cursor.fetchone()
        text=a[2]
        success=True
        return success, text
    else:
        return False, 'none'

def updaterecommendationimage(actid):
    db, cursor = getDC()
    if findActByid(cursor,actid):
        success = True
        oneAct = cursor.fetchone()[4]
    else:
        success = False
        oneAct = 'nothing'
    db.close()
    return jsonify(success=success, actImg=oneAct)
