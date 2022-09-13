import matplotlib.pyplot as plt
movies = ["Shawshank", "Goodwill \n Hunting",  "Imitation \n Game", "Cast \n Away", "Beutiful \n Mind"] 
num_oscars =[7, 9, 0,3,9]

plt.bar(range(len(movies)), num_oscars)

plt.title("My Facorite Movies")
plt.ylabel("the Number of Academy Awards")
plt.xticks(range(len(movies)), movies)
plt.show()


