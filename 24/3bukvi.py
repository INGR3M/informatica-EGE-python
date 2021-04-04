"""Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите максимальную длину цепочки вида XYZXYZXYZ... (составленной из фрагментов XYZ, последний фрагмент может быть неполным).

Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма. 
Ответ: 13"""

f = open('3bukvi.txt')
s = f.read().strip()
 
k = 0
kmax = 0
 
frags = ['X', 'Y', 'Z']
frag_index = 0
 
for i in s:
    if i == frags[frag_index]:
        k += 1
        frag_index = (frag_index + 1) % 3
    else:
        kmax = max(k, kmax)
        k = 0
        frag_index = 0
        if i == 'X':
            k = 1
            frag_index = 1
 
kmax = max(k, kmax)
 
print(kmax)
