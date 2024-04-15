from stats import *
from matplotlib import pyplot as plt

data = [15, 18, 22, 23, 26, 27, 27, 27, 27, 28, 28, 28, 28, 29, 29, 29, 32, 33, 34, 34, 36, 38, 40, 41, 41, 42, 42, 43, 46, 50, 50]

stats = APStats(data)
stats.all(30)

"""

histogram: plt.hist(data)
dotplot: plt.hist(data, max(data) - min(data) + 1)
boxplot: plt.boxplot(data, vert=False, positions=[1])

plt.savefig("name.png")

"""