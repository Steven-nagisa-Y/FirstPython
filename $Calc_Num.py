#coding:utf-8
#author:StevenYan.studio
import os

def inputData():
	data0 = {}
	print('Please input a list of numbers (enter Q to quit):')
	i = 1
	while True:
		numIn = input('>')
		if numIn.lower() == 'q':
			break
		if numIn.isdigit() != True:
			print('Sorry,what you input is not a number!')
		else:
			if len(numIn) > 30:
				print('Sorry,The number is too lonnnnng.')
			else:
				data0[i] = float(numIn)
				i += 1
	return data0

def printData(data1):
	print('--id-- # --------------num---------------\n')
	for keys in data1.keys():
		print(''+str(keys).center(6)+' : '+str(data1[keys]).ljust(30))
	print('\n')

def theOne(data2):
	largest = max(data2.values())
	wherel = list(data2.values()).index(largest) + 1
	smallest = min(data2.values())
	wheres = list(data2.values()).index(smallest) + 1
	print('The largest number is at id '+str(wherel))
	print('The largest number is '+str(largest))
	print('The smallest number is at id '+str(wheres))
	print('The smallest number is '+str(smallest))
	print('\n')
def sumUp(data3):
	sums = 0
	i = 0
	while i < len(data3.values()):
		sums = sums + list(data3.values())[i]
		i += 1
	print('The sum of numbers is '+str(sums))
	print('\n')
	
if __name__ == '__main__':
	data = inputData()
	printData(data)
	theOne(data)
	sumUp(data)
	