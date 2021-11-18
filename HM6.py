import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def distance(self, other):
        return (abs(self.x - other.x) ** 2 + abs(self.y - other.y) ** 2) ** 1/2

    def sum_cords(self):
        return self.x + self.y


random.seed(42)
points = []
for _ in range(10000):
    x, y = random.randint(1, 100), random.randint(1, 100)
    points.append(Point(x, y))
counted_points = []
for point1 in points:
    n = 0
    for point2 in points:
        if point1 is not point2 and abs(point1.x - point2.x) <= 5 and abs(point1.y - point2.y) <= 5:
            if point1.distance(point2) <= 5:
                n += 1
    counted_points.append((point1, n))
rezults = sorted(counted_points, key=lambda a: a[1], reverse=True)
rezults = [i for i in rezults if i[1] == rezults[0][1]]
print(rezults)
if len(rezults) > 1:
    rezults = sorted(rezults, key=lambda a: a[0].sum_cords())
    rezults = [i for i in rezults if i[0].sum_cords() == rezults[0][0].sum_cords()]
    if len(rezults) > 1:
        print(sorted(rezults, key=lambda i: i[0].x)[0][0])
    else:
        print(rezults[0][0])
else:
    print(rezults[0][0])
