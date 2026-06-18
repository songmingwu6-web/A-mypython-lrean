import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # 显式创建 figure 和 axes 对象
    fig, ax = plt.subplots()
    
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    
    # 使用 ax 对象绘制（面向对象方式）
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  
    
    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break