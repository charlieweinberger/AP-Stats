from stats import *
from matplotlib import pyplot as plt

damelio = [11.9, 2.2, 20.1, 2.2, 30.2, 5.8, 31.0, 8.1, 29.8, 16.1, 15.9, 38.5, 15.4, 21.9, 12.9, 32.7, 12.6, 11.8, 26.1, 37.2, 28.2, 58.8, 33.2, 44.2, 17.6, 21.3, 25.3, 25.1, 16.8, 15.1, 12.8]
rae = [17.5, 18.8, 13.7, 24.2, 22.1, 13.7, 17.7, 19.6, 57.7, 17.5, 12.0, 15.5, 12.1, 12.1, 15.2, 9.6, 34.5, 36.2, 16.8, 15.7, 20.1, 29.6, 27.1, 65.3, 24.5, 15.1, 17.2, 20.5, 10.3, 9.3, 9.6]

plt.boxplot(damelio, vert=False, positions=[1.5])
plt.boxplot(rae, vert=False)
plt.savefig("both.png")

damelio_stats = APStats(damelio, ' million views')
rae_stats = APStats(rae, ' million views')

print("\nCharli D'Amelio's statistics:")
damelio_stats.all()

print("\nAddison Rae's statistics:")
rae_stats.all()
print('')

"""

plt.histogram(data, max(data) - min(data))
plt.boxplot(data, vert=False, positions=[1.5])
plt.savefig("both.png")

stats = APStats(data)
stats.all()

mean: average
median: typical
IQR: 50% of _ are within {Q1} and {Q3}

"""

"""

Example 1:

male   = [67, 63, 68, 68, 60, 65, 65, 65, 69, 66, 66, 66, 66, 64, 68, 64, 70, 68, 66, 62]
female = [68, 70, 69, 72, 67, 68, 71, 74, 70, 72, 66, 65, 70, 70, 69, 66, 70, 72, 68, 72]

plt.boxplot(male, vert=False, positions=[1.5])
plt.boxplot(female, vert=False)
plt.savefig("both.png")

male_class = APStats(male)
female_class = APStats(female)
male_class.all()
female_class.all()

The distribution of the heights of the female students in this AP Stats class is skewed left, whereas distribution of the heights of the male students is roughtly symmetric. A typical female student has a height of 66 inches, whereas a typical male student has a height of 70 inches. Male students tend to be taller than female students. Both female and male heights, among the middle 50%, vary by 3.5 inches. However, female heights have a range of 10 inches, which is slightly larger than the range of male heights, which is 9 inches. There are no male or female students with unusual heights.

"""

"""

Example 2:

The distribution of the number of views (in millions) that Charli D'Amelio has recieved on her 31 most recent tiktok videos is roughly symmetric.
The distribution of the number of views (in millions) that Addison Rae has recieved on her 31 most recent tiktok videos is skewed right.

A typical Charli D'Amelio tiktok has 20.1 million views.
A typical Addison Rae tiktok has 17.5 million views.

The middle 50% of Charli D'Amelio tiktoks vary in view count by 17.4 million views.
The middle 50% of Addison Rae tiktoks vary in view count by only 10.5 million views.

Charli D'Amelio has one outlier video, at 58.8 million views.
Addison Rae has two outlier videos, at 57.7 and 65.3 million views.

"""

"""

Example 3 (page 97 #16):

From 2002 to 2004, the average weekly gas price at a service station in the midwestern United States increased. The range of the distributions also increased with time.

The distribution in 2002 is symmetric. The typical gas price was about 1.35 dollars per gallon. There were 4 weeks during which gas prices were unusually low, three of which were extremely low.

The distribution in 2003 is skewed right. The typical gas price was about 1.5 dollars per gallon.

The distribution in 2004 is symmetric. The typical gas price was about 1.70 dollars per gallon. There was 1 week during which gas prices were unusually high.

[add IQRs]
[add values for outliers]

"""
