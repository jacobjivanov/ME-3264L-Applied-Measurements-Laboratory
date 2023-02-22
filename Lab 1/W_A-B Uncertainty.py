import numpy as np

def W_AB(meas):
   return meas[0] * meas[1] * 1e-6 * np.log(meas[2] / meas[1]) # mJ

# IWC
# meas = [101325, 91369.413, 87221.529]
# u_meas = [0, 859.369, 826.769]

# RTWC
# meas = [101325, 91369.413, 87221.529]
# u_meas = [0, 859.369, 826.769]

# FBD IWC
meas = [101738.89, 91369.413, 87221.529]
u_meas = [7.54, 859.369, 826.769]

D = []
nom = W_AB(meas)

for i in range(len(u_meas)):
   meas_pert = meas.copy()
   meas_pert[i] += u_meas[i]
   W_AB_pert = nom - W_AB(meas_pert)
   D.append(W_AB_pert)
u_W_AB = np.linalg.norm(D)
print("W_AB: {0:.2f}±{1:.2f}".format(nom, u_W_AB))
# W_AB: -430.123±126.516 mJ, therefore, 
# Q_AB: -430.123±126.516 mJ

# FBD
# W_AB: -431.88±127.03 mJ, therefore,
# Q_AB: -431.88±127.03

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