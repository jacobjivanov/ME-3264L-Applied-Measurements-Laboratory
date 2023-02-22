import numpy as np
import matplotlib.pyplot as plt

power = np.array([2.92, 5.93, 9.02, 12.06])
u_power = np.array([0.04, 0.06, 0.08, 0.09])

k = np.array([5745.9499741641, 6189.5908493022, 6155.9930829434, 6337.1916733597])
u_k = np.array([596.29479676589, 600.79905636588, 581.21238808433, 544.38513582266])

fig, ax = plt.subplots(1, 1, figsize = (6.5, 3))
plt.tight_layout(pad = 3)

plt.scatter(power, k, color = "blue", label = "Heat Pipe")
plt.errorbar(power, k, xerr = u_power, yerr = u_k, ecolor = "grey", capsize = 5, color = "blue")
plt.axhline(398, color = "orange", label = "Copper")

plt.xlim(2, 14)
plt.xlabel("Power Input (W)")
plt.ylim(0, 8000)
plt.ylabel(r"Thermal Conductivity $\left(\frac{\mathrm{W}}{\mathrm{m \cdot K}}\right)$")
plt.title("Figure 3: Comparison of Thermal Conductivity")
plt.legend()
plt.show()
fig.savefig('Figure 3.png', dpi = 300)