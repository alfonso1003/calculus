import pandas as pd
import numpy as np
from random import random
import matplotlib.pyplot as plt

x = [random() for _ in range(10000)]
y = [random() for _ in range(10000)]

x = map(lambda x: -10 if x < 0.5 else 10, x)
y = map(lambda x: -10 if x < 0.5 else 10, y)

plt.plot(np.cumsum(x), np.cumsum(y))
plt.show()
