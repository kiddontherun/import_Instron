import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv('Specimen_RawData_1_SN19Z009675.csv', skiprows=2, usecols=[1, 2], names=["Extension", "Force"])
df2 = pd.read_csv('Specimen_RawData_2_SN1A0005640.csv', skiprows=2, usecols=[1, 2], names=["Extension", "Force"])
df3 = pd.read_csv('Specimen_RawData_3_SN19Z010748.csv', skiprows=2, usecols=[1, 2], names=["Extension", "Force"])
df4 = pd.read_csv('Specimen_RawData_4_SN1A1008126.csv', skiprows=2, usecols=[1, 2], names=["Extension", "Force"])

EUT1 = df1.to_numpy()
EUT2 = df2.to_numpy()
EUT3 = df3.to_numpy()
EUT4 = df4.to_numpy()

plt.figure()
plt.plot(EUT1[:,0],EUT1[:,1], label='EUT1')
plt.plot(EUT2[:,0],EUT2[:,1], label='EUT2')
plt.plot(EUT3[:,0],EUT3[:,1], label='EUT3')
plt.plot(EUT4[:,0],EUT4[:,1], label='EUT4')
plt.xlabel("Extension (mm)")
plt.ylabel("Force(N)")
plt.legend()
plt.grid()
plt.title("Instron Test 06/27/2019")
plt.show()

#ax = df1.plot(kind='scatter', x='Extension', y='Force', color='Red', label='EUT1')
#df2.plot(kind='scatter', x='Extension', y='Force', color='Blue', label='EUT2', ax=ax)
#df3.plot(kind='scatter', x='Extension', y='Force', color='Green', label='EUT3', ax=ax)
#df4.plot(kind='scatter', x='Extension', y='Force', color='Purple', label='EUT4', ax=ax)
#plt.xlabel("Extension (mm)")
#plt.ylabel("Force (N)")
#plt.legend(loc='upper right')
#plt.show()