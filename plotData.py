import numpy as np
import matplotlib.pyplot as plt

"""
han     : 141144        31.18% of tweets
hon     : 47769 10.55% of tweets
det     : 106402        23.50% of tweets
denne   : 1334  0.29% of tweets
den     : 262684        58.02% of tweets
denna   : 4139  0.91% of tweets
hen     : 4290  0.95% of tweets
('Time: ', '146.05\tTweets counted: 452723')

"""
y = [47769, 106402, 1334, 262684, 4139, 141144, 4290]
x_label = ["hon", "det", "denne", "den", "denna", "han", "hen"]

count = 452723.0
time = 146.05
y_norm = [val/count for val in y]

N = 7
men_means = (20, 35, 30, 35, 27)
men_std = (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, y, width, color='b')

# add some text for labels, title and axes ticks
ax.set_ylabel('Amount')
figure_title = ax.set_title('Tweet occurence of Swedish pronouns', y=1.06)

ax.set_xticks(ind + width / 2)
ax.set_xticklabels(x_label)


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
set_ylabel = x_label
sizes = [15, 30, 45, 10]
explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(y_norm, explode=explode, labels=x_label, autopct='%1.2f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()