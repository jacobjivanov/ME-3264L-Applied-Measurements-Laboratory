import numpy as np

def W_CD(meas):
   return meas[0] * meas[1] * 1e-6 * np.log(meas[2] / meas[1]) # mJ

# IWC
# meas = [106143.585, 129529.946, 131189.100]
# u_meas = [1410.685, 1169.136, 1182.886]

# RTWC
# meas = [106143.585, 117086.294, 120404.602]
# u_meas = [1410.685, 1066.614, 1093.842]

# FBD
# IWC
# meas = [102921.42, 129529.946, 131189.100]
# u_meas = [12.12, 1169.136, 1182.886]

# RTWC
meas = [102921.42, 117086.294, 120404.602]
u_meas = [12.12, 1066.614, 1093.842]

D = []
nom = W_CD(meas)

for i in range(len(u_meas)):
   meas_pert = meas.copy()
   meas_pert[i] += u_meas[i]
   W_CD_pert = nom - W_CD(meas_pert)
   D.append(W_CD_pert)
u_W_CD = np.linalg.norm(D)
print("W_CD: {0:.2f}±{1:.2f}".format(nom, u_W_CD))

# IWC
# W_CD: 174.990±174.309 mJ, therefore, 
# Q_CD: 174.990±174.309 mJ
# RTWC
# W_CD: 347.318±157.729 mJ, therefore,
# Q_CD: 347.318±157.729 mJ

# FBD
# W_CD: 169.68±169.00 mJ, therefore, 
# Q_CD: 169.68±169.00 mJ
# RTWC
# W_CD: 336.77±152.88 mJ, therefore,
# Q_CD: 336.77±152.88 mJ
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