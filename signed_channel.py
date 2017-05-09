#!/usr/bin/python
# -*- coding: UTF-8 -*-
import zipfile
import shutil
import os
import time
###############################
# Describe : 签名、渠道号
# D&P Author By:   LvStudio
# Create Date:     2016-08-31
# Modify Date:     2016-08-31
###############################

src_apk_name="ChronicManagement.apk" #未签名的apk
channel_file='channel.txt' #渠道号配置文件
version='v1006'#版本信息
prefix='twhb'
suffix='.apk'
current_time=time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

signed_apk_name='signed_'+src_apk_name;

def signedApk():
	print ('signeding..................')
	command='jarsigner -verbose -keystore cmri.key -storepass cmcc1234 -keypass cmri1234 -signedjar '+signed_apk_name+' '+src_apk_name+' cmri  -digestalg SHA1 -sigalg MD5withRSA'
	os.system(command)
	print ('singed complete!')

def MarkChannelApk(target_apk_name,channel_name):
	zipped = zipfile.ZipFile(target_apk_name, 'a', zipfile.ZIP_DEFLATED)
	empty_channel_file = "META-INF/mtchannel_{channel}".format(channel=channel_name)
	zipped.write(empty_file, empty_channel_file)
	zipped.close()

signedApk()

empty_file='empty.txt'
open(empty_file,'w').close()


f=open(channel_file)
lines=f.readlines()
f.close()
os.mkdir(version);
for x in lines:
	x=x.strip('\n')
	# target_apk_name=x+'/'+prefix+'_'+version+'_'+current_time+'_'+suffix
	target_apk_name=version+'/'+prefix+'_'+x+'_'+version+suffix
	print (signed_apk_name+'===='+target_apk_name)
	shutil.copy(signed_apk_name,target_apk_name)
	MarkChannelApk(target_apk_name,x)