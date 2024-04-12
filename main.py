# First argument must be an iterable of pandas objects

import pandas as pd

df1 = pd.DataFrame({
    'letter': ['A', 'B'],
    'number': [1, 2]
})

df2 = pd.DataFrame({
    'letter': ['C', 'D'],
    'number': [3, 4]
})

df3 = pd.concat([df1, df2])

# 0      A       1
# 1      B       2
# 0      C       3
# 1      D       4
print(df3)