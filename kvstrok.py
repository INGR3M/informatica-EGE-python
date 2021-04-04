'''Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только заглавные буквы латинского алфавита (ABC…Z). Определите количество строк, в которых буква E встречается чаще, чем буква A.
Ответ: 467 '''

with open("kvstrok.txt", "r") as file:
	count = 0
	line = file.readline()
	while line:
		# print(line, end="")
		if line.count('E') > line.count('A'):
			count += 1
		line = file.readline()
print(count)
		