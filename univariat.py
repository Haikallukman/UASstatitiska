import numpy as np
import matplotlib.pyplot as plt


data = np.random.normal(loc=500, scale=20, size=1500)


mean = np.mean(data)
variance = np.var(data)


print(f"Mean: {mean:.2f}")
print(f"Varians: {variance:.2f}")


plt.hist(data, bins=30, density=True)
plt.title("Distribusi Normal - Variabel Random Univariat")
plt.xlabel("Nilai")
plt.ylabel("Kepadatan Frekuensi")
plt.show()
