import matplotlib.pyplot as plt
x_values = [1,2,3,4,5]#x轴数据
y_values = [1,4,9,16,25]#y轴数据
plt.scatter(x_values,y_values,s=100)#s参数设置散点的大小
#设置图表标题并给坐标轴加上标签
plt.title("Squares Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
#设置刻度标记的大小
plt.tick_params(axis = 'both',which = 'major',labelsize = 14)
plt.show()