import numpy as np

def pB(v):
   return 101325 * (v[0] / v[1])

v = [91369.413, 87221.529]
u_v = [859.369, 826.769]
D = []
nom = pB(v)
for i in range(len(u_v)):
   v_pert = v.copy()
   v_pert[i] += u_v[i]
   pB_pert = nom - pB(v_pert)
   D.append(pB_pert)
u_pB = np.linalg.norm(D)
print("Pressure B: {0:.3f}±{1:.3f}".format(nom, u_pB))
# Pressure B: 106143.585±1410.685 Pa

