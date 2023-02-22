import numpy as np

def Q_BC(meas):
   return meas[0] * 1e-6 * meas[1] * meas[2] * (meas[4] - meas[3]) # mJ

# IWC
# meas = [91369.413, 1.292, 1000, 0, 100]
# u_meas = [859.369, 0, 0, 0, 0]

# RTWC
meas = [91369.413, 1.292, 1000, 20, 100]
u_meas = [859.369, 0, 0, 0, 0]

D = []
nom = Q_BC(meas)

for i in range(len(u_meas)):
   meas_pert = meas.copy()
   meas_pert[i] += u_meas[i]
   Q_BC_pert = nom - Q_BC(meas_pert)
   D.append(Q_BC_pert)
u_Q_BC = np.linalg.norm(D)
print("Q_BC: {0:.3f}±{1:.3f}".format(nom, u_Q_BC))

# IWC Q_BC: 11804.928±111.030 mJ
# RTWC Q_BC: 9443.943±88.824 mJ

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