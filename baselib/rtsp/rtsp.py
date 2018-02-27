#!/usr/bin/env python
# -*- coding: utf-8 -*-   
import socket,time,string,random,threading
import logging
from baselib.logging.pylogging import setup_logging
from ReceviveAnnounce import RecAnnounce
setup_logging()
logger = logging.getLogger(__name__)

"""This Class performs rtsp protocol play.   
    Example:

         >>> myRtsp = Rtsp(host = '10.5.0.179',asset_id = 'XorMedia7#1-C201512141131xxxxx',port = 554,useragent = 'ITVLibrary 1.0; amino',application_id = 60010011)  
         >>> myRtsp.connect()  
         >>> myRtsp.setup(group_id=3,smartcard_id=201602241,device_id=201602241,home_id=10000004,purchase_id=777,require='')  
         >>> print myRtsp.setup_response
         >>> print myRtsp.setup_status
         
         >>> myRtsp.play(scale='1.000000',rangenpt='npt=0') 
         >>> print myRtsp.play_response
         >>> print myRtsp.play_status
         
         >>> time.sleep(500); 
         >>> print myRtsp.status_play[0]   
         >>> print myRtsp.play_announce
                  
         >>> myRtsp.pause() 
         >>> print myRtsp.pause_response
         >>> print myRtsp.pause_status
         >>> myRtsp.play() 
         
         >>> myRtsp.teardown() 
         >>> print myRtsp.teardown_response
         >>> print myRtsp.teardown_status
         
         >>> myRtsp.close()  
"""
def msgdecode(strContent):
    map = {}
    arrayresponse = strContent.split("\n")
    strstatus = arrayresponse[0]
    if strstatus[0:4] == 'RTSP':   
        map["Status"] = strstatus[9:12]

    for strs in arrayresponse[1:-2]:
        tmp = strs.split(": ")
        map[tmp[0]]=tmp[1][:-1]
    return map

def announce(obj,status,messageref):
    objid = obj
    statusofplay = status
    announce_play = messageref
    if statusofplay[0] == 'playing' :
        num = 0
        while True:
            msgRcv = objid.recv(1024*10)
            logger.debug("the daemon respose message is :\n%s." % msgRcv) 
            announceresponse = msgRcv.split("\n")
            announcefirststr = announceresponse[0]
            if announcefirststr[0:8] == 'ANNOUNCE': 
                announce_play.insert(num, msgdecode(msgRcv))
                logger.debug("the paly announce message is :\n%s." % msgRcv)
                num = num + 1
                notice = msgdecode(msgRcv)["TianShan-NoticeParam"];
                logger.debug("the TianShan-NoticeParam value is %s." % notice)
                if 'presentation_state=stop' in notice:
                    statusofplay[0] = "stopped"
                    logger.debug("The media play is over.")
                    break;
                if 'presentation_state=play' in notice:
                    statusofplay[0] = "playing"
                    logger.debug("The media is playing.")
                if statusofplay[0] == 'stopped' : 
                    break;   

