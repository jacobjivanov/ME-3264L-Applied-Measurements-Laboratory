import numpy as np

def W_DAp(meas):
   return meas[0] * (meas[2] - meas[1]) * 1e-6 # mJ

# IWC
# meas = [104801.183, 131189.100, 87221.529]
# u_meas = [1926.619, 1182.886, 826.769]

# RTWC
# meas = [103218.306, 120404.602, 88880.683]
# u_meas = [1905.130, 1093.842, 839.774]

# FBD
# IWC
# meas = [101738.89, 131189.100, 87221.529]
# u_meas = [7.54, 1182.886, 826.769]

# RTWC
meas = [101738.89, 120404.602, 88880.683]
u_meas = [7.54, 1093.842, 839.774]

D = []
nom = W_DAp(meas)

for i in range(len(u_meas)):
   meas_pert = meas.copy()
   meas_pert[i] += u_meas[i]
   W_DAp_pert = nom - W_DAp(meas_pert)
   D.append(W_DAp_pert)
u_W_DAp = np.linalg.norm(D)
print("W_DAp: {0:.3f}±{1:.3f}".format(nom, u_W_DAp))

# IWC W_DAp: -4607.853±173.353 mJ
# RTWC W_DAp: -3253.846±154.492 mJ

# FBD 
# IWC W_DAp: -4473.212±146.828
# RTWC W_DAp: -3207.209±140.301

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