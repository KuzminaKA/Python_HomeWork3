#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

N=int(input("введите число N: "))
data = list()
for i in range(N):
    i=int(input("введите число: "))
    data.append(i)
print(data)

X=int(input("введите число Х: "))
count=0
for i in range(N):
    if data[i]==X:
        count+=1
print(count)