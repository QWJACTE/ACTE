# -*- encoding=utf-8 -*-
import time

def get_log(tag, msg):
    '''
    put log message to its special log files
    '''
    try:
        open('log/'+tag+'.log', 'w+').write(time.strftime('%Y-%m-%d %H:%M:%S ')+msg)
        return 0
    # if read file failed
    except Exception, e:
        return -1