class Rtsp(object):
    host = None
    port = None
    url = None
    session_id = None
    group_id = None
    smartcard_id = None
    device_id = None
    home_id = None
    purchase_id = None
    obj_soket = None
    useragent = None
    application_id = None
    asset_id = None
    require =None
    setup_response = None
    setup_status = None
    play_response = None
    play_announce = []
    play_status = None
    pause_response = None
    pause_status = None
    teardown_response = None
    teardown_status = None
    seq = 1
    buflen = 1024*10
    status_play = ["stopped"]
    
    
    def __init__(self, host, asset_id ,port = 554 ,useragent ="ITVLibrary 1.0; amino", application_id = 60010011):
        self.host = host
        self.asset_id = asset_id
        self.port = port
        self.useragent = useragent
        self.application_id = application_id
    def genmsg_setup(self,url,seq,userAgent,groupId,smartcardId,deviceId,homeId,purchaseId,require=''):
        msgRet = "SETUP " + url + " RTSP/1.0\r\n"
        msgRet += "CSeq: " + str(seq) + "\r\n"
        if require == '':
            logger.debug("the input require is null.")
        else:
            msgRet += "Require: " + require + "\r\n"
        msgRet += "User-Agent: " + userAgent + "\r\n"
        msgRet += "Transport: MP2T/DVBC/QAM;unicast" + "\r\n"
        msgRet += "TianShan-Version: 1.0" + "\r\n"
        msgRet += "TianShan-ServiceGroup: " + str(groupId) + "\r\n"
        msgRet += "TianShan-AppData:smartcard-id=" + str(smartcardId) + ";device-id=" + str(deviceId) + ";home-id=" + str(homeId) + ";purchase-id=" + str(purchaseId) + "\r\n"
        msgRet += "\r\n"
        return msgRet
    
    def genmsg_play(self,seq,userAgent,sessionId,scale='1.000000',rangeNpt=''):
        msgRet = "PLAY * RTSP/1.0\r\n"
        msgRet += "CSeq: " + str(seq) + "\r\n"
        msgRet += "Session:  " + sessionId + "\r\n"
        msgRet += "User-Agent: " + userAgent + "\r\n"
        if rangeNpt == '':
            msgRet += "Range: \r\n"
        else:
            msgRet += "Range: " + "npt=" + rangeNpt + "\r\n"     
        msgRet += "Scale: " + scale + "\r\n"
        msgRet += "\r\n"
        return msgRet
    
    def genmsg_pause(self,seq,userAgent,sessionId):
        msgRet = "PLAUSE * RTSP/1.0\r\n"
        msgRet += "Session:  " + sessionId + "\r\n"
        msgRet += "CSeq: " + str(seq) + "\r\n"
        msgRet += "User-Agent: " + userAgent + "\r\n"
        msgRet += "\r\n"
        return msgRet
    
    
    def genmsg_teardown(self,sessionId,seq,userAgent,xReason):
        msgRet = "TEARDOWN * RTSP/1.0\r\n"
        msgRet += "Session:  " + sessionId + "\r\n"
        msgRet += "CSeq: " + str(seq) + "\r\n"
        msgRet += "User-Agent: " + userAgent + "\r\n"
        msgRet += "x-reason: " + xReason + "\r\n"
        msgRet += "\r\n"
        return msgRet
       
#     def decodemsg(self,strContent):
#         mapRetInf = {}
#         reponsearray = strContent.split("\n")
#         statusstr = reponsearray[0]
#         if statusstr[0:4] == 'RTSP':   
#             mapRetInf["Status"] = statusstr[9:12]
# 
#         for strs in reponsearray[1:-2]:
#             tmp = strs.split(": ")
#             mapRetInf[tmp[0]]=tmp[1][:-1]
#         return mapRetInf
    
    
#     def receive_announce(self):
#         if self.status_play == 'playing' :
#             num = 0
#             while True:
#                 msgRcv = self.obj_soket.recv(self.buflen)
#                 announceresponse = msgRcv.split("\n")
#                 announcefirststr = announceresponse[0]
#                 if announcefirststr[0:8] == 'ANNOUNCE': 
#                     self.play_announce.insert(num, self.decodemsg(msgRcv))
#                     logger.debug("the paly announce message is :\n%s." % msgRcv)
#                     num = num + 1
#                     notice = self.decodemsg(msgRcv)["TianShan-NoticeParam"];
#                     logger.debug("the TianShan-NoticeParam value is %s." % notice)
#                     if 'presentation_state=stop' in notice:
#                         self.status_play = "stopped"
#                         logger.debug("The media play is over.")
#                         break;
#                     if 'presentation_state=play' in notice:
#                         self.status_play = "playing"
#                         logger.debug("The media is playing.")
#                 if self.status_play == 'stopped' : 
#                     break;
    
    def connect(self):
        self.obj_soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
        self.obj_soket.connect((self.host, self.port));
        
    def setup(self,group_id,smartcard_id,device_id,home_id,purchase_id,require=''):
        self.seq = self.seq + 1
        self.url = "rtsp://" + self.host + ":" + str(self.port) + "/" + str(self.application_id) + "?asset=" + str(self.asset_id)
        logger.debug("the url is %s" % self.url)
        self.group_id = group_id
        self.smartcard_id = smartcard_id
        self.device_id = device_id
        self.home_id = home_id
        self.purchase_id = purchase_id
        self.require = require
        setupmsg = self.genmsg_setup(self.url,self.seq,self.useragent,self.group_id,self.smartcard_id,self.device_id,self.home_id,self.purchase_id,self.require)
        logger.debug("the setup message is :\n%s" % setupmsg)
        self.obj_soket.send(setupmsg)
        msg1 = self.obj_soket.recv(self.buflen); 
        logger.debug("the setup response message is :\n%s" % msg1)
        self.setup_response = msg1
        #status = self.decodemsg(msg1)["Status"];
        status = msgdecode(msg1)["Status"];
        logger.debug("The setup status is %s." % status)
        self.setup_status = status
        if status == '200' :        
            #self.session_id = self.decodemsg(msg1)["Session"];
            self.session_id = msgdecode(msg1)["Session"];
            logger.debug("The setup session id is %s." % self.session_id)
        else:
            logger.error("setup fail.")
    def play(self,scale,rangenpt):
        if self.session_id == None:
            logger.error("can not get sessionid,play fail.")
        else:
            self.seq = self.seq + 1
            playmsg = self.genmsg_play(self.seq,self.useragent,self.session_id,scale,rangenpt)
            logger.debug("the play message is :\n%s" % playmsg)
            self.obj_soket.send(playmsg)
            msg2 = self.obj_soket.recv(self.buflen)
            self.play_response = msg2
            logger.debug("the play respose message is :\n%s." % msg2) 
            #playstatus = self.decodemsg(msg2)["Status"];
            playstatus = msgdecode(msg2)["Status"];
            logger.debug("The play status is %s." % playstatus)
            self.play_status = playstatus
                      
            if playstatus == '200' :
                self.status_play[0] = "playing"
                #t= threading.Thread(target =self.receive_announce,args=())
                t= threading.Thread(target = RecAnnounce(announce,(self.obj_soket,self.status_play,self.play_announce),announce.__name__))
                t.setName('Collectannounce')
                t.setDaemon(True)
                t.start()
                logger.debug("quit the play command." )
