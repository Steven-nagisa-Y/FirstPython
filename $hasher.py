#coding:utf-8
#author:StevenYan.studio
import hashlib
import os
import time

def writefile(text):
#	print(text)
	f.write(text+'\n')
def hasher(files):
	hasher1 = hashlib.md5()
	hasher2 = hashlib.sha1()
	hasher3 = hashlib.sha256()
	#file_name = input('Input a filename:')
	with open(files,'rb') as afile:
		infile = afile.read()
		hasher1.update(infile)
		hasher2.update(infile)
		hasher3.update(infile)
		writefile('The md5 of '+files+' is:'+hasher1.hexdigest())
		writefile('The sha1 of '+files+' is:'+hasher2.hexdigest())
		writefile('The sha256 of '+files+' is:'+hasher3.hexdigest())
		writefile('\n')
def getListFiles(path):
	ret = [] 
	for root, dirs, files in os.walk(path):
		for filespath in files:
			return files

if __name__ == '__main__':
	print('Progressing...\n')
	f = open('hashlist.txt','w+')
	start = time.clock()
	writefile('########## The Beginning of File ##########\n')
	writefile('The progressing path is: '+os.getcwd())
	writefile('There are(is) '+str(len(getListFiles('./')))+' item(s)\n')
	for i in getListFiles('./'):
		writefile('This is '+i)
		writefile('File size:%.3f'%(os.path.getsize(i)/1024/1024)+'MB')
		hasher(i)
	end = time.clock()
	writefile('Total time consuming：'+str(end-start)+'s\n')
	print('Done.\n')
	print('Total time consuming：'+str(end-start)+'s\n')
	writefile('\n########## The End of File ##########')