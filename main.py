import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()
def cubic_b_spline_basis(t):
    return (t**3,t**2,t,1)

def evaluate_b_spline_curve(G, Ms, t):
    T = cubic_b_spline_basis(t)
    curve_point = [0, 0]

    for i in range(len(T)):
        for j in range(len(G)):
            curve_point[0] += T[i] * Ms[i * len(G) + j] * G[j][0]
            curve_point[1] += T[i] * Ms[i * len(G) + j] * G[j][1]
    return curve_point

points = [[0, 0], [1, 4], [4, 3], [6, 9],[10, 10], [15,12], [18,18], [12,20],[10,25],[2,27]]
#points = [[4,-2], [0,0], [-4,4], [5,5],[10, 10], [15,12], [12,12], [18,13], [20,13]]

#Пересчитанные весовые коэффициенты для прохода через все точки

Ms = [1/6.0 * x for x in [-1, 3, -3, 1,
                           3, -6, 3, 0,
                           -3, 0, 3, 0,
                           1, 4, 1, 0]]

curve_points = []

for i in range(1, len(points)-2):
    G = points[i-1:i+3]  # Выбираем 4 контрольные точки
    t_values = np.linspace(0, 1, 100)
    curve_points.extend([evaluate_b_spline_curve(G, Ms, t) for t in t_values])

end_time = time.time()
execution_time = end_time - start_time
print("Время выполнения программы:", execution_time, "секунд")

# Визуализация кривой
plt.figure()

# Распаковываем координаты x и y из списка точек кривой
x_curve = [point[0] for point in curve_points]
y_curve = [point[1] for point in curve_points]

# Строим кривую
plt.plot(x_curve, y_curve, color='b')

# Добавляем точки управления
for point in points:
    plt.scatter(point[0], point[1], color='r')

# Настройка осей
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Реализация алгоритма  построение кривой B-Spline')

plt.grid(True)
plt.show()

