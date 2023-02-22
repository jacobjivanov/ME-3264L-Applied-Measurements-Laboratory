import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize = (6.5, 2.5))
fig.tight_layout(pad = 3.25)
p_IWC = np.array([101325, 106143.585, 106143.585, 104801.183, 104801.183]) / 1000
up_IWC = np.array([0, 1410.685, 1410.685, 1926.619, 1926.619]) / 1000
v_IWC = np.array([91369.413, 87221.529, 129529.946, 131189.100, 87221.529])
uv_IWC = np.array([859.369, 826.769, 1169.136, 1182.886, 826.769])

p_RTWC = np.array([101325, 106143.585, 106143.585, 103218.306, 103218.306]) / 1000
up_RTWC = np.array([0, 1410.685, 1410.685, 1905.130, 1905.130]) / 1000
v_RTWC = np.array([91369.413, 87221.529, 117086.294, 120404.602, 88880.683])
uv_RTWC = np.array([859.369, 826.769, 1066.614, 1093.842, 839.774])

ax[0].scatter(v_IWC, p_IWC, color = "blue")
ax[0].errorbar(v_IWC, p_IWC, xerr = uv_IWC, yerr = up_IWC, ecolor = "grey", capsize = 5, color = "blue", linestyle = "dashed")

ax[1].scatter(v_RTWC, p_RTWC, color = "red")
ax[1].errorbar(v_RTWC, p_RTWC, xerr = uv_RTWC, yerr = up_RTWC, ecolor = "grey", capsize = 5, color = "red", linestyle = "dashed")

labels = ["A", "B", "C", "D", "A'"]
for i in range(len(labels)):
   ax[0].annotate(labels[i], (v_IWC[i] + 2500, p_IWC[i] + 0.25))
   ax[1].annotate(labels[i], (v_RTWC[i] + 2500, p_RTWC[i] + 0.25))


ax[0].set_ylim(100, 108)
ax[1].set_ylim(100, 108)
ax[0].set_xlim(80000, 140000)
ax[1].set_xlim(80000, 140000)

ax[0].set_ylabel("Pressure (kPa)")
ax[1].set_ylabel("Pressure (kPa)")
ax[0].set_xlabel("Volume (cubic mm)")
ax[1].set_xlabel("Volume (cubic mm)")

ax[0].set_title("Ice Water Cycle")
ax[1].set_title("Room Temperature Water Cycle")

fig.suptitle("Figure 1: Comparison of Cycles (Ideal Gas Pressures)")

plt.show()
fig.savefig('Figure 1.png', dpi = 300)