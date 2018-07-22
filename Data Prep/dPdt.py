import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

__author__ = "Abdulelah Alshehri"
__email__ = "asaalshehr@gmail.com"

# Define file to read
xlf = r'C:\Users\shehrias\Desktop\First delivery_data_CTM\PRF 100\ic8h18_Tw=185_Pin=1.4_phi=0.4_EGR=0.4.csv'
# Read Data
df = pd.read_csv(xlf)
cols = ['t [s]', 'P [bar]']
df = df[cols]
dpdf=df['P [bar]'].diff()
print(np.max(dpdf))
fig, ax = plt.subplots()
ax.plot(df['t [s]'], dpdf)
ax.set(xlabel='time (s)', ylabel='dP (bar)',
       title='ID')
ax.grid()

fig.savefig("test.png")
plt.show()