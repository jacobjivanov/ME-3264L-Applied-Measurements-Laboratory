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

fig, ax = plt.subplots(1, 1, figsize = (6.5, 3))

plt.plot(time, evap1, label = "heat 7")
plt.plot(time, evap2, label = "heat 1")
plt.plot(time, evap3, label = "heat 2")

plt.plot(time, cond1, label = "heat 3")
plt.plot(time, cond2, label = "heat 4")
plt.plot(time, cond3, label = "heat 6")
plt.plot(time, cond4, label = "heat 5")

plt.ylim(100, 110)
plt.xlim(3700, 4400)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Figure 1: Final Steady State Temperature Approach") #\n$P = 12.06±0.09$ W")
plt.legend(bbox_to_anchor=(1.05, 1.0))
plt.tight_layout()
plt.show()
fig.savefig('Figure 1.png', dpi = 300)