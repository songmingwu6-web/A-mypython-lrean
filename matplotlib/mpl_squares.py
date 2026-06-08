import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]#x轴数据
squares = [1,4,9,16,25]#y轴数据
plt.plot(input_values,squares,linewidth=5)
#设置图表标题，并给坐标轴加上标签
plt.title("squares numbers",fontsize = 24)
plt.xlabel("value",fontsize = 14)
plt.ylabel("square of value",fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis = 'both',labelsize = 14)
plt.show()