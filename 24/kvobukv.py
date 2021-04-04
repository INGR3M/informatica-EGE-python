'''Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите длину самой длинной последовательности, состоящей из символов X. Хотя бы один символ X находится в последовательности.

Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
Ответ: 19 '''

f = open('kvobukv.txt') # к-во букв б (For each)
str = f.read()
count = 0
maxi = 0
for i in str:
	if i == 'X':
		count += 1
	else:
		count = 0
	if count > maxi:
		maxi = count
print(maxi)