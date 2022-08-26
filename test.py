from stats import *

data = [7.5, 4.2, 4.5, 3.4, 1.9, 4.4, 3.1, 3.2, 2.6, 2.6, 2.6, 3.3, 2.8, 2.9, 3.3, 2.3, 1.7, 2.2, 1.5, 1.4]

stats = APStats(data, '%')
stats.hist("plot.png", 6)

stats.mean()
stats.median()
stats.five_point_summary()
stats.IRQ()
stats.stdev()
stats.range()
stats.variance()