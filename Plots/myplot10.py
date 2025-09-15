from pylab import *

items = ['Samsung', 'Huawei', 'Apple', 'Oppo']

proportions = [40, 20, 30, 50]

colors = ['r', 'y', 'g', 'b']

pie(proportions, labels=items, colors=colors,
        startangle=20, shadow=True, explode=(0.1, 0, 0, 0),
        radius=1.2, autopct='%1.1f%%')


title('Market share of smart phones')
legend()
show()