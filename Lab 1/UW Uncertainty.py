import numpy as np

def UW(meas):
   return (meas[0] + meas[1]) / 1000 * 9.81 * (meas[3] - meas[2]) / 1000 * 1e3 # mJ

meas = [0, 35, 60, 22]
u_meas = [0, 0.6, 0.5, 0.5] 

D = []
nom = UW(meas)

for i in range(len(u_meas)):
   meas_pert = meas.copy()
   meas_pert[i] += u_meas[i]
   UW_pert = nom - UW(meas_pert)
   D.append(UW_pert)
u_UW = np.linalg.norm(D)
print("UW: {0:.3f}±{1:.3f}".format(nom, u_UW))

# IWC
# UW_AB: -6.622±0.937 mJ
# UW_BC: 67.542±0.983 mJ
# UW_CD: 0.687±0.243 mJ
# UW_DAp: -18.198±0.395 mJ

# RTWC
# UW_AB: 6.622±0.937 mJ
# UW_BC: 47.677±0.960 mJ
# UW_CD: 1.373±0.244 mJ
# UW_DAp: -13.047±0.330 mJ