import numpy as np
import pandas as pd

a = np.array(range(12))
print('1 - исходный вектор', a)
a = a.reshape((4, 3))
print('2 - смена размерности\n', a)
# b = np.array([2, 3, 5, 6])
# print(b)
# c = a.dot(b)
# print('3 - произведение матрицы и вектора\n', c)
a = np.delete(a, 2, 0)
print('4 - удалена строка\n', a)
try:
    a = np.linalg.inv(a)
    print('5 - обратная матрица\n', a)
except:
    print('5 - детерминант равен нулю')
ds = pd.read_csv('https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv')
print('1, 2 - первые 3 строки таблицы\n', ds.head(3))

ds_bmw = ds.loc[ds['Make'] == "BMW"]
print('3 - отфильтровано по производителю BMW\n', ds_bmw)

print('4 - средняя стоимость автомобиля BMW - \n', round(ds_bmw['MSRP'].mean(), 2))

print('5 - C ручной коробкой больше' if len(ds.loc[ds['Transmission Type'] == "AUTOMATIC"]) >
                                    len(ds.loc[ds['Transmission Type'] == "MANUAL"])
                                else 'C автоматической коробкой больше')

# for i in ds:
#     print(i)



