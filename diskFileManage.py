import os
import json


def f_fCreate(name):
	open(name,'w').close
	return "Created File"

def f_fOpen(name):
	try:
		file = open(name,'r')
		text = file.read()
	except FileNotFoundError:
		return "File does not exists"
	return text


def f_fRename(old_name, new_name):
	try:
		os.rename(old_name,new_name)
	except FileNotFoundError:
		return "File does not exists"
	return "File name changed"


def f_fgetAttr(name):
	try:
		info = os.stat(name)
	except FileNotFoundError:
		return "File not found"
	file_attr={}
	file_attr['LastModified'] = info.st_mtime
	file_attr['Size'] = info.st_size
	file_ext=name.split('.')
	print(file_ext)
	if len(file_ext)==1:
		file_attr['Type'] = 'Unknown'
	else:
		file_attr['Type'] = file_ext[1]
	return json.dumps(file_attr)


def f_fDelete(name):
	try:
		os.remove(name)
	except FileNotFoundError:
		return "File does not exists"
	return "Deleted file"
