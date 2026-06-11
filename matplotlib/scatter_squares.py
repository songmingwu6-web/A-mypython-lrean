import matplotlib.pyplot as plt
x_values = list(range(1,1001))#创建x轴数据
y_values = [x**2 for x in x_values]#y轴数据
plt.scatter(x_values,y_values,c='red',edgecolors='none',s=40)#s参数设置散点的大小和颜色
#设置图表标题并给坐标轴加上标签
plt.title("Squares Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
#设置刻度标记的大小
plt.axis([0,1100,0,1100000])#设置每个坐标的取值范围
plt.show()