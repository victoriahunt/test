print(1+1)
print(2+3)
import matplotlib
import numpy
from matplotlib import pyplot as plt

days=(1,2,3,4,5,6,7,8,9,10)
temp = (10,20,15,25,30,35,50,24,28,50)
plt.plot(days,temp, color='purple')
plt.title('day vs. temp')
plt.xlabel('days')
plt.ylabel('temp')
plt.show('plottest1.png')
