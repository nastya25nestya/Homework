def minimum(arr):
min_elem = arr[0]
for elem in arr:
if elem < min_elem:
min_elem = elem
return min_elem


a=[]
n=int(input()) # ввод количества элементов массива
print('Введите элементы массива: ')
for i in range(n):
a.append(int(input())) # ввод элементов массива
result = minimum(a)
print('Минимальный элемент: ', result)