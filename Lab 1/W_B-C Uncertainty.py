import numpy as np

def W_BC(meas):
   return meas[0] * (meas[2] - meas[1]) * 1e-6 # mJ

# IWC
# meas = [106143.585, 87221.529, 129529.946]
# u_meas = [1410.685, 826.769, 1169.136]

# RTWC
# meas = [106143.585, 87221.529, 117086.294]
# u_meas = [1410.685, 826.769, 1066.614]

# FBD
# IWC
# meas = [102921.42, 87221.529, 129529.946]
# u_meas = [12.12, 826.769, 1169.136]

# RTWC
meas = [106143.585, 87221.529, 117086.294]
u_meas = [1410.685, 826.769, 1066.614]

D = []
nom = W_BC(meas)

for i in range(len(u_meas)):
   meas_pert = meas.copy()
   meas_pert[i] += u_meas[i]
   W_BC_pert = nom - W_BC(meas_pert)
   D.append(W_BC_pert)
u_W_BC = np.linalg.norm(D)
print("W_BC: {0:.2f}±{1:.2f}".format(nom, u_W_BC))

# IWC W_BC: 4490.767±163.289 mJ
# RTWC W_BC: 3169.953±149.310 mJ

# FBD
# IWC W_BC: 4354.44±147.38
# RTWC W_BC: 3169.95±149.31

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