#!/usr/bin/python
# -*- encoding=utf-8 -*-

import os
from flask import send_from_directory,Flask, request, jsonify, render_template
import socket
from handle import *
app = Flask(__name__)

# HOST = '121.42.145.248'
# PORT = 8080

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/readme')
def readme():
    return render_template('readme.txt',abc='helloworld')

@app.route('/signup', methods=['POST'])
def signup():
    uid = request.form['uid']
    password = request.form['password']
    nickname = request.form['nickname']
    sex = request.form['sex']
    birthday = request.form['birthday']
    email = request.form['email']
    location = request.form['location']
    return handle.signup(uid, password, nickname, sex, birthday, email, location)

@app.route('/login', methods=['POST'])
def login():
    uid = request.form['uid']
    password = request.form['password']
    if uid == '':
        return jsonify(success=False, msg=u'请输入用户名')
    elif password == '':
        return jsonify(success=False, msg=u'请输入密码')
    else:
        return handle.login(uid, password)

@app.route('/updatebasic/', methods=['GET'])
@app.route('/updatebasic/<uid>', methods=['GET'])
def updatebasic(uid=''):
    return handle.updatebasic(uid)

@app.route('/updaterecommendation/', methods=['GET'])
@app.route('/updaterecommendation/<uid>', methods=['GET'])
def updaterecommendation(uid=''):
    return handle.updaterecommendation(uid)

@app.route('/updaterecommendationimage/', methods=['GET'])
@app.route('/updaterecommendationimage/<actid>', methods=['GET'])
def updaterecommendationimage(actid=''):
    if actid == '':
        return jsonify(success=False, msg=u'没有活动id')
    else:
        return handle.updaterecommendationimage(actid)

@app.route('/image')
def image():
    return send_from_directory(os.path.join(app.root_path,'templates/img'),'1.jpg')

@app.route('/loadimage/<imginfo>', methods=['GET'])
def loadimage(imginfo='unknown_0101001'):
    uid, img = ('%s' % imginfo).split('_')
    tab = int(str(img)[0:2])
    section = int(str(img)[2:4])
    position = int(str(img)[4:7])
    imgurl = handle.sendimage(str(uid),tab,section,position)
    return send_from_directory(os.path.join(app.root_path,'templates/img'),imgurl)

@app.route('/loadtext/<textinfo>', methods=['GET'])
def loadtext(textinfo='unknown_0101001'):
    uid, text = ('%s' % textinfo).split('_')
    tab = int(str(text)[0:2])
    section = int(str(text)[2:4])
    position = int(str(text)[4:7])
    success, text = handle.sendtitle(str(uid),tab,section,position)
    return jsonify(success=success, msg=text)

@app.errorhandler(404)
def page_not_found(error):
    return u'你走错门了'


if __name__ == '__main__':
    app.run()


# def main():
#     ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     ss.bind((HOST, PORT))
#     ss.listen(5)

#     while True:
#         print 'begin accept'
#         conn, addr = ss.accept()
#         # record Client address
#         log.get_log('Client addr', str(addr))

#         try:
#             conn.settimeout(50)
#             buf = conn.recv(2048)
#             back_msg = handle.handle(buf)
#             if back_msg[0] == const.ILLEGAL_REQUEST:
#                 raise ILLEGAL_REQUEST_EXCEPTION
#             else:
#                 conn.sendall(back_msg[1])
#         except socket.timeout:
#             print 'time out'
#         except ILLEGAL_REQUEST_EXCEPTION:
#             conn.sendall(const.ILLEGAL_REQUEST)
#         conn.close()

#     ss.close()
