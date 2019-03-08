#功能：实现文件快速拷贝
#作者：subaoyuanbo@163.com	
#日期：2017-11-13
#coding:utf-8
import shutil
import re
import configparser
import time
import datetime
import os
#单文件正则表达式拷贝
#def filecopy(file_choose):
#	with open('dir.ini', 'r') as f:
#		str = f.read()
#	filename = "".join(re.findall(r"file = (.+?)\n",str))
#	dir = "".join(re.findall(r"outdir = (.+?)\n",str))
#	#print(dir)
#	#print(filename)
#	shutil.copyfile(filename,dir)

def filecopy_new(file_choose):
	error = 1
	config = configparser.ConfigParser()
	try:
		config.readfp(open('dir.ini'))    #打开配置文件
	except FileNotFoundError:
		print("\n未找到配置文件\n")
		return error
	str = '序号' + file_choose #字符串拼接
	try:
		source = config.get(str,"源文件路径")  #将序号x下的“源文件路径”赋值给source
		target = config.get(str,"目标路径")
		#old_filedate = os.path.getctime(source)
	except configparser.NoSectionError:
		print("\n序号错误\n")
		return error
	#while(1):
	try:
			#new_filedate = os.path.getctime(source)
			#if old_filedate != new_filedate:
		shutil.copyfile(source,target)	#复制文件
	except IOError:
		print("\n文件路径错误\n")
		return error
	#print("%s\n"%(str))
	print("\n源文件路径:%s\n"%(source))
	print("目标路径:%s\n"%(target))
	return 0

while(1):
	#print("*请输入要拷贝的文件序号:\n")
	file_choose = input("****请输入要拷贝的文件序号:")
	ret = filecopy_new(file_choose)
	if ret == 0:
		print('拷贝成功\n')
	else:
		print('拷贝失败\n')