#                 num = 0
#                 while True:
#                     msgRcv = self.obj_soket.recv(self.buflen)
#                     self.play_announce.insert(num, self.decodemsg(msgRcv))
#                     logger.debug("the paly announce message is %s." % msgRcv)
#                     num = num + 1
#                     notice = self.decodemsg(msgRcv)["TianShan-NoticeParam"];
#                     logger.debug("the TianShan-NoticeParam value is %s." % notice)
#                     if 'presentation_state=stop' in notice:
#                         self.status_play = "stopped"
#                         logger.debug("The media play is over.")
#                         break;
#                     if 'presentation_state=play' in notice:
#                         self.status_play = "playing"
#                         logger.debug("The media is playing.")
            else:
                logger.error("play fail.")    
    def pause(self):
        if self.session_id == None:
            logger.error("can not get sessionid,pause fail.")
        else:
            self.seq = self.seq + 1
            if self.status_play[0] == "playing":
                pausemsg = self.genmsg_pause(self.seq,self.useragent,self.session_id)
                self.obj_soket.send(pausemsg);
                while True:
                    msg3 = self.obj_soket.recv(self.buflen);
                    pauseresponse = msg3.split("\n")
                    pausefirststr = pauseresponse[0]
                    if pausefirststr[0:4] == 'RTSP':               
                        logger.debug("The pause response is %s." % msg3) 
                        self.pause_response = msg3
                        #pausestatus = self.decodemsg(msg3)["Status"];
                        pausestatus = msgdecode(msg3)["Status"];
                        logger.debug("The pause status is %s." % pausestatus)
                        self.pause_status = pausestatus  
                        break                      
            else:
                logger.debug("the play is end,need not to pause.")    
              
    def teardown(self,reason):
        if self.session_id == None:
            logger.error("can not get sessionid,play fail.")
        else:
            self.seq = self.seq + 1
            if self.status_play[0] == "playing":
                teardownmsg = self.genmsg_teardown(self.session_id,self.seq,self.useragent,reason)
                self.obj_soket.send(teardownmsg)
                while True:
                    msg4 = self.obj_soket.recv(self.buflen)
                    teardownresponse = msg4.split("\n")
                    teardownfirststr = teardownresponse[0]
                    if teardownfirststr[0:4] == 'RTSP':
                        logger.debug("the teardown response is %s" % msg4)                
                        self.teardown_response = msg4
                        #teardownstatus = self.decodemsg(msg4)["Status"]
                        teardownstatus = msgdecode(msg4)["Status"]
                        logger.debug("The teardown status is %s." % teardownstatus)
                        self.teardown_status = teardownstatus
                        if teardownstatus == '200':
                            self.status_play[0] == "stopped"                                
            else:
                logger.debug("the play is end,need not to teardown.")    
       
    def close(self):
        self.obj_soket.close();
         
   