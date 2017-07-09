#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

class glog(object):
    """
    Usage:
    This program will creat proj_name.log file and write it.
    First let 'log = glog.glog("proj_name")'
    Then use 'log.log("Some msg",[int error_code])'
    Enjoy
    """
    def __init__(self, proj_name):
        super (glog, self).__init__()
        self.proj_name = "%s.log"%proj_name
        self.started = False
        self.last_error = ''
        self.start()

    def start(self):
        if not os.path.exists(self.proj_name):
            os.system("touch %s"%self.proj_name)
        self.started = True
        self.log(u'<<<<<<<<<<   Start log   >>>>>>>>>>')
    
    def log(self,msg,code=0):
        if not self.started:
            self.start()
        if not (type(code) == type(0)):
            self.last_error = '"code" type is not int, exit.'
            return False
        if (type(msg) == type(u'')):
            msg = msg.encode('utf-8')
        if not (type(msg) == type(u''.encode('utf-8'))):
            self.last_error = '"msg" type is not unicode nor str, exit.'
            return False

        with open(self.proj_name,"a") as log_file:
            time_now = time.time()
            log_file.write("[%f] %d $> %s\r\n"%(time_now,code,msg))
        return True






