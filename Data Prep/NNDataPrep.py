import pandas as pd
import numpy as np


__author__ = "Abdulelah Alshehri"
__email__ = "asaalshehr@gmail.com"

#TODO: fix tol (should be very small)
#Define number of rows and sheets
nr=10
#Define file to read
xlf = 'C:\Users\mrui\Desktop\NNdata\Igni_data_CH2O_EGR_30_40.xlsx'
#Define first
PVP = pd.read_excel(xlf, sheet_name='1.point_value_vs_parameter')

#Initialize list
sheets=[]
#for loop to create sheet names
for i in range(1,nr+1):
    sheets.append(str(i+3)+".soln_no_1_Run#"+str(i))

# t1=PVP['t2'].tolist()
print sheets
cols=['t','T','P','YH2O','YCH2O']
frames=[]
for i in range(0,nr):
    frames.append(pd.read_excel(xlf, sheet_name=sheets[i],header=None, skiprows=1))

allsheets=pd.concat(frames)

t1=PVP['t1'].tolist()
t0=allsheets[0].tolist()
p1=allsheets[3].tolist()

df1 = pd.DataFrame({'time' : t0, 'YCH2O' : [lst2]}, columns=['time','YCH2O'])