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

print("Steady State Evaporator Temperature (2.92±0.04 W): {0:.3f}±{1:.3f} °C".format(np.mean(evap_avg[2200:2600]), 2 * np.std(evap_avg[2200:2600])))
print("Steady State Condenser  Temperature (2.92±0.04 W): {0:.3f}±{1:.3f} °C".format(np.mean(cond_avg[2200:2600]), 2 * np.std(cond_avg[2200:2600])))
print()

print("Steady State Evaporator Temperature (5.93±0.06 W): {0:.3f}±{1:.3f} °C".format(np.mean(evap_avg[4600:4800]), 2 * np.std(evap_avg[4600:4800])))
print("Steady State Condenser  Temperature (5.93±0.06 W): {0:.3f}±{1:.3f} °C".format(np.mean(cond_avg[4600:4800]), 2 * np.std(cond_avg[4600:4800])))
print()

print("Steady State Evaporator Temperature (9.02±0.08 W): {0:.3f}±{1:.3f} °C".format(np.mean(evap_avg[6800:7100]), 2 * np.std(evap_avg[6800:7100])))
print("Steady State Condenser  Temperature (9.02±0.08 W): {0:.3f}±{1:.3f} °C".format(np.mean(cond_avg[6800:7100]), 2 * np.std(cond_avg[6800:7100])))
print()

print("Steady State Evaporator Temperature (12.06±0.09 W): {0:.3f}±{1:.3f} °C".format(np.mean(evap_avg[8300:8700]), 2 * np.std(evap_avg[8300:8700])))
print("Steady State Condenser  Temperature (12.06±0.09 W): {0:.3f}±{1:.3f} °C".format(np.mean(cond_avg[8300:8700]), 2 * np.std(cond_avg[8300:8700])))
print()