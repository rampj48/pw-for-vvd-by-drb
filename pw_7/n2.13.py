def angle(x, y):
    return x / ((x ** 2 + y ** 2) ** 0.5)


x1, x2 = map(int, input("Введите координаты точки X: ").split())
y1, y2 = map(int, input("Введите координаты точки Y: ").split())
z1, z2 = map(int, input("Введите координаты точки Z: ").split())

result = [x1, x2]
angle_x = angle(x1, x2)
angle_y = angle(y1, y2)
angle_z = angle(z1, z2)

if angle_x > angle_y:
    result = [y1, y2]
if angle_y > angle_z:
    result = [z1, z2]
print(*result)
