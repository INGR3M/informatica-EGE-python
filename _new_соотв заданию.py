'''
Задание 23 № 15959

Исполнитель РазДваТри преобразует число на экране.

У исполнителя есть три команды, которым присвоены номера:

1. Прибавить 1

2. Умножить на 2

3. Умножить на 3

Первая команда увеличивает число на экране на 1, вторая умножает его на 2, третья умножает его на 3.

Программа для исполнителя РазДваТри — это последовательность команд.

Сколько существует программ, которые преобразуют исходное число 3 в число 50 и при этом траектория вычислений содержит число 15 и не содержит числа 33?

Траектория вычислений — это последовательность результатов выполнения всех команд программы. Например, для программы 312 при исходном числе 6 траектория будет состоять из чисел 18, 19, 38.

Ответ:121
'''

krn1 = 3 
lst1 = 15
krn2 = lst1
lst2 = 50
excp = 33
count = 0

def tree(tkrn,tlst,texcept,tcount):
	tlst1 = tkrn + 1
	tlst2 = tkrn * 2
	tlst3 = tkrn * 3

	if tlst1 == tlst:
		tcount += 1
	elif tlst1 < tlst and tlst1 != texcept: 
		tcount = tree(tlst1,tlst,texcept,tcount)

	if tlst2 == tlst:
		tcount += 1
	elif tlst2 < tlst and tlst2 != texcept: 
		tcount = tree(tlst2,tlst,texcept,tcount)

	if tlst3 == tlst:
		tcount += 1
	elif tlst3 < tlst and tlst3 != texcept: 
		tcount = tree(tlst3,tlst,texcept,tcount)

	return tcount

print(tree(krn1,lst1,excp,count)*tree(krn2,lst2,excp,count))