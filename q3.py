def counter(initial,limit,increment):
	val=initial
	while val<limit:
		yield val
		val=val+increment

ctr = counter(0,10,1)

for i in ctr:
	print('Value given by Counter is :',i)