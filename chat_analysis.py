from distutils.filelist import findall
from itertools import count
from typing import final
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv 


messages    = []
num_of_msgs = []

with open('filtered_chat.csv', mode='r') as inp:
    reader = csv.reader(inp)
    for i in reader:
        messages.append(i[0])
        num_of_msgs.append(int(i[1].replace(' ','')))

plt.plot(np.array(messages),np.array(num_of_msgs))
plt.xlabel('Message')
plt.ylabel('Numbers of Message')

plt.show()