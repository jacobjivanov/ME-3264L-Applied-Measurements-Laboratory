import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Heat Pipe Data.csv')

time = np.array(df['Time (s)'])

evap1 = np.array(df["Evaporator Position 1 (°C)"])
evap2 = np.array(df["Evaporator Position 2 (°C)"])
evap3 = np.array(df["Evaporator Position 3 (°C)"])

cond1 = np.array(df["Condenser Position 1 (°C)"])
cond2 = np.array(df["Condenser Position 2 (°C)"])
cond3 = np.array(df["Condenser Position 3 (°C)"])
cond4 = np.array(df["Condenser Position 4 (°C)"])

evap_avg = np.zeros(len(evap1))
cond_avg = np.zeros(len(cond1))

for i in range(len(evap1)):
   evap_avg[i] = (evap1[i] + evap2[i] + evap3[i]) / 3
   cond_avg[i] = (cond1[i] + cond2[i] + cond3[i] + cond4[i]) / 4

fig, ax = plt.subplots(1, 1, figsize = (6.5, 3.4))
plt.tight_layout(pad = 3)
plt.title("Figure 2: Average Evaporator, Condenser \nTemperatures over Time")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")

plt.xlim(0, time[-1])
plt.ylim(0, 120)
# plt.grid()

plt.plot(time, evap_avg, color = 'red', label = "Evaporator Average")
plt.plot(time, cond_avg, color = 'blue', label = "Condenser Average")
plt.legend()
plt.show()
fig.savefig('Figure 2.png', dpi = 300)