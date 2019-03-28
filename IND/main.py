import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random 
prt = lambda s, e=30: print((e-len(s))*'_', s, (e-len(s))*'_')

s1 = pd.Series([0, 10, 20, 30])
dates = pd.date_range('20190208', periods=20)

df = pd.DataFrame(np.random.randn(20, 4), index=dates, columns=list('ABDC'))

print(df.loc['20190201':'20190209', 'B'])
