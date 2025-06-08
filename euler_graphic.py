import matplotlib.pyplot as plt

g = 9.81
dt = 0.1
x = 100.0
v = 0.0
t = 0.0

waktu = []
posisi = []
kecepatan = []

while x > 0:
    waktu.append(t)
    posisi.append(x)
    kecepatan.append(v)
    x = x - v * dt
    v = v + g * dt
    t += dt

waktu.append(t)
posisi.append(x)
kecepatan.append(v)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(waktu, posisi, color='blue', marker='o')
plt.title('Grafik Posisi terhadap Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Posisi (m)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(waktu, kecepatan, color='orange', marker='o')
plt.title('Grafik Kecepatan terhadap Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Kecepatan (m/s)')
plt.grid(True)

plt.tight_layout()
plt.show()
