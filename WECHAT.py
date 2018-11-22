from urllib import request
from bs4 import BeautifulSoup
import re
import chardet
import sys
import json
import demjson
import os
import time

def get_content(url,timeStamp):
	resp = request.urlopen(url)
	html = resp.read()
	bs = BeautifulSoup(html, "html.parser")
	content =  bs.get_text()
	#print(content)
	lindex = content.find("微信号")
	rindex = content.find("var first_sceen__time = (+new Date());")


	titlelindex = content.find("window.logs.pagetime['html_begin'] = (+new Date());")
	length = len("window.logs.pagetime['html_begin'] = (+new Date());")
	titlerindex = content.find(".radius_avatar")
	#print(content[titlelindex+length+12:titlerindex-2])
	#print(content[lindex+89:rindex-23])
	con_string=content[lindex+88:rindex-23]
	tit_string=content[titlelindex+length+12:titlerindex-2]
	#con_string = content[lindex+89:rindex-23]
	
	#时间处理
	timeArray = time.localtime(timeStamp)
	otherStyleTime = time.strftime("%Y.%m.%d", timeArray)
	#print(otherStyleTime)
	
	#内容处理
	newstr=''
	for str in con_string:	
		if str.isspace():
			if str.isspace(): 
				#print(str)
				str = '\n\t'
		newstr = newstr + str
	#print(newstr)
	
	#标题处理
	titlestr=''
	for str2 in tit_string:
		if str2=='|':
			str2='-'
		titlestr = titlestr+str2
	#print(titlestr)
	
	#文件流处理
	os.getcwd()
	os.chdir(r'C:\Users\zhututu\Desktop\py test\rmsp')
	f = open(otherStyleTime+'  '+titlestr+".doc",'w',encoding="utf-8")
	f.write('\t\t\t\t'+titlestr+'\n\n\t'+newstr)
	f.flush()
	f.close()
	#os.close()
	

#控制台输入方式爬去
#url_input=" "
#while url_input!='end':
#	url_input =input("\n请输入你的url:\n")
#	if url_input == '-1':
#		break
#	get_content(url_input,1507644415)

#json方式爬取
#f=open('rmsp.txt', 'r',encoding="ISO-8859-1")
#jsonstr = f.read()
#datas = json.loads(jsonstr)
#print(type(datas[0]['app_msg_list'][0]['link']))
#for data in datas:
#	for dat in data['app_msg_list']:
#		get_content(dat['link'],dat['update_time'])

#get_content("https://mp.weixin.qq.com/s/wWMdLJRpfUyKBLmKfy_btQ",1507644415)








