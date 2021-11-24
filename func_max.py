def large(arr):
max_elem = arr[0]
for elem in arr:
if elem > max_elem:
max_elem = elem
return max_elem


list1 = [3,5,9,12,8]
result = large(list1)
print('Максимальный элемент: ', result)