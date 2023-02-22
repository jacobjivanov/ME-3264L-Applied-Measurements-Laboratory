import numpy as np

def pD(v):
   return v[0] * (v[1] / v[2])

# IWC
# v = [106143.585, 129529.946, 131189.100]
# u_v = [1410.685, 1169.136, 1182.886]

# RTWC
v = [106143.585, 117086.294, 120404.602]
u_v = [1410.685, 1066.614, 1093.842]

D = []
nom = pD(v)
for i in range(len(u_v)):
   v_pert = v.copy()
   v_pert[i] += u_v[i]
   pD_pert = nom - pD(v_pert)
   D.append(pD_pert)
u_pD = np.linalg.norm(D)
print("Pressure D: {0:.3f}±{1:.3f}".format(nom, u_pD))
# IWC: Pressure D: 104801.183±1926.619 Pa
# RTWC: Pressure D: 103218.306±1905.130 Pa

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