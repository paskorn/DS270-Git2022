import matplotlib.pyplot as plt


plt.plot([1950, 1960, 1970, 1980, 1990, 2000, 2010], 
         [200, 350, 400, 150, 600, 50, 100],
         color='red', marker='+', linestyle='--')
plt.title("Graph")
plt.ylabel("Data")
plt.show()


