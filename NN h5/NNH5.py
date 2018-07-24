import pandas as pd
import numpy as np
import keras
import h5py
from keras.models import load_model
import csv


__author__ = "Abdulelah Alshehri"
__email__ = "asaalshehr@gmail.com"

#Define a temporary file to write to
Temp= r'C:\Users\shehrias\Desktop\Data Prep\NN h5\Temp.csv'
#Define Data file csv file
xlf = r'C:\Users\shehrias\Desktop\Data Prep\NN h5\First delivery_data_CTM\PRF 000\nc7h16_Tw=135_Pin=1.4_phi=0.4_EGR=0.0.csv'

#Initial values
df = pd.read_csv(xlf)

#TODO: Change EGR and phi
df['EGR']=0.0
df['phi']=0.4
gamma=1.4

V0= df['Vol [m3]'].iloc[0]
P0=df['P [bar]'].iloc[0]
T0=df['T [K]'].iloc[0]
#delta T
dt=df['t [s]'].iloc[1] - df['t [s]'].iloc[0]
V=df['Vol [m3]']

dfT = pd.DataFrame({'T': 1000/((T0*V0**gamma)/(V**gamma))})
dfP = pd.DataFrame({'P': (P0*V0**gamma)/(V**gamma)})
df=pd.merge(df, dfP , left_index=True, right_index=True, how='inner');
dfs = pd.merge(df, dfT , left_index=True, right_index=True, how='inner');
dfs.drop(columns=['t [s]', 'P [bar]', 'T [K]', 'Q loss [W]'], inplace=True)

dfs.to_csv(Temp, sep=',',encoding='utf-8', index=False, header=False)

#Loading models
#Tau
model1 = load_model('ID_Octane.h5')
#CCm
model2 = load_model('HO2_Octane.h5')

test = np.loadtxt('Temp.csv', delimiter=",")
x = test[:, 1:5]

Tau = model1.predict(x)
CCm= model2.predict(x)

# print(Tau)
print(CCm)
sum =0
i=0

# while i <= len(Tau)-1:
#    sum += (CCm[i]*dt/Tau[i])
#    i += 1
#    print(sum)
#    if sum/CCm[i-1] >= 1:
#       print(i-1)
#       print(sum)
#       break


