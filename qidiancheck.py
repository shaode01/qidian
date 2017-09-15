# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 08:46:12 2017

@author: 
"""


import itchat

flag=True
maxtry=3
while(maxtry>0): 
    itchat.auto_login(hotReload=True)
    mps = itchat.get_mps()
    qidian = itchat.search_mps(name=u'起点读书')
    resp=itchat.send(u"签到",toUserName = qidian[0]['UserName'])  
    if(resp['BaseResponse']['Ret']==0):
        maxtry=0
        flag=False
    else:
        maxtry=maxtry-1
        print resp['BaseResponse']['ErrMsg']
if(flag):
    users = itchat.search_friends(name=u'一步')
    itchat.send(u"起点签到失误，请手动签到",toUserName = users[0]['UserName'])
  
