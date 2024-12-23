import matplotlib.pyplot as plt
import numpy as np
from math import sin,sqrt
import matplotlib


# 1 задание
def first_func(x):
    return x ** 2


def second_func(x):
    return x ** 3


def two_func():
    x = np.linspace(0,100,1000)
    first_y = [first_func(i) for i in x]
    second_y = [second_func(i) for i in x]
    fig, ax1 = plt.subplots()

    ax1.plot(x, first_y, 'b-',label='Первая функция')
    ax1.set_xlabel('Ось Х')
    ax1.set_ylabel('Ось Y для первой функции')

    ax2 = ax1.twinx()
    ax2.plot(x, second_y, 'r-', label='Вторая функция')
    ax2.set_ylabel('Ось Y для второй функции')

    fig.legend(loc="upper left")
    plt.title("График двух функций")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('two_func.png')
    plt.savefig('two_func.pdf')
    
    plt.close()


# 2 задание
def create_clusters():
    first_cluster_x = np.random.normal(2,0.5,50)
    first_cluster_y = np.random.normal(2,0.5,50)
    
    second_cluster_x = np.random.normal(4,0.5,50)
    second_cluster_y = np.random.normal(4,0.5,50)
    
    third_cluster_x = np.random.normal(8,0.5,50)
    third_cluster_y = np.random.normal(8,0.5,50)
    
    plt.scatter(first_cluster_x, first_cluster_y, color='blue', marker='o')
    plt.scatter(second_cluster_x, second_cluster_y, color='red', marker='o')
    plt.scatter(third_cluster_x, third_cluster_y, color='green', marker='o')
    
    plt.savefig('clusters.png')
    plt.savefig('clusters.pdf')
    
    plt.close()
    
    
# 3 задание
def create_circular_diag():
    vals = [21,19,38,12,10]
    labels = ["footbal","race","hockey","ufc","run"]
    
    plt.pie(vals, labels=labels, autopct='%1.1f%%')
    
    plt.savefig('circular_diagram.png')
    plt.savefig('circular_diagram.pdf')
    
    plt.close()


# 4 задание
def create_heatmap():
    matrix = np.random.rand(10,10)
    plt.imshow(matrix)
    plt.colorbar()
    
    plt.savefig('heatmap.png')
    plt.savefig('heatmap.pdf')
    
    plt.close()
    
    
# 5 задание
def create_bar_char():
    x = np.arange(1, 8)
    y = np.random.randint(1, 20, size = 7)
    
    _, ax = plt.subplots()
    bars=ax.barh(x, y)
    ax.bar_label(bars,label_type='center',fontsize=20)
    
    plt.savefig('bar_char.png')
    plt.savefig('bar_char.pdf')
    
    plt.close()
    
    
# 7 задание
def f(x,y):
    return sin(sqrt(x ** 2 + y ** 2))


def create_surface_plot():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    z = [f(x[i],y[i]) for i in range(len(x))]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label='parametric curve')
    
    plt.savefig('surface_plot.png')
    plt.savefig('surface_plot.pdf')
    
    plt.close()


if __name__ == "__main__":
    matplotlib.use("Agg")
    two_func()