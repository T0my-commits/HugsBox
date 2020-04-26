import random
import pylab as plt
import seaborn as sns
 
data = [sum(random.randint(1,6) for i in range(5)) for i in range(1000)]
ax = sns.distplot(data)
plt.show()
