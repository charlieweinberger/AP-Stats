from stats import *

data = [15, 18, 22, 23, 26, 27, 27, 27, 27, 28, 28, 28, 28, 29, 29, 29, 32, 33, 34, 34, 36, 38, 40, 41, 41, 42, 42, 43, 46, 50, 50]
activity = 'complete a logic puzzle'
unit = 'seconds'

stats = APStats(data, activity, unit)

stats.mean()
stats.median()
stats.IRQ(print_quanitles=False)
stats.stdev()
stats.range()
stats.variance()