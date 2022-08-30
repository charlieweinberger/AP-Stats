from stats import *

data = [200, 192, 178, 171, 168, 162, 157, 156, 153, 149, 145, 145, 142, 137, 132, 131, 129, 124, 122, 120, 117, 116, 114, 114, 107, 107, 107, 106, 100, 76]

stats = APStats(data, ' homeruns')
stats.histogram("histogram.png", max(data) - min(data))
stats.boxplot("boxplot.png")

stats.mean()
stats.median()
stats.five_point_summary()
stats.IRQ()
stats.stdev()
stats.range()
stats.variance()