from math import sqrt
count = 0
j = 2


for i in range(245690,245757):
	count += 1
	numDel = 2
	for j in range(2,i):
		if i % j == 0:
			numDel += 1
			if numDel > 2:
				break
	if numDel == 2:
		print(count,i)
