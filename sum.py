import time

innum = input('How many numbers do you want to sum up? ')
#method = input('Choose a method in 1..2  ')
def m1(all):
	num = 1
	sum = 0
	print('progressing...')
	start1 = time.clock()
	while num <= int(all):
		sum += num
		num += 1
	print('The sum is '+str(sum))
	end1 = time.clock()
	print('方法一用时：'+str(end1-start1)+'s')
def m2(all):
	num = 1
	sum = 0
	print('progressing...')
	start2 = time.clock()
	sum = (num + int(all))*int(all)/2
	print('The sum is '+str(sum))
	end2 = time.clock()
	print('方法二用时：'+str(end2-start2)+'s')
m1(innum)
m2(innum)