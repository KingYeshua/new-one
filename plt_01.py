
from matplotlib import pyplot as plt 


days = [0,1,2,3,4,5,6,7]

cash = [10,20,30,40,80,177,333,666]

caffeine = [100,333,80,112,0,0,0,0]

plt.plot(days, cash, linestyle = ':', color = 'red')

plt.plot(days, caffeine, color = 'green')

plt.show()