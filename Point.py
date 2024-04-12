class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    def get_coordinates(self):
        return (self.x, self.y)
    def distance_to(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
# Пример использования:
point1 = Point(2, 3)
point2 = Point(5, 7)
print(f"Координаты точки 1: {point1.get_coordinates()}")
print(f"Координаты точки 2: {point2.get_coordinates()}")
print(f"Расстояние между точкой 1 и точкой 2: {point1.distance_to(point2)}")


#Этот класс Point позволяет создавать объекты точек с координатами (x, y),
#получать и изменять эти координаты, а также вычислять расстояние до другой точки.
#Метод distance_to использует евклидово расстояние для вычисления дистанции между двумя точками.
