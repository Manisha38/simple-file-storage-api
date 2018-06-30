"""
This file contains all generic functions. 
Each function calls respective storage mechanism
"""

from s3fileManage import *
from diskFileManage import *


flag = None

#variable set to type of storage : 
# aws s3 flag= 1
# filesystem flag =2
def setFlag(type):
	global flag	
	if type=="aws" or type=="s3":
		flag=1
	elif type =="filesystem":
		flag=2


def fCreate(name):
	if flag==1:
		return aws_fCreate(name)
	elif flag==2:
		return f_fCreate(name)


def fOpen(name):
	if flag==1:
		return aws_fOpen(name)
	elif flag==2:
		return f_fOpen(name)


def fRename(old_name,new_name):
	#print(old_name)
	if flag==1:
		return aws_fRename(old_name,new_name)
	elif flag==2:
		return f_fRename(old_name,new_name)


def fGetAttr(name):
	if flag==1:
		return aws_fgetAttr(name)
	elif flag==2:
		return f_fgetAttr(name)


def fDelete(name):
	if flag==1:
		return aws_fDelete(name)
	elif flag==2:
		return f_fDelete(name)



