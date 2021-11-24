def large(arr):
max_elem = arr[0]
for elem in arr:
if elem > max_elem:
max_elem = elem
return max_elem


a=[]
n=int(input()) # ввод количества элементов массива
print('Введите элементы массива: ')
for i in range(n):
a.append(int(input())) # ввод элементов массива
result = large(a)
print('Максимальный элемент: ', result)