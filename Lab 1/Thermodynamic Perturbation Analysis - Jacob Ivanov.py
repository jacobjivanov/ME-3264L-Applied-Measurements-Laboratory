import numpy as np

def total_V(meas_list):
   # D_can, h_can, D_hose, l_hose, D_pis, h_pis
   return np.pi * (meas_list[1] * (meas_list[0] / 2) ** 2 + meas_list[3] * (meas_list[2] / 2) ** 2 + meas_list[5] * (meas_list[4] / 2) ** 2)

h_pis_IWC = [25, 20, 71, 73, 20] # mm
h_pis_RTWC = [25, 20, 56, 60, 22] # mm

u_h_pis = [0.5, 0.5, 0.5, 0.5, 0.5] # mm

for i in range(len(h_pis_IWC)):
   pos = ["A", "B", "C", "D", "A'"]
   # meas = [37.5, 60, 3.3, 510, 32.5, h_pis_IWC[i]] # mm
   meas = [37.5, 60, 3.3, 510, 32.5, h_pis_RTWC[i]] # mm
   u_meas = [0, 0, 0, 25, 0.1, u_h_pis[i]] # mm

   nom = total_V(meas)

   D = []
   for j in range(len(meas)):
      meas_pert = meas.copy()
      meas_pert[j] += u_meas[j]

      D.append(total_V(meas_pert) - nom)
   D = np.array(D)

   u_tV = np.linalg.norm(D)
   print("{0}: Total Volume {1:.3f}±{2:.3f}".format(pos[i], nom, u_tV))

'''
IWC
A: Total Volume 91369.413±859.369
B: Total Volume 87221.529±826.769
C: Total Volume 129529.946±1169.136
D: Total Volume 131189.100±1182.886
A': Total Volume 87221.529±826.769

RTWC
A: Total Volume 91369.413±859.369
B: Total Volume 87221.529±826.769
C: Total Volume 117086.294±1066.614
D: Total Volume 120404.602±1093.842
A': Total Volume 88880.683±839.774
'''
 