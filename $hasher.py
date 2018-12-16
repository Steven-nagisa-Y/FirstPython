#coding:utf-8
#author:StevenYan.studio
import hashlib
import os
import time
import base64

def writefile(text):
#	print(text)
	f.write(text+'\n')
def hasher(files):
	hasher1 = hashlib.md5()
	hasher2 = hashlib.sha1()
	hasher3 = hashlib.sha256()
	#file_name = input('Input a filename:')
	with open(files,'rb') as fileOj1:
		infile1 = fileOj1.read()
		hasher1.update(infile1)
		hasher2.update(infile1)
		hasher3.update(infile1)
		writefile('The md5 of '+files+' is:'+hasher1.hexdigest())
		writefile('The sha1 of '+files+' is:'+hasher2.hexdigest())
		writefile('The sha256 of '+files+' is:'+hasher3.hexdigest())
		writefile('\n')
		
def base64encode(files):
	with open(files,'rb') as fileOj2:
		infile2 = fileOj2.read()
		b64encode = base64.b64encode(infile2)
		writefile('The base64 of '+files+' is: '+str(b64encode))
		writefile('\n')
	
def getListFiles(path):
	ret = [] 
	for root, dirs, files in os.walk(path):
		for filespath in files:
			return files
	
def getDirsFiles(path):
	ret = [] 
	for root, dirs, files in os.walk(path):
		for filespath in files:
			ret.append(os.path.join(root,filespath))
	return ret

if __name__ == '__main__':
	print('What do you want to do?')
	toDo = input('Enter \'hash\' to calc hash of files.\nEnter \'base64\' to calc base64 of files.\n>')
	toGet = input('Calc all files in dirs?(y/n)\n>')
	if toGet == 'y':
		s_toget = True
	else:
		s_toget = False
	if toDo == 'hash':
		print('Progressing...\n')
		f = open('hashlist.txt','w+')
		start = time.clock()
		writefile('########## The Beginning of File ##########\n')
		writefile('The progressing path is: '+os.getcwd())
		writefile('There are(is) '+str(len(getListFiles('./')))+' item(s)\n')
		if s_toget:	
			for i in getDirsFiles('./'):
				writefile('This is '+i)
				writefile('File size:%.3f'%(os.path.getsize(i)/1024/1024)+'MB')
				hasher(i)
		else:
			for i in getListFiles('./'):
				writefile('This is '+i)
				writefile('File size:%.3f'%(os.path.getsize(i)/1024/1024)+'MB')
				hasher(i)
		end = time.clock()
		writefile('Total time consuming：'+str(end-start)+'s\n')
		print('Done.\n')
		print('Total time consuming：'+str(end-start)+'s\n')
		writefile('\n########## The End of File ##########')
	elif toDo == 'base64':
		print('Progressing...\n')
		f = open('base64list.txt','w+')
		start = time.clock()
		writefile('########## The Beginning of File ##########\n')
		writefile('The progressing path is: '+os.getcwd())
		writefile('There are(is) '+str(len(getListFiles('./')))+' item(s)\n')
		if s_toget:
			for i in getDirsFiles('./'):
				writefile('This is '+i)
				writefile('File size:%.3f'%(os.path.getsize(i)/1024/1024)+'MB')
				base64encode(i)
		else:
			for i in getListFiles('./'):
				writefile('This is '+i)
				writefile('File size:%.3f'%(os.path.getsize(i)/1024/1024)+'MB')
				base64encode(i)
		end = time.clock()
		writefile('Total time consuming：'+str(end-start)+'s\n')
		print('Done.\n')
		print('Total time consuming：'+str(end-start)+'s\n')
		writefile('\n########## The End of File ##########')
	else:
		quit()