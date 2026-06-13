import matplotlib.pyplot as plt
x_values = [1,2,3,4,5]
y_values = [x**3 for x in x_values]
#设置图表标题并给坐标轴加上标签
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors = 'none', s=40)
plt.title("squares Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("square of Values ", fontsize = 14)
#设置刻度标记的样式大小
plt.tick_params(axis = 'both',which = 'major',labelsize =14)
plt.show